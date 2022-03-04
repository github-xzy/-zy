import threading
import requests
import time

url = "https://aweme.snssdk.com/ad/mission/openapi/report_event?event_type=1&aid=1128"
账号Cookie = {"Cookie":""}

def 刷视频数量(活动名):
    参数 = 活动名
    时间戳 = str(int(time.time()))
    视频请求参数 = {
                "msg_type":10002,
                "update_type":1,
                "mission_id":参数.mission,
                "requirement_id":参数.视频数量requirement,
                "item_id":时间戳,
                "author_id":参数.主页author,
                "item_source":1
                }

    R = requests.post(url,json=视频请求参数,cookies=账号Cookie)
    print(R.text)

def 刷主页时间(活动名):
    参数 = 活动名
    主页请求参数 = {
                "msg_type":10001,
                "update_type":0,
                "mission_id":参数.mission,
                "requirement_id":参数.主页时间requirement,
                "author_id":参数.主页author,
                "duration":60000
                }

    R = requests.post(url,json=主页请求参数,cookies=账号Cookie)
    print(R.text)


def 刷话题时间(活动名):
    参数 = 活动名
    主页请求参数 = {
                "msg_type":10003,
                "update_type":0,
                "mission_id":参数.mission,
                "requirement_id":参数.话题时间requirement,
                "topic_id":参数.话题topic,
                "duration":60000
                }

    R = requests.post(url,json=主页请求参数,cookies=账号Cookie)
    print(R.text)



def 刷主页时间1(活动名,次数):
    for _ in range(次数):
        刷主页时间(活动名)
        time.sleep(0.5)

def 刷视频数量2(活动名,次数):
    for _ in range(次数):
        刷视频数量(活动名)
        time.sleep(1)

def 刷话题时间3(活动名,次数):
    for _ in range(次数):
        刷话题时间(活动名)
        time.sleep(1)

