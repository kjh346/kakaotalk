import requests
import json

# 카카오톡 API URL
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# Access Token (카카오 OAuth를 통해 발급받은 액세스 토큰 입력)
ACCESS_TOKEN = "UZK3eIDN9xgfz2TNu6xElQ_65RECxdxxAAAAAQo9c-wAAAGTPVTevaj01SImjvGc"

# 헤더 설정
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
}

# template_object 데이터 설정
template_object = {
    "object_type": "text",
    "text": "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
    "link": {
        "web_url": "https://developers.kakao.com",
        "mobile_web_url": "https://developers.kakao.com"
    },
    "button_title": "바로 확인"
}

# POST 요청 보내기 (data 대신 json으로 인코딩된 template_object를 전달)
response = requests.post(
    url,
    headers=headers,
    data={"template_object": json.dumps(template_object)}
)

# 응답 결과 출력
if response.status_code == 200:
    print("메시지 전송 성공:", response.json())
else:
    print("메시지 전송 실패:", response.json())
