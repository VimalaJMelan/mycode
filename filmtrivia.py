import requests

import pprint

#request url
TURL = "https://opentdb.com/api.php?amount=1&category=11&difficulty=medium&type=boolean"


def main():

    resp = requests.get(TURL)

    respjson = resp.json()

    print(respjson)

    question = respjson['results'][0]['question']
    print(question)



if __name__ == "__main__":
    main()
