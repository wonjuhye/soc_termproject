import json
import math
import xml.etree.ElementTree as ET
import requests
from keys import GOOGLE_API_KEY_1, GOOGLE_APT_google_KEY, GOOGLE_APT_youtube_KEY, DBPIA_API_KEY, KOCW_API_KEY, \
    GOOGLE_API_KEY_2

GOOGLE_BASE_URL = "https://www.googleapis.com/customsearch/v1?"
DBPIA_BASE_URL = "http://api.dbpia.co.kr/v2/search/search.xml?"
KOCW_BASE_URL = "http://www.kocw.net/home/api/handler.do?"


def getGoogleSearchInformation(str_input, index):
    res = requests.get(
        url=GOOGLE_BASE_URL + 'key=' + GOOGLE_API_KEY_1 + '&cx=' + GOOGLE_APT_google_KEY +
            '&q=' + str_input + '&start=' + str(1 + (index - 1) * 10)
    )

    if res.status_code == 200:
        docs = res.json()
        nextIndex = math.trunc(int(docs['queries']['nextPage'][0]['startIndex']) / 10) + 1
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
        url=GOOGLE_BASE_URL + 'key=' + GOOGLE_API_KEY_2 + '&cx=' + GOOGLE_APT_youtube_KEY +
            '&q=' + str_input + '&start=' + str(1 + (index - 1) * 10)
    )

    if res.status_code == 200:
        docs = res.json()
        nextIndex = math.trunc(int(docs['queries']['nextPage'][0]['startIndex']) / 10) + 1
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
        url=DBPIA_BASE_URL + 'key=' + DBPIA_API_KEY + '&target=se' + '&searchall=' + str_input
            + '&pagenumber=' + str(index)
    )

    if res.status_code == 200:
        docs = res.text
        tree = ET.fromstring(docs)
        nextIndex = index + 1
        result = []
        for item in tree.findall('./result/items/item'):
            tmp = {"title": str(item.find('title').text).replace("<!HS>", "").replace("<!HE>", ""),
                   "link": item.find('link_url').text}
            result.append(tmp)

        searchInformation = {"status": res.status_code,
                             "nextPage": nextIndex,
                             "searchResult": result
                             }
    else:
        searchInformation = {"error": res.status_code}

    return searchInformation


# def getKOCWSearchInformation(str_input, index):
#     res = requests.get(
#         url=KOCW_BASE_URL + 'key=' + KOCW_API_KEY + '&category_type=t' + '&category_id=' +
#             str_input + '&end_num=20' + '&from=20170101'
#     )
#
#     if res.status_code == 200:
#         docs = res.text
#         tree = ET.fromstring(docs)
#         result = []
#         for item in tree.findall('./list/list_item'):
#             if (item.find('course_title') is not None) & (item.find('course_url') is not None) & (
#                     item.find('course_description') is not None):
#                 tmp = {"title": item.find('course_title').text,
#                        "link": item.find('course_url').text,
#                        "description": item.find('course_description').text
#                        }
#                 result.append(tmp)
#
#         searchInformation = {"status": res.status_code,
#                              "nextPage": index+1,
#                              "searchResult": result
#                              }
#     else:
#         searchInformation = {"error": res.status_code}
#
#     return searchInformation
