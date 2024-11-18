import json
import requests

ACCESS_TOKEN = "UZK3eIDN9xgfz2TNu6xElQ_65RECxdxxAAAAAQo9c-wAAAGTPVTevaj01SImjvGc"
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
}

data = {
    "template_object": {
        "object_type": "text",
        "text": "안녕하세요! 나에게 보내는 테스트 메시지입니다.",
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
