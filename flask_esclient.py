import esclient

from flask import current_app
from flask import _app_ctx_stack as stack


class ESClient(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('ELASTICSEARCH_URL', 'http://localhost:9200/')

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'esclient_connection'):
                ctx.esclient_connection = esclient.ESClient(current_app.config['ELASTICSEARCH_URL'])
            return ctx.esclient_connection
