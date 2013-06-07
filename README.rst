Flask-ESClient
==============

Flask-ESClient is a Flask extension for ESClient_ (elasticsearch client).

.. _ESClient: https://github.com/eriky/ESClient

Here is an example::

  from flask import Flask
  from flask_esclient import ESClient

  app = Flask(__name__)
  app.config['ELASTICSEARCH_URL'] = 'http://localhost:9200/'
  esclient = ESClient(app)

  @app.route('/add_document')
  def add_document():
      # Construct the data dynamically
      data = {
        "title": "Some Title",
        "content": "Some content",
        }
      esclient.connection.index("app1",
                                "something",
                                body=data,
                                docid=1) # docid should be dynamically changed


