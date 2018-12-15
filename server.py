import http
import http.server
import time


class CrawlLogHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        print(time.asctime(), "HEAD")
        print(self.headers)
        print()

    def do_GET(self):
        self.send_response(200)
        print(time.asctime(), "GET")
        print(self.headers)
        print()

    def do_CONNECT(self):
        self.send_response(200)
        print(time.asctime(), "CONNECT")
        print(self.headers)
        print()


if __name__ == '__main__':
    server_class = http.HTTPServer
    HOST_NAME = 'localhost'
    PORT_NUMBER = 8890
    httpd = server_class((HOST_NAME, PORT_NUMBER), CrawlLogHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
