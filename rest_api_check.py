import json
import requests
from flask import Blueprint, render_template, request

resource_blueprint = Blueprint('soc_term_project', __name__)


@resource_blueprint.route("/rest_api_check")
def rest_api_check(word=None):

    return render_template("api_check.html", word=word, nav_menu='api_print')


@resource_blueprint.route("/rest_api_print", methods=['POST'])
def rest_api_print():
    if request.method == 'POST':
        search_word = request.form['search_word']
        index = request.form['index']
    else:
        search_word = None
        index = None

    if len(index) == 0:
        res = requests.get(
            url='http://localhost:8080/integrated_search/' + str(search_word)
        )
    elif len(index) > 0:
        res = requests.get(
            url='http://localhost:8080/integrated_search/' + str(search_word) + '/' + str(index)
        )

    result = json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))

    return render_template("api_check.html", word=search_word, resource=result, nav_menu='api_print')


@resource_blueprint.route("/example_page_input")
def example_page_input(word=None):

    return render_template("example_page.html", word=word, nav_menu='example_page')


@resource_blueprint.route("/example_page",  methods=['POST'])
def example_page():
    if request.method == 'POST':
        search_word = request.form['search_word']
        index = request.form['index']
    else:
        search_word = None
        index = None

    if len(index) == 0:
        res = requests.get(
            url='http://localhost:8080/integrated_search/' + str(search_word)
        )
    elif len(index) > 0:
        res = requests.get(
            url='http://localhost:8080/integrated_search/' + str(search_word) + '/' + str(index)
        )

    result = json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    res_dict = json.loads(result)

    return render_template("example_page.html", word=search_word, resource=res_dict, nav_menu='example_page')


@resource_blueprint.route("/manual")
def manual():

    return render_template("manual.html", nav_menu='manual')