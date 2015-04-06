import tornado
from models import NewsAkhbar,Author

__author__ = 'HASHEM'


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        CatInfo = NewsAkhbar.select().order_by(NewsAkhbar.id.desc())

        self.render('index.html', CatInfo=CatInfo)


class FivePostHandler(tornado.web.RequestHandler):
    def get(self):
        CatInfo = NewsAkhbar.select().order_by(NewsAkhbar.id.desc()).limit(5)

        self.render('index.html', CatInfo=CatInfo)


class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        CatInfo = NewsAkhbar.select().order_by(NewsAkhbar.id.desc())

        self.render('admin.html', CatInfo=CatInfo)