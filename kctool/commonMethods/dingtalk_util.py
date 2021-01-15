# encoding=utf-8
# @Author : wangjie
# @Time : 2019/11/27 下午5:59

import json

import requests

import config


class SendMessage():

    def __init__(self):
        access_token = config.ding_token
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(access_token)

    def post_message(self, data):
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        data = json.dumps(data)
        requests.post(self.url, data=data, headers=HEADERS)

    def send_text(self, message="我是你爸爸"):
        String_textMsg = {
            "msgtype": "text",
            "text": {"content": message},
            "at": {
                "atMobiles": ["17364782550"],
                "isAtAll": False

            }
        }
        self.post_message(String_textMsg)

    def send_markdown(self, *lines, ding_title="通知",ats=["17364782550"]):
        text = "## @17364782550\n"
        for line in lines:
            text = text + "> {}\n\n".format(line)
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": ding_title,
                "text": text

            },
            "at": {
                "atMobiles": ats,
                "isAtAll": False
            }
        }
        self.post_message(data)

    def send_action_card(self, title,text,ats=["17364782550"],btn_title="查看详情",actionURL="http://10.2.1.32:8080/incomecheck"):
        data = {
            "actionCard": {
                "title": title,
                "text": text,
                "btnOrientation": "0",
                "btns": [
                    {
                        "title": btn_title,
                        "actionURL": actionURL
                    }
                ]
            },
            "at": {
                "atMobiles": ats,
                "isAtAll": False
            },
            "msgtype": "actionCard"
        }
        self.post_message(data)


