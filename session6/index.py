import requests
# lệnh dùng thư viện requests
from bs4 import BeautifulSoup
url = "https://dantri.com.vn/suc-khoe.htm"

response = requests.get(url)
print(response.content.decode())