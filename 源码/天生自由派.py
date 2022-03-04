#---------------------------------------------------------#
#                       ⬆️以下内容勿动❕
#---------------------------------------------------------#
import threading
import time
import 轻任务
import 天生自由派
#---------------------------------------------------------#
#                       ⬆️以上内容勿动❕
#---------------------------------------------------------#





活动名 = 天生自由派
所有账号Cookie = {
            "许中亦":"MONITOR_WEB_ID=14b44ff9-0d41-4556-b406-6d37831339f7; xgplayer_device_id=6236723659; xgplayer_user_id=584798479008; ttcid=6dc7acf6146f4281b8753c48d4e6cd9f67; _ga=GA1.2.2098459727.1639628602; ttwid=1|i49N8G4wgneC-7WIxQYWew_C8KCe8XaDeeBu4xtaPmk|1641646386|18f40ffd6b02b6ad8cd841ddfc360498c1c968aae4d612c958aa0baf634c211b; passport_csrf_token_default=27c42bda569005f7112e9e5f46b8ac0e; passport_csrf_token=27c42bda569005f7112e9e5f46b8ac0e; n_mh=cQhYQOv62JEr8cSOkcYXhp5xvmgk-yrE4nntLosXLsg; THEME_STAY_TIME=299649; IS_HIDE_THEME_CHANGE=1; pwa_guide_count=3; AB_LOGIN_GUIDE_TIMESTAMP=1646286476944; sso_uid_tt=104b5f6447384f169eca659227a0f6fc; sso_uid_tt_ss=104b5f6447384f169eca659227a0f6fc; toutiao_sso_user=fe831e7b61c945420f5ee475276cf157; toutiao_sso_user_ss=fe831e7b61c945420f5ee475276cf157; sid_ucp_sso_v1=1.0.0-KDhlMGI5OTUxOGU3NDExYzIzNTNhNTA5ODAzNzc1MzMxZDllODg1NzAKHQi0tJ_l8gIQr62BkQYY7zEgDDCni8TYBTgGQPQHGgJsZiIgZmU4MzFlN2I2MWM5NDU0MjBmNWVlNDc1Mjc2Y2YxNTc; ssid_ucp_sso_v1=1.0.0-KDhlMGI5OTUxOGU3NDExYzIzNTNhNTA5ODAzNzc1MzMxZDllODg1NzAKHQi0tJ_l8gIQr62BkQYY7zEgDDCni8TYBTgGQPQHGgJsZiIgZmU4MzFlN2I2MWM5NDU0MjBmNWVlNDc1Mjc2Y2YxNTc; passport_auth_status=399444230feb253980c372cd58ecc5b9,d9f77079f0a6d25b906707da9aca8a87; passport_auth_status_ss=399444230feb253980c372cd58ecc5b9,d9f77079f0a6d25b906707da9aca8a87; sid_guard=cc164ab62f691661582677663fd3efa9|1646286512|5183999|Mon,+02-May-2022+05:48:31+GMT; uid_tt=f00f85558c0acff62e73e25c23b33903; uid_tt_ss=f00f85558c0acff62e73e25c23b33903; sid_tt=cc164ab62f691661582677663fd3efa9; sessionid=cc164ab62f691661582677663fd3efa9; sessionid_ss=cc164ab62f691661582677663fd3efa9; sid_ucp_v1=1.0.0-KDI1NjQyOGIzODM1NGE2Y2IzYzFmNzBlZjBhMTE3Nzg5ZTZkZmE4ZGYKFwi0tJ_l8gIQsK2BkQYY7zEgDDgGQPQHGgJsZiIgY2MxNjRhYjYyZjY5MTY2MTU4MjY3NzY2M2ZkM2VmYTk; ssid_ucp_v1=1.0.0-KDI1NjQyOGIzODM1NGE2Y2IzYzFmNzBlZjBhMTE3Nzg5ZTZkZmE4ZGYKFwi0tJ_l8gIQsK2BkQYY7zEgDDgGQPQHGgJsZiIgY2MxNjRhYjYyZjY5MTY2MTU4MjY3NzY2M2ZkM2VmYTk; odin_tt=5d18a340ef6664810e602a610e5bf545e7b55aeaca4ee56e27d4dc0a76085dcddb589a8516784f411c66adcfba0660c0; home_can_add_dy_2_desktop=1; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAS0Wj8Rp2rRc87qN5bY4Kp8thaq4rPKFdSVDd-tg9toY/1646323200000/0/0/1646287113953; __ac_nonce=0622056b800be18c4a8b5; __ac_signature=_02B4Z6wo00f010zbJpgAAIDA2A19lCu14EdM.yIAALEhzEbAPAppcLDWrBOP7kbCdOZ6dIwfDezmv1ISV6lnX5P9MXjfzjohCmR4Pm6iuJ1w-NOCk1hHNJGJys.UReh7jtTAEUOUNi1UrX.jdd; csrf_session_id=92c1a3d2be804d36a91e384655c84100; s_v_web_id=verify_l0akhm0j_DUMqT7kR_aql7_4qyj_AUHy_21tJomiE7jDR; tt_scid=TzurQ.VCoAzJRznA8iwppDWfmmHDH.vmb75mDz3hVILti8uLRAAdZsBZcwNMSh1tcc12; live_can_add_dy_2_desktop=1; msToken=FAX76ZgvYIP7-1XP72WU_As9UOT1g3QeAH7JCc6_CYZysk080-obISYELyI8tiVzyXi-JBdCEEsL91xfRNe-2OqmpNYYQX8ZcTiIbDQANY9YhlbqHhPTuNx5hbE=; msToken=3v9Uo6JXRxazeYvm4Y23t6MkWJBVWrp-2MTewvjyY4AmzSmvzJ7SSfzy5maLEZvBb9-ayMECWOC8C2GUU21iKv8p2xJmTzU3HfaH0isrisjVTR-ktMRpgnmbd2pi",
            "章若楠":"ttwid=1|veN4FTtF6Qr-H_6L_KYzrAeoV244QER4NKfyAXUJx_o|1645007911|ef5a9255489d5b368a2e678ec5e4469a3ddbc71edde6a5f56ab58d0587abc523; home_can_add_dy_2_desktop=0; AB_LOGIN_GUIDE_TIMESTAMP=1645007910518; passport_csrf_token_default=29a47535f8d2c239370ee75262cf7033; passport_csrf_token=29a47535f8d2c239370ee75262cf7033; n_mh=32GkJhfnR7GqdMQVbwB4dBYeK-1o0OKn0-LMq0CTNfU; sso_uid_tt=ef4bd8d8fadce24be8462c9f1b900c61; sso_uid_tt_ss=ef4bd8d8fadce24be8462c9f1b900c61; toutiao_sso_user=1c95a843110218821c85b997ae8f5504; toutiao_sso_user_ss=1c95a843110218821c85b997ae8f5504; sid_ucp_sso_v1=1.0.0-KDZjNGJiODIzYzQ5MmMxYWVjNTY5OThlN2E1ZGViM2NkZGY3NzBmNzYKHgig1ZDMyY1AEMyos5AGGO8xIAwwq9enhgY4BkD0BxoCbGYiIDFjOTVhODQzMTEwMjE4ODIxYzg1Yjk5N2FlOGY1NTA0; ssid_ucp_sso_v1=1.0.0-KDZjNGJiODIzYzQ5MmMxYWVjNTY5OThlN2E1ZGViM2NkZGY3NzBmNzYKHgig1ZDMyY1AEMyos5AGGO8xIAwwq9enhgY4BkD0BxoCbGYiIDFjOTVhODQzMTEwMjE4ODIxYzg1Yjk5N2FlOGY1NTA0; odin_tt=aed7ac3f6c139d47cc01a3864ae095e98ebbdb1bc6d50219941429b217cfb0ec744fe66b1a207802ab77c0670f3d39c33dd77edf5748822d0f54175bead6976e; passport_auth_status_ss=855cef8f843e435cdc268f591266b10c,; sid_guard=60ea5e64c63b232fb6842976d6666395|1645007950|5183998|Sun,+17-Apr-2022+10:39:08+GMT; uid_tt=33b88e536c1b2653d7a451a22dfda0df; uid_tt_ss=33b88e536c1b2653d7a451a22dfda0df; sid_tt=60ea5e64c63b232fb6842976d6666395; sessionid=60ea5e64c63b232fb6842976d6666395; sessionid_ss=60ea5e64c63b232fb6842976d6666395; sid_ucp_v1=1.0.0-KDQwNmEzNzZmMWJjOGE5YjFhMmQ2M2NlNWQ4MjFmYTA1M2Y0ZjBjODIKFgig1ZDMyY1AEM6os5AGGO8xOAZA9AcaAmxmIiA2MGVhNWU2NGM2M2IyMzJmYjY4NDI5NzZkNjY2NjM5NQ; ssid_ucp_v1=1.0.0-KDQwNmEzNzZmMWJjOGE5YjFhMmQ2M2NlNWQ4MjFmYTA1M2Y0ZjBjODIKFgig1ZDMyY1AEM6os5AGGO8xOAZA9AcaAmxmIiA2MGVhNWU2NGM2M2IyMzJmYjY4NDI5NzZkNjY2NjM5NQ; passport_auth_status=855cef8f843e435cdc268f591266b10c,; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAR3dDBXBi-DgWvyvNZRq3NKfh8A0ic90AWLNTzK9x33Q/1645027200000/0/1645007950777/0; FOLLOW_YELLOW_POINT_STATUE_INFO=0/1645009167833; __ac_nonce=0620cd467003f08d58c19; __ac_signature=_02B4Z6wo00f01vlHBrAAAIDCeUX88fAvMKr5ZwIAANxq98; ttcid=15d94ba093f34cde82dce0f4c830f6d367; tt_scid=qM5OkCiUNnKjHpoLtWYT5hRneSDMUtYNXG1nSBqmGVcMYjs6nMLFcJK4qUXsPdyE8ea3; live_can_add_dy_2_desktop=0; xgplayer_user_id=236613569007; csrf_session_id=9fce2eb89c28fcfad417f887ad0405e5; MONITOR_WEB_ID=b386b2ae-ffca-4bfc-baed-f921ed1bac9a; s_v_web_id=verify_kzpf9y2u_dON8eaMy_P5Ml_4Kyn_BEbV_pG4mlj4jqVdZ; msToken=P9dQm58VHCCyHw1FSiErESBCIZIkoVRX_Lu8k8MMHbt8L2ghrqkI_MTRdsAVO33n6iE1B_irMkGb4Bzkhz5htAOcp_JbVbHKNvISwUY2gDwPWbQi4MKymEEqmo0DJB0=; msToken=Y7SCA2pynTdBg7JMrXGfPhMwstsWux8BT1oTfjBWpcB-2Z7b2ijEa8M9_9kG-Thh-xty_Uafi8-ntMKJAEBLy9KwGsfgq0KCPalKX36FfwxAzegrB1_XvA==; THEME_STAY_TIME=70034",
            "名扬海":"ttwid=1|a2TNn7kaOZQGEBtAeUx3bDkSCkil4BdV8F8LlF6-OA0|1645008084|cc4a62d6286b9f54b44bde81b22099956b3bba61c5c1a439cd706166c6502685; home_can_add_dy_2_desktop=0; AB_LOGIN_GUIDE_TIMESTAMP=1645008083286; passport_csrf_token_default=6ea5ad5efe0aca782f6fbad7e21122c2; passport_csrf_token=6ea5ad5efe0aca782f6fbad7e21122c2; n_mh=WLk0YXt5YEe__-Cv-2NVMoiKwybRCx9IiSv7GRthi-g; sso_uid_tt=0fa7b183754b0316e0f57f1e263e2b03; sso_uid_tt_ss=0fa7b183754b0316e0f57f1e263e2b03; toutiao_sso_user=2edc5a67c87eb023e586bd542ff34060; toutiao_sso_user_ss=2edc5a67c87eb023e586bd542ff34060; sid_ucp_sso_v1=1.0.0-KGJhMDhlYWYzOGU4YjBjZmM2Njk2NjBlZTllMGEyMGQxOGI2MDRmOGIKHwis0cD7jY3uBhDxqbOQBhjvMSAMMIqguIwGOAZA9AcaAmxmIiAyZWRjNWE2N2M4N2ViMDIzZTU4NmJkNTQyZmYzNDA2MA; ssid_ucp_sso_v1=1.0.0-KGJhMDhlYWYzOGU4YjBjZmM2Njk2NjBlZTllMGEyMGQxOGI2MDRmOGIKHwis0cD7jY3uBhDxqbOQBhjvMSAMMIqguIwGOAZA9AcaAmxmIiAyZWRjNWE2N2M4N2ViMDIzZTU4NmJkNTQyZmYzNDA2MA; odin_tt=b7b9e8d75e6f870ec172e13172f78dac2ef5b2a0eb4910ad113ada43d67664b69ac01dac8633a9c43a9043fab822e1c9132cbcb70752125e83275c1a429e0022; passport_auth_status_ss=07c62a10a85c53793a130a34c15dd3c8,; sid_guard=d350b1a21fb990c613c8f93364972f37|1645008114|5183999|Sun,+17-Apr-2022+10:41:53+GMT; uid_tt=44ea977e85262d40bc22fc3394f72664; uid_tt_ss=44ea977e85262d40bc22fc3394f72664; sid_tt=d350b1a21fb990c613c8f93364972f37; sessionid=d350b1a21fb990c613c8f93364972f37; sessionid_ss=d350b1a21fb990c613c8f93364972f37; sid_ucp_v1=1.0.0-KDQxMzcwOThmMTFjNTdlMjc1ZDE5Zjc3MzA3Yzg3OTc4MDhhNWY3YzYKFwis0cD7jY3uBhDyqbOQBhjvMTgGQPQHGgJscSIgZDM1MGIxYTIxZmI5OTBjNjEzYzhmOTMzNjQ5NzJmMzc; ssid_ucp_v1=1.0.0-KDQxMzcwOThmMTFjNTdlMjc1ZDE5Zjc3MzA3Yzg3OTc4MDhhNWY3YzYKFwis0cD7jY3uBhDyqbOQBhjvMTgGQPQHGgJscSIgZDM1MGIxYTIxZmI5OTBjNjEzYzhmOTMzNjQ5NzJmMzc; passport_auth_status=07c62a10a85c53793a130a34c15dd3c8,; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAaoUqBGF6fivdaYwQ1rpihXGA5Bzx0mvcnBGhz6HZHGbxP2CJ8Xl6hAAmaC6_G25u/1645027200000/0/1645008115186/0; FOLLOW_YELLOW_POINT_STATUE_INFO=0/1645009316420; __ac_nonce=0620cd4f900161eaa4f99; __ac_signature=_02B4Z6wo00f01OaN0kgAAIDAZo8oCznS55DmrdbAAFu179; ttcid=0dcf6820be204f8ea66e40fbb102fb2a35; live_can_add_dy_2_desktop=0; xgplayer_user_id=86337481125; csrf_session_id=9fce2eb89c28fcfad417f887ad0405e5; MONITOR_WEB_ID=614616c0-ce35-471f-a977-b75620777130; s_v_web_id=verify_kzpfd24l_limwLXDs_8fkB_4FFa_A1VD_c9flXOcidZW3; msToken=QZexOpkZOj5gHTPuz4HoccuolkSoupGRXU7Nlo5m305oUjAIwhD8nO6Lg65Bu6Jd0XI6MKeeauhZi0db1iZYd8njc43kf5t0Tz_47n6-FyVaENC2rC620g==; msToken=1SCKQGgDcIq6G8lguyGHHUQLz_7ZK92QS5juNDdtZeT46SNqpfZyyIHFcUTSTdc9dfCYYHCEEaN_pwVXYLmJriGkyOaShRMPQKy4ANNnVCAOCvDczW_HMQ==; THEME_STAY_TIME=43503",
            }
#修改你成自己的Cookie
#账号Cookie = {
#           "账号名称1":"这里输入你的cookie值"
#           "账号名称2":"这里输入你的cookie值"
#           } 
#可以多账号执行
#注意⚠️结尾的 " 双引号和 } 打大括号（使用英文输入）

mission = "1709"
视频数量requirement = "3630189452809594562"
主页时间requirement = "3630154268437505730"
话题时间requirement = "3630083899693328066"
主页author = "101873038474"
话题topic = "1724894125742088"


#---------------------------------------------------------#
#                       ⬆️以下内容勿动❕
#---------------------------------------------------------#
def 所有账号刷主页时间(次数):
    for cookie值 in 所有账号Cookie:
        轻任务.账号Cookie["Cookie"] = 所有账号Cookie[cookie值]
        print("正在为"+cookie值+"刷主页时间")
        # print(账号Cookie) 
        轻任务.刷主页时间1(活动名,次数)

def 所有账号刷视频数量(次数):
    for cookie值 in 所有账号Cookie:
        轻任务.账号Cookie["Cookie"] = 所有账号Cookie[cookie值]
        print("正在为"+cookie值+"刷视频数量")
        # print(账号Cookie) 
        轻任务.刷视频数量2(活动名,次数)

def 所有账号刷话题时间(次数):
    for cookie值 in 所有账号Cookie:
        轻任务.账号Cookie["Cookie"] = 所有账号Cookie[cookie值]
        print("正在为"+cookie值+"刷话题时间")
        # print(账号Cookie) 
        轻任务.刷话题时间3(活动名,次数)
#---------------------------------------------------------#
#                       ⬆️以上内容勿动❕
#---------------------------------------------------------#





if __name__ == '__main__':
    所有账号刷主页时间(0)
    所有账号刷视频数量(0)
    所有账号刷话题时间(0)

#修改()括号里的次数为你需要刷多少次时间（1/1次）（0/0次）