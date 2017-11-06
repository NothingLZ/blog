from django.test import TestCase

# Create your tests here.
import re
import requests
html = requests.get("http://jp.tingroom.com/yuedu/yd300p/")
html.encoding='utf-8'
b=html.text
# print(b)
a = re.findall("<a href=\"(.*?)\" target.*src=\"(.*?)\"",b)
for i in a:
    print(i)
