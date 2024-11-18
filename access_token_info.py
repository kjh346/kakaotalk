import requests

ACCESS_TOKEN = "UZK3eIDN9xgfz2TNu6xElQ_65RECxdxxAAAAAQo9c-wAAAGTPVTevaj01SImjvGc"

url = "https://kapi.kakao.com/v1/user/access_token_info"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url, headers=headers)
print(response.json())
