#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-07-21
# Author: Master Yumi
# Email : yumi@meishixing.com

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
import os

from tornado.options import define, options
define("port", default=8866, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/reqicaitang/download")

class DownloadIndex(tornado.web.RequestHandler):
    def get(self, appname=None):
        appname_cn = "七彩糖"
        if appname == "reqicaitang":
            appname_cn = "七彩糖"
        self.render("index.html", result={"appname": appname, "appname_cn": appname_cn})

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/index", IndexHandler), (r"/(\S+)/download", DownloadIndex)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
