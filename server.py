import Settings
import tornado.ioloop
import tornado.web
import tornado.httpserver
import json
from Shape import *

PORT = 8888
SHAPE_FILE = "tl_2014_us_zcta510"
WEBPAGE = "zipmap.html"
DEFAULT_LAT, DEFAULT_LNG = 37.792783, -122.404301
shape = Shape(SHAPE_FILE)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/lat=[-+]?\d+.?\d+&lng=[-+]?\d+.\d+", QueryHandler)
        ]
        settings = {
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,
        }
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            lat, lng = DEFAULT_LAT, DEFAULT_LNG
            res = shape.searchZip(lat, lng)
            self.render(WEBPAGE, points=res[1])
        except Exception:
            self.write("ERROR(GET): MainHandler")

class QueryHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            uri = self.request.uri
            tokens = uri.strip().split("=")
            lat, lng = float(tokens[1].split("&")[0]), float(tokens[2])
            res = shape.searchZip(lat, lng)
            self.write(str(res[0]) + ":" + str(res[1]))
        except Exception:
            self.write("ERROR(GET): QueryHandler")


def main():
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    print "Server Launched..."
    http_server.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
