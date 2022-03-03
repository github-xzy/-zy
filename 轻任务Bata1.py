from json.tool import main
import requests
import time

#修改你成自己的Cookie
#账号Cookie = {"Cookie":"这里输入你的cookie"} 
#注意⚠️结尾的 " 双引号和 } 打括号

账号Cookie = {"Cookie":""}
mission = "1709"
视频数量requirement = "3630189452809594562"
主页时间requirement = "3630154268437505730"
话题时间requirement = "3630083899693328066"
主页author = "101873038474"
话题topic = "1724894125742088"
url = "https://aweme.snssdk.com/ad/mission/openapi/report_event?event_type=1&aid=1128"


def 刷视频数量():
    时间戳 = str(int(time.time()))
    视频请求参数 = {
                "msg_type":10002,
                "update_type":1,
                "mission_id":mission,
                "requirement_id":视频数量requirement,
                "item_id":时间戳,
                "author_id":主页author,
                "item_source":1
                }

    R = requests.post(url,json=视频请求参数,cookies=账号Cookie)
    print(R.text)

def 刷主页时间():
    主页请求参数 = {
                "msg_type":10001,
                "update_type":0,
                "mission_id":mission,
                "requirement_id":主页时间requirement,
                "author_id":主页author,
                "duration":60000
                }

    R = requests.post(url,json=主页请求参数,cookies=账号Cookie)
    print(R.text)


def 刷话题时间():
    主页请求参数 = {
                "msg_type":10003,
                "update_type":0,
                "mission_id":mission,
                "requirement_id":话题时间requirement,
                "topic_id":话题topic,
                "duration":60000
                }

    R = requests.post(url,json=主页请求参数,cookies=账号Cookie)
    print(R.text)

#点赞任务有问题正在测试
def 点赞任务():
    url = "https://www.douyin.com/aweme/v1/web/commit/item/digg/?"
    点赞任务请求参数 = "aweme_id=7063430928642755877&item_type=0&type=1"

    R = requests.post(url,data=点赞任务请求参数,cookies=账号Cookie)
    print(R.text)

#在range()输入你需刷的数量 如range(1000) 这就是刷1000次 时间1次/1分钟 视频1次/1条
if __name__ == '__main__':    
    for _ in range(0):
        刷主页时间()
        time.sleep(0.5)

    for _ in range(0):
        刷视频数量()
        time.sleep(1)

    for _ in range(0):
        刷话题时间()
        time.sleep(0.5)