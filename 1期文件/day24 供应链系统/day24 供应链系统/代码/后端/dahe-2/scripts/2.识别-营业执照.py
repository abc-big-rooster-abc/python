import base64
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token'
response = requests.get(
    url="https://aip.baidubce.com/oauth/2.0/token",
    params={
        "grant_type": "client_credentials",
        "client_id": "PhGc5UK5e5UOkSqpNakZLpxL",
        "client_secret": "cS1OaU3GngGDdsZj2Fo7scd4j7S3M3Gw",

    }
)
data_dict = response.json()
access_token = data_dict['access_token']
print(access_token)


request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/business_license"
# 二进制方式打开图片文件
f = open('files/营业执照.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
res = requests.post(request_url, data=params, headers=headers)
res_dict = res.json()
for k, v in res_dict['words_result'].items():
    print(k, v)

