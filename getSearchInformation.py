import math
import pprint

import requests
from keys import GOOGLE_API_KEY, GOOGLE_APT_google_KEY, GOOGLE_APT_youtube_KEY

GOOGLE_BASE_URL = "https://www.googleapis.com/customsearch/v1?"


def getGoogleSearchInformation(str_input, index):
    res = requests.get(
        url=GOOGLE_BASE_URL + 'key=' + GOOGLE_API_KEY + '&cx=' + GOOGLE_APT_google_KEY +
        '&q=' + str_input + '&start=' + str(1+(index-1)*10)
    )

    if res.status_code == 200:
        docs = res.json()
        nextIndex = math.trunc(int(docs['queries']['nextPage'][0]['startIndex'])/10) + 1
        result = []
        for item in docs['items']:
            tmp = {"title": item['title'], "snippet": item['snippet'], "link": item['link']}
            result.append(tmp)
        searchInformation = {"status": res.status_code,
                             "nextPage": nextIndex,
                             "searchResult": result
                             }
    else:
        searchInformation = {"error": res.status_code}

    return searchInformation


def getYoutubeSearchInformation(str_input, index):
    res = requests.get(
        url=GOOGLE_BASE_URL + 'key=' + GOOGLE_API_KEY + '&cx=' + GOOGLE_APT_youtube_KEY +
        '&q=' + str_input + '&start=' + str(1+(index-1)*10)
    )

    if res.status_code == 200:
        docs = res.json()
        nextIndex = math.trunc(int(docs['queries']['nextPage'][0]['startIndex'])/10) + 1
        result = []
        for item in docs['items']:
            tmp = {"title": item['title'], "snippet": item['snippet'], "link": item['link']}
            result.append(tmp)
        searchInformation = {"status": res.status_code,
                             "nextPage": nextIndex,
                             "searchResult": result
                             }
    else:
        searchInformation = {"error": res.status_code}

    return searchInformation
