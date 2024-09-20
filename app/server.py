from http.server import HTTPServer
from handlers import Handler

# configurando o servidor com host e porta
host = "localhost"
port = 8080
server = HTTPServer((host, port), Handler)

print(f"Servidor rodando em http://{host}:{port}")
server.serve_forever()