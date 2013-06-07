import unittest
import flask
from flask_esclient import ESClient


class BasicAppTestCase(unittest.TestCase):

    def setUp(self):
        app = flask.Flask(__name__)
        app.config['ELASTICSEARCH_URL'] = 'http://localhost:9200/'
        app.config['TESTING'] = True
        esclient = ESClient(app)

        self.app = app
        self.esclient = esclient

    def test_create_delete_index(self):

        body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            }
        }

        with self.app.test_request_context('/nowhere'):
            self.esclient.connection.delete_index('esclient_test')
            self.assertTrue(self.esclient.connection.create_index('esclient_test', body))
            self.assertTrue(self.esclient.connection.delete_index('esclient_test'))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BasicAppTestCase))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
