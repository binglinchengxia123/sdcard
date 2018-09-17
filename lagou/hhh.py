import requests
import json

s = requests.session()

def post1():

    # url = "http://222.190.125.58:80/newphonebank3/shopadvert.do?"
    url = "http://jandan.net/?oxwlxojflwblxbsapi=jandan.get_ooxx_comments&page=1"
    p=s.post(url)
    result = p.json()
    #print(result)
    print(type(result))
    # page = result["comment_author"]
    # print(page)
    # data = result["comments"]
    # print(data['comments'][0]['comment_author'])
    # for i in data:
    #     if "kafka" in i["comment_author"]:
    #         print(i)
    # r = p.json()
    # print(r['comments'][2]['comment_author'])
    print(json.dumps(result, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    post1()
