from json.tool import main
import requests
import time

#修改你成自己的Cookie
账号Cookie = {"Cookie":"MONITOR_WEB_ID=14b44ff9-0d41-4556-b406-6d37831339f7; xgplayer_device_id=6236723659; xgplayer_user_id=584798479008; ttcid=6dc7acf6146f4281b8753c48d4e6cd9f67; _ga=GA1.2.2098459727.1639628602; ttwid=1|i49N8G4wgneC-7WIxQYWew_C8KCe8XaDeeBu4xtaPmk|1641646386|18f40ffd6b02b6ad8cd841ddfc360498c1c968aae4d612c958aa0baf634c211b; passport_csrf_token_default=27c42bda569005f7112e9e5f46b8ac0e; passport_csrf_token=27c42bda569005f7112e9e5f46b8ac0e; n_mh=cQhYQOv62JEr8cSOkcYXhp5xvmgk-yrE4nntLosXLsg; THEME_STAY_TIME=299649; IS_HIDE_THEME_CHANGE=1; pwa_guide_count=3; AB_LOGIN_GUIDE_TIMESTAMP=1646286476944; sso_uid_tt=104b5f6447384f169eca659227a0f6fc; sso_uid_tt_ss=104b5f6447384f169eca659227a0f6fc; toutiao_sso_user=fe831e7b61c945420f5ee475276cf157; toutiao_sso_user_ss=fe831e7b61c945420f5ee475276cf157; sid_ucp_sso_v1=1.0.0-KDhlMGI5OTUxOGU3NDExYzIzNTNhNTA5ODAzNzc1MzMxZDllODg1NzAKHQi0tJ_l8gIQr62BkQYY7zEgDDCni8TYBTgGQPQHGgJsZiIgZmU4MzFlN2I2MWM5NDU0MjBmNWVlNDc1Mjc2Y2YxNTc; ssid_ucp_sso_v1=1.0.0-KDhlMGI5OTUxOGU3NDExYzIzNTNhNTA5ODAzNzc1MzMxZDllODg1NzAKHQi0tJ_l8gIQr62BkQYY7zEgDDCni8TYBTgGQPQHGgJsZiIgZmU4MzFlN2I2MWM5NDU0MjBmNWVlNDc1Mjc2Y2YxNTc; passport_auth_status=399444230feb253980c372cd58ecc5b9,d9f77079f0a6d25b906707da9aca8a87; passport_auth_status_ss=399444230feb253980c372cd58ecc5b9,d9f77079f0a6d25b906707da9aca8a87; sid_guard=cc164ab62f691661582677663fd3efa9|1646286512|5183999|Mon,+02-May-2022+05:48:31+GMT; uid_tt=f00f85558c0acff62e73e25c23b33903; uid_tt_ss=f00f85558c0acff62e73e25c23b33903; sid_tt=cc164ab62f691661582677663fd3efa9; sessionid=cc164ab62f691661582677663fd3efa9; sessionid_ss=cc164ab62f691661582677663fd3efa9; sid_ucp_v1=1.0.0-KDI1NjQyOGIzODM1NGE2Y2IzYzFmNzBlZjBhMTE3Nzg5ZTZkZmE4ZGYKFwi0tJ_l8gIQsK2BkQYY7zEgDDgGQPQHGgJsZiIgY2MxNjRhYjYyZjY5MTY2MTU4MjY3NzY2M2ZkM2VmYTk; ssid_ucp_v1=1.0.0-KDI1NjQyOGIzODM1NGE2Y2IzYzFmNzBlZjBhMTE3Nzg5ZTZkZmE4ZGYKFwi0tJ_l8gIQsK2BkQYY7zEgDDgGQPQHGgJsZiIgY2MxNjRhYjYyZjY5MTY2MTU4MjY3NzY2M2ZkM2VmYTk; odin_tt=5d18a340ef6664810e602a610e5bf545e7b55aeaca4ee56e27d4dc0a76085dcddb589a8516784f411c66adcfba0660c0; home_can_add_dy_2_desktop=1; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAS0Wj8Rp2rRc87qN5bY4Kp8thaq4rPKFdSVDd-tg9toY/1646323200000/0/0/1646287113953; __ac_nonce=0622056b800be18c4a8b5; __ac_signature=_02B4Z6wo00f010zbJpgAAIDA2A19lCu14EdM.yIAALEhzEbAPAppcLDWrBOP7kbCdOZ6dIwfDezmv1ISV6lnX5P9MXjfzjohCmR4Pm6iuJ1w-NOCk1hHNJGJys.UReh7jtTAEUOUNi1UrX.jdd; csrf_session_id=92c1a3d2be804d36a91e384655c84100; s_v_web_id=verify_l0akhm0j_DUMqT7kR_aql7_4qyj_AUHy_21tJomiE7jDR; tt_scid=TzurQ.VCoAzJRznA8iwppDWfmmHDH.vmb75mDz3hVILti8uLRAAdZsBZcwNMSh1tcc12; live_can_add_dy_2_desktop=1; msToken=FAX76ZgvYIP7-1XP72WU_As9UOT1g3QeAH7JCc6_CYZysk080-obISYELyI8tiVzyXi-JBdCEEsL91xfRNe-2OqmpNYYQX8ZcTiIbDQANY9YhlbqHhPTuNx5hbE=; msToken=3v9Uo6JXRxazeYvm4Y23t6MkWJBVWrp-2MTewvjyY4AmzSmvzJ7SSfzy5maLEZvBb9-ayMECWOC8C2GUU21iKv8p2xJmTzU3HfaH0isrisjVTR-ktMRpgnmbd2pi"}

# 账号Cookie = {"Cookie":"MONITOR_WEB_ID=14b44ff9-0d41-4556-b406-6d37831339f7; xgplayer_device_id=6236723659; xgplayer_user_id=584798479008; ttcid=6dc7acf6146f4281b8753c48d4e6cd9f67; _ga=GA1.2.2098459727.1639628602; ttwid=1|i49N8G4wgneC-7WIxQYWew_C8KCe8XaDeeBu4xtaPmk|1641646386|18f40ffd6b02b6ad8cd841ddfc360498c1c968aae4d612c958aa0baf634c211b; passport_csrf_token_default=27c42bda569005f7112e9e5f46b8ac0e; passport_csrf_token=27c42bda569005f7112e9e5f46b8ac0e; n_mh=cQhYQOv62JEr8cSOkcYXhp5xvmgk-yrE4nntLosXLsg; THEME_STAY_TIME=299649; IS_HIDE_THEME_CHANGE=1; pwa_guide_count=3; AB_LOGIN_GUIDE_TIMESTAMP=1646286476944; sso_uid_tt=104b5f6447384f169eca659227a0f6fc; sso_uid_tt_ss=104b5f6447384f169eca659227a0f6fc; toutiao_sso_user=fe831e7b61c945420f5ee475276cf157; toutiao_sso_user_ss=fe831e7b61c945420f5ee475276cf157; sid_ucp_sso_v1=1.0.0-KDhlMGI5OTUxOGU3NDExYzIzNTNhNTA5ODAzNzc1MzMxZDllODg1NzAKHQi0tJ_l8gIQr62BkQYY7zEgDDCni8TYBTgGQPQHGgJsZiIgZmU4MzFlN2I2MWM5NDU0MjBmNWVlNDc1Mjc2Y2YxNTc; ssid_ucp_sso_v1=1.0.0-KDhlMGI5OTUxOGU3NDExYzIzNTNhNTA5ODAzNzc1MzMxZDllODg1NzAKHQi0tJ_l8gIQr62BkQYY7zEgDDCni8TYBTgGQPQHGgJsZiIgZmU4MzFlN2I2MWM5NDU0MjBmNWVlNDc1Mjc2Y2YxNTc; passport_auth_status=399444230feb253980c372cd58ecc5b9,d9f77079f0a6d25b906707da9aca8a87; passport_auth_status_ss=399444230feb253980c372cd58ecc5b9,d9f77079f0a6d25b906707da9aca8a87; sid_guard=cc164ab62f691661582677663fd3efa9|1646286512|5183999|Mon,+02-May-2022+05:48:31+GMT; uid_tt=f00f85558c0acff62e73e25c23b33903; uid_tt_ss=f00f85558c0acff62e73e25c23b33903; sid_tt=cc164ab62f691661582677663fd3efa9; sessionid=cc164ab62f691661582677663fd3efa9; sessionid_ss=cc164ab62f691661582677663fd3efa9; sid_ucp_v1=1.0.0-KDI1NjQyOGIzODM1NGE2Y2IzYzFmNzBlZjBhMTE3Nzg5ZTZkZmE4ZGYKFwi0tJ_l8gIQsK2BkQYY7zEgDDgGQPQHGgJsZiIgY2MxNjRhYjYyZjY5MTY2MTU4MjY3NzY2M2ZkM2VmYTk; ssid_ucp_v1=1.0.0-KDI1NjQyOGIzODM1NGE2Y2IzYzFmNzBlZjBhMTE3Nzg5ZTZkZmE4ZGYKFwi0tJ_l8gIQsK2BkQYY7zEgDDgGQPQHGgJsZiIgY2MxNjRhYjYyZjY5MTY2MTU4MjY3NzY2M2ZkM2VmYTk; odin_tt=5d18a340ef6664810e602a610e5bf545e7b55aeaca4ee56e27d4dc0a76085dcddb589a8516784f411c66adcfba0660c0; home_can_add_dy_2_desktop=1; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAS0Wj8Rp2rRc87qN5bY4Kp8thaq4rPKFdSVDd-tg9toY/1646323200000/0/0/1646287113953; __ac_nonce=0622056b800be18c4a8b5; __ac_signature=_02B4Z6wo00f010zbJpgAAIDA2A19lCu14EdM.yIAALEhzEbAPAppcLDWrBOP7kbCdOZ6dIwfDezmv1ISV6lnX5P9MXjfzjohCmR4Pm6iuJ1w-NOCk1hHNJGJys.UReh7jtTAEUOUNi1UrX.jdd; csrf_session_id=92c1a3d2be804d36a91e384655c84100; s_v_web_id=verify_l0akhm0j_DUMqT7kR_aql7_4qyj_AUHy_21tJomiE7jDR; tt_scid=TzurQ.VCoAzJRznA8iwppDWfmmHDH.vmb75mDz3hVILti8uLRAAdZsBZcwNMSh1tcc12; live_can_add_dy_2_desktop=1; msToken=FAX76ZgvYIP7-1XP72WU_As9UOT1g3QeAH7JCc6_CYZysk080-obISYELyI8tiVzyXi-JBdCEEsL91xfRNe-2OqmpNYYQX8ZcTiIbDQANY9YhlbqHhPTuNx5hbE=; msToken=3v9Uo6JXRxazeYvm4Y23t6MkWJBVWrp-2MTewvjyY4AmzSmvzJ7SSfzy5maLEZvBb9-ayMECWOC8C2GUU21iKv8p2xJmTzU3HfaH0isrisjVTR-ktMRpgnmbd2pi"}







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
    for _ in range(1):
        刷主页时间()
        time.sleep(0.5)

    for _ in range(0):
        刷视频数量()
        time.sleep(1)

    for _ in range(1):
        刷话题时间()
        time.sleep(0.5)