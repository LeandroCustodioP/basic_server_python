from http.server import BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Responde a uma requisição GET com uma página simples
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Corpo da resposta: contendo HTML simples
        self.wfile.write(bytes("<html><body><h1>Hello, World!</h1></body></html>","utf-8"))