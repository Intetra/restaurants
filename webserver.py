from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from crudDB import getRestaurants
import cgi
import os
import re

Wrapper = "<div>%s</div>"
edit = "<a href='/edit_%s'>edit</a><br>"
delete = "<a href='/delete_%s'>delete</a>"
editPattern = re.compile("edit_(.*)")
deletePattern = re.compile("delete_(.*)")

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pathEnd = os.path.basename(os.path.normpath(self.path))
        try:
            if self.path.endswith("/"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                for x in getRestaurants():
                    output += Wrapper % x + edit % x + delete % x
                output += "</body></html>"
                self.wfile.write(output)
                return
#start edit ---------------------------------------------------------------
            if editPattern.match(pathEnd):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += os.path.basename(os.path.normpath(self.path))
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello!</body></html>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'>"
                output += "<h2>What would you like me to say?</h2>"
                output += "<input name='message' type='text'>"
                output += "<input type='submit' value='Submit'></form>"
                self.wfile.write(output)
                return

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>&#161Hola!<br><a href='/hello'>Back to Hello</a></body></html>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)
    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields=cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')
            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
            output += "</body></html>"
            self.wfile.write(output)

        except:
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print "...stopping web server..."
        server.socket.close()

if __name__ == '__main__':
    main()
