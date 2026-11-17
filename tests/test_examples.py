import json
import os
import subprocess
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
requests = []

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        requests.append((self.path, self.headers.get('Authorization'), body))
        data = json.dumps({'id':'test','object':'chat.completion','created':0,'model':body['model'],'choices':[{'index':0,'message':{'role':'assistant','content':'mock answer'},'finish_reason':'stop'}], 'usage':{'prompt_tokens':2,'completion_tokens':2,'total_tokens':4}}).encode()
        self.send_response(200); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(data))); self.end_headers(); self.wfile.write(data)
    def log_message(self, *args): pass

class Examples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1',0),Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever,daemon=True); cls.thread.start()
    @classmethod
    def tearDownClass(cls): cls.server.shutdown(); cls.server.server_close()
    def test_each_example_sends_supported_request_once(self):
        env = dict(os.environ, SMTOKEN_API_KEY='test-only-key', SMTOKEN_BASE_URL=f'http://127.0.0.1:{self.server.server_port}/v1', LITELLM_LOCAL_MODEL_COST_MAP='True', NO_PROXY='*', no_proxy='*')
        for name, command in [('python',['.venv/bin/python','openai_example.py']),('javascript',['node','openai_example.mjs']),('litellm',['.venv/bin/python','litellm_example.py'])]:
            with self.subTest(name=name):
                before=len(requests)
                result=subprocess.run(command,cwd=ROOT,env=env,text=True,capture_output=True,timeout=90)
                self.assertEqual(result.returncode,0,result.stderr[-2000:])
                self.assertIn('mock answer',result.stdout)
                self.assertEqual(len(requests),before+1)
                path, auth, body=requests[-1]
                self.assertEqual(path,'/v1/chat/completions')
                self.assertEqual(auth,'Bearer test-only-key')
                self.assertEqual(body['model'],'deepseek-v4.1-flash')
                self.assertIn('messages',body)
                self.assertTrue(set(body).issubset({'model','messages','max_tokens','stream','thinking'}),body)
                self.assertLessEqual(body['max_tokens'],100)
                self.assertEqual(body['thinking'],{'type':'disabled'})

if __name__ == '__main__': unittest.main()
