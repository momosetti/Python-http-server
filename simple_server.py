#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
  # GET http verb
  def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "<h1>Hello world</h1>"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        port=int(argv[1])

try:
      print('Starting server ...')
      # Server settings
      # Choose port 8080, for port 80, which is normally used for a http server, you need root access
      server_address = ('127.0.0.1', port)
      httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
      host='http://localhost:%s'%port
      print(' \033[0;37;46m Running server at',host)
      httpd.serve_forever()
except KeyboardInterrupt:
      print("^C received, shutting down the web server")
      httpd.socket.close()
