from http.client import responses
from http.server import BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Responde a uma requisição GET com uma página simples
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Corpo da resposta: contendo HTML simples
        self.wfile.write(bytes("<html><body><h1>Hello, World!</h1></body></html>","utf-8"))

    def do_POST(self):
        # Definir o tamanho do conteúdo para ler os dados enviados no POST
        content_length = int(self.headers['Content-Length'])
        # Lendo os dados enviados no corpo da requisição
        post_data = self.rfile.read(content_length)

        # Aqui você pode processar os dados, vamos supor que sejam JSON
        try:
            data = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid JSON format')
            return

        # Lógica do que fazer com os dados recebidos
        response = {
            'message': 'POST request received succefully',
            'received_data': data
        }

        # Retornar uma resposta para o cliente
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

