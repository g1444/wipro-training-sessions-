import requests
import json
get_url="http://127.0.0.1:5000/users"

headers={
    "Accept":"application/json",
    "User-Agent":"Python-Requests-Client"
}
response=requests.get(get_url,headers=headers,timeout=5)
post_url='http://127.0.0.1:5000/users'
body={
    "name":"vedant"

}
r1=requests.post(post_url,json=body)
print(r1.status_code)
data=json.loads(r1.text)
print(data)