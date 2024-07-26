import requests
from lxml.html import fromstring,etree
import io

st_accept = "text/html"  # говорим веб-серверу,
# что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 "
                "Safari/605.1.15")
# формируем хеш заголовков
headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}

url = "https://russia.gorodrabot.ru/python?jt=удаленная+работа"
data = requests.get(url, headers=headers)
print(data.status_code)
parser = etree.HTMLParser()
dom = fromstring(data.text)
tree = etree.parse(io.StringIO(data.text), parser=parser)
arr_name = tree.xpath('.//a[@class="snippet__title-link link an-vc"]')
for i in arr_name:
    print(i.text)
