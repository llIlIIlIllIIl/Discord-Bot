from http.server import HTTPServer, BaseHTTPRequestHandler


class ServerHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html') # <head>
        self.end_headers() # </head>
        self.wfile.write('hello world'.encode())

    def do_POST(self):
        pass

PORT = 8080
server = HTTPServer(('', PORT), ServerHandler)

print(f'서버가 {PORT}로 서비스되고 있습니다.') # 서버 상태 확인
server.serve_forever() # 서버 지속 운영
