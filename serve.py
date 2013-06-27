import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('index.html')

application = tornado.web.Application([
    (r'/$', IndexHandler), 
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': '_build/html' }),
])


if __name__ == '__main__':
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
