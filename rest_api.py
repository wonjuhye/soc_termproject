import pprint

from flask_restful import Resource, abort, reqparse
from getSearchInformation import getGoogleSearchInformation, getYoutubeSearchInformation


class SearchResult(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # self.parser.add_argument('temperature')
        # self.parser.add_argument('datetime')
        # self.parser.add_argument('location')

    def get(self, search_string):
        result = {}
        googleResult = getGoogleSearchInformation(search_string, 1);
        youtubeResult = getYoutubeSearchInformation(search_string, 1)

        if 'error' not in googleResult.keys():
            result.update({"google": googleResult})
        if 'error' not in youtubeResult.keys():
            result.update({"youtube": youtubeResult})

        if len(result) == 0:
            result.update({"error": "Data Not Found"})
            return result, 404
        else:
            return result, 200


class MultiSearchResult(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        # self.parser.add_argument('temperature')
        # self.parser.add_argument('datetime')
        # self.parser.add_argument('location')

    def get(self, search_string, index):
        result = {}
        googleResult = getGoogleSearchInformation(search_string, index);
        youtubeResult = getYoutubeSearchInformation(search_string, index)

        if 'error' not in googleResult.keys():
            result.update({"google": googleResult})
        if 'error' not in youtubeResult.keys():
            result.update({"youtube": youtubeResult})

        if len(result) == 0:
            result.update({"error": "Data Not Found"})
            return result, 404
        else:
            return result, 200
