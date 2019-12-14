import math
import xml.etree.ElementTree as ET
import pprint

import requests
from keys import GOOGLE_API_KEY, GOOGLE_APT_google_KEY, GOOGLE_APT_youtube_KEY, DBPIA_API_KEY, KOCW_API_KEY

GOOGLE_BASE_URL = "https://www.googleapis.com/customsearch/v1?"
DBPIA_BASE_URL = "http://api.dbpia.co.kr/v2/search/search.xml?"
KOCW_BASE_URL = "http://www.kocw.net/home/api/handler.do?"

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


def getDBPIASearchInformation(str_input, index):
    res = requests.get(
        url=DBPIA_BASE_URL + 'key=' + DBPIA_API_KEY + '&target=se' + '&searchall=' +
            str_input + '&pagenumber=' + str(1+(index-1)*10)
    )

    if res.status_code == 200:
        docs = res.text
        tree = ET.fromstring(docs)
        nextIndex = int(tree.find('paramdata').find('pagenumber').text) + 1
        result = []
        for item in tree.findall('./result/items/item'):
            tmp = {"title": item.find('title').text, "link_url": item.find('link_url').text}
            result.append(tmp)

        searchInformation = {"status": res.status_code,
                             "nextPage": nextIndex,
                             "searchResult": result
                             }
        pprint.pprint(searchInformation)
    else:
        searchInformation = {"error": res.status_code}

    return searchInformation


def getKOCWSearchInformation(str_input, index):
    res = requests.get(
        url=KOCW_BASE_URL + 'key=' + KOCW_API_KEY + '&category_type=t' + '&category_id=' +
            str_input + '&end_num=' + str(1+(index-1)*10)
    )

    if res.status_code == 200:
        docs = res.text
        nextIndex = math.trunc(int(docs['queries']['nextPage'][0]['startIndex'])/10) + 1
        result = []
        for list in docs['list_item']:
            tmp = {"course_title": list['course_title'], "course_url": list['course_url']}
            result.append(tmp)

        searchInformation = {"status": res.status_code,
                             "nextPage": nextIndex,
                             "searchResult": result
                             }
    else:
        searchInformation = {"error": res.status_code}

    return searchInformation