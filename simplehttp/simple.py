import os
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def send_error(self, code, message=None):
        if code == 404:
            self.error_message_format = 'File Not Found'
        SimpleHTTPRequestHandler.send_error(self, code, message)


if __name__ == '__main__':
    httpd = HTTPServer(('', 8080), MyHandler)
    print("Serving app on port 8080 ...")
    httpd.serve_forever()
