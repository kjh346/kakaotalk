import requests

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "authorization_code",
    "client_id": "78febd09f9d2505fe2035b17ef6156bd",
    "redirect_uri": "http://localhost:5000/oauth/callback",
    "code": "HJBA3ZTEpT3eJ6DsJFgt184WE1fsaugQVplGxoLJbiAyS9kWHhcwLQAAAAQKKiUPAAABkz1Uo2insOtctwzlGQ"
}

response = requests.post(url, data=data)  # data 사용
print(response.json())
