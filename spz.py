import base64
import requests
import json

image_path = "c:\\obr.jpg"
secret_key = "sk_0485f639dbfbea2d03533326"

with open(image_path , "rb") as image_file:
    img_base64 = base64.b64encode(image_file.read())



with open(image_path, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=eu&secret_key=%s' % (secret_key)
r = requests.post(url, data = img_base64)

print(json.dumps(r.json(), indent=2))
try:
    print({
        "Plate": r.json()["results"][0]["Plate"]
    })
except:
    print(r)