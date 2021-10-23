from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as parser

class ServerHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200) # 연결 성공 메시지 출력.

        self.send_header('content-type','text/html') # <head>
        self.end_headers() # </head>

        self.wfile.write('<p> hello world get </p>'.encode()) # text
        print('get 요청이 들어왔습니다.')

        self.wfile.write(self.path.encode()) # '/'

        self.wfile.write('<br>'.encode())
        if '?' in self.path:
            self.wfile.write(str(self.path.split('?')[1].split('&')).encode())
            print(parser.parse_qsl(self.path.split('?')[1]))
            print(dict(parser.parse_qsl(self.path.split('?')[1]))) # 딕셔너리 형태로 '?' 뒤 값들을 & 단위로 출력.

    def do_POST(self):
        self.send_response(200) # 연결 성공 메시지 출력.

        self.send_header('content-type','text/html') # <head>
        self.end_headers() # </head>

        self.wfile.write('<p> hello world post </p>'.encode()) # text
        print('post 요청이 들어왔습니다.')

        self.wfile.write(self.path.encode()) # '/'
        self.wfile.write('<br>'.encode())
        
        data = self.rfile.read(int(self.headers['Content-Length']))
        if data is not None:
            data_decode = dict(parser.parse_qs(data.decode()))
        print(f'post params = {data_decode}')

PORT = 8080
server = HTTPServer(('', PORT), ServerHandler)

print(f'서버가 {PORT}로 서비스되고 있습니다.') # 서버 상태 확인
server.serve_forever() # 서버 지속 운영
