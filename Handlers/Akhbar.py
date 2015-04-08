__author__ = 'HASHEM'

import tornado
from models import NewsAkhbar, Author, Category


class DeleteHandler(tornado.web.RequestHandler):
    def get(self, *args):
        CatId = args[0]
        CatInfo = NewsAkhbar.select().where(NewsAkhbar.id == CatId).get().delete_instance()
        self.redirect('/admin')


class EditHandler(tornado.web.RequestHandler):
    def get(self, *args):
        CatId = args[0]
        post = NewsAkhbar.select().where(NewsAkhbar.id == CatId).get()

        CatAuthor = Author.select()

        Cat = Category.select()
        self.render('akhbar-edit.html', post=post, au=CatAuthor, cat=Cat)


    def post(self, *args):
        CatId = args[0]
        CatInfo = NewsAkhbar.select().where(NewsAkhbar.id == CatId).get()

        CatInfo.title = self.get_argument("title")
        CatInfo.text = self.get_argument("text")
        CatInfo.author = self.get_argument("author")
        CatInfo.date = self.get_argument("date")
        CatInfo.category = self.get_argument("category")
        CatInfo.image = self.get_argument("image")

        CatInfo.save()

        self.redirect('/admin')


class AddHandler(tornado.web.RequestHandler):
    def get(self):
        Cat = Category.select()

        Au = Author.select()

        self.render('akhbar-new.html', cat=Cat, au=Au)

    def post(self):

        title = self.get_argument("title")
        text = self.get_argument("text")
        author = self.get_argument("author")
        date = self.get_argument("date")
        category = self.get_argument("category")
        image = self.get_argument("image")

        CatInfo = NewsAkhbar.create(
            title=title,
            text=text,
            author=author,
            date=date,
            category=category,
            image=image
        )

        self.redirect('/admin')