import requests
from bs4 import BeautifulSoup
import json

URL = "http://127.0.0.1:5001"

response = requests.get(URL)
response.raise_for_status()

# The response is JSON, not HTML
# We manually wrap it to simulate HTML scraping
html = f"<html><body><pre>{response.text}</pre></body></html>"

soup = BeautifulSoup(html, "html.parser")

raw_json = soup.find("pre").text
patients = json.loads(raw_json)

for patient in patients:
    print("Name:", patient["patient_name"])
    print("Age:", patient["age"])
    print("Disease:", patient["disease"])
    print("Doctor:", patient["doctor_assigned"])
    print("-" * 30)
