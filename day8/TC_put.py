import requests
# --------put------------#

put_url="https://api-restful-api.dev/objects/ff8081819782e69e019be407eedc2e8d"

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