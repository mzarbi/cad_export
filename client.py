# -*- coding: utf-8 -*-
import requests

# define the URL to our face detection API
url = "http://localhost:5000/dxf"



# use our face detection API to find faces in images via image URL
payload = {"scenario_id": "3",
           "boundingBox" : "[36.84403144329702, 36.849122756425146, 36.849122756425146, 36.84403144329702, 10.194945037365857, 10.194945037365857, 10.200352370740223, 10.200352370740223]"}
r = requests.post(url, data=payload).content

print "Response: {}".format(r)