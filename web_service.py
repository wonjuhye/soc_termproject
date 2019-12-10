from flask import Flask, render_template, session
from flask_restful import Api
import logging

from rest_api import SearchResult, MultiSearchResult
from rest_api_check import resource_blueprint

application = Flask(__name__)
application.debug = True
api = Api(application)
application.register_blueprint(resource_blueprint, url_prefix='/soc_term_project')

api.add_resource(SearchResult, "/integrated_search/<search_string>")
api.add_resource(MultiSearchResult, "/integrated_search/<search_string>/<int:index>")

@application.route('/')
def hello_html():

    return render_template(
        'index.html',
        nav_menu="home"
    )


if __name__ == "__main__":
    logging.info("Flask Web Server Started!!!")

    application.debug = True
    application.run(host="0.0.0.0", port="8080")