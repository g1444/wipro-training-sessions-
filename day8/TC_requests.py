import requests
# -----------get----------------#
get_url="https://api.restful-api.dev/objects"

response=requests.get(get_url)
print(response.status_code) 
print(response.json())
#-----------get----------#
# ----------post---------#
post_url="https://api.restful-api.dev/objects"

body={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

r1=requests.post(post_url,json=body)
print(r1.status_code)
print(r1.json())
#---------post------------#
# --------put------------#

put_url="https://api.restful-api.dev/objects/ff8081819782e69e019be4042b7e2e72"

put_body={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

r2=requests.put(put_url,json=put_body)
print(r2.status_code)
print(r2.json())