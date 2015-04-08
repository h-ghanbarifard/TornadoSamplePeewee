__author__ = 'mojtaba.banaie'
from Handlers.index_handler import IndexHandler,FivePostHandler,AdminHandler
from Handlers.category__handler import CategoryHandler,CategoryEditHandler,CategoryDeleteHandler,CategoryNewHandler
from Handlers.Akhbar import DeleteHandler,EditHandler,AddHandler


urlList = [
    (r'/', IndexHandler),
    (r'/category$', CategoryHandler),
    (r'/category/edit/(\d+)$', CategoryEditHandler),
    (r'/category/delete/(\d+)$', CategoryDeleteHandler),
    (r'/category/new$', CategoryNewHandler),
    (r'/FivePost$', FivePostHandler),
    (r'/admin$', AdminHandler),
    (r'/New/delete/(\d+)$', DeleteHandler),
    (r'/New/Edit/(\d+)$', EditHandler),
    (r'/New/Add$', AddHandler)
]