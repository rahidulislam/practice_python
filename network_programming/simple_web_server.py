from http.server import SimpleHTTPRequestHandler,HTTPServer,BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # send the content of the response
        self.wfile.write(b'Hello, This is a custom web server response')

# Define server address and port
server_address = ('',8000) # empty string represents localhost and port 8000

# Create HTTP server
# httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd = HTTPServer(server_address, MyRequestHandler)

# print server status
print("Server running on http://localhost:8000")
# Start the server
httpd.serve_forever()

