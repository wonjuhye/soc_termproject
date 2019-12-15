from flask_restful import Resource, reqparse
from getSearchInformation import getGoogleSearchInformation, getYoutubeSearchInformation, getDBPIASearchInformation, getKOCWSearchInformation


class SearchResult(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self, search_string):
        result = {}
        googleResult = getGoogleSearchInformation(search_string, 1);
        youtubeResult = getYoutubeSearchInformation(search_string, 1);
        dbpiaResult = getDBPIASearchInformation(search_string, 1);
       # kocwResult = getKOCWSearchInformation(search_string, 1)

        if 'error' not in googleResult.keys():
            result.update({"google": googleResult})
        else:
            result.update({"google": googleResult["error"]})
        if 'error' not in youtubeResult.keys():
            result.update({"youtube": youtubeResult})
        else:
            result.update({"youtube": youtubeResult["error"]})
        if 'error' not in dbpiaResult.keys():
            result.update({"dbpia": dbpiaResult})
        else:
            result.update({"dbpia": dbpiaResult["error"]})
        #if 'error' not in kocwResult.keys():
         #   result.update({"kocw": kocwResult})

        if len(result) == 0:
            result.update({"error": "Data Not Found"})
            return result, 404
        else:
            return result, 200


class MultiSearchResult(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self, search_string, index):
        result = {}
        googleResult = getGoogleSearchInformation(search_string, index);
        youtubeResult = getYoutubeSearchInformation(search_string, index);
        dbpiaResult = getDBPIASearchInformation(search_string, index);
        #kocwResult = getKOCWSearchInformation(search_string, index)

        if 'error' not in googleResult.keys():
            result.update({"google": googleResult})
        else:
            result.update({"google": googleResult["error"]})
        if 'error' not in youtubeResult.keys():
            result.update({"youtube": youtubeResult})
        else:
            result.update({"youtube": youtubeResult["error"]})
        if 'error' not in dbpiaResult.keys():
            result.update({"dbpia": dbpiaResult})
        else:
            result.update({"dbpia": dbpiaResult["error"]})
        #if 'error' not in kocwResult.keys():
         #   result.update({"kocw": kocwResult})

        if len(result) == 0:
            result.update({"error": "Data Not Found"})
            return result, 404
        else:
            return result, 200
