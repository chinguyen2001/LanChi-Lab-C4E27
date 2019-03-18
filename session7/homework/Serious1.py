from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict


url = 'https://www.apple.com/itunes/charts/songs/'
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf-8')

# with open("dantri.html","wb") as f:
#     f.write(raw_data)

soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section", 'section chart-grid')
ul = section.div.ul
li_list = ul.find_all("li")

Top_Charts = []
for li in li_list:
    h3 = li.h3
    a = h3.a
    songname = a.string
    h4 = li.h4
    a2 = h4.a
    artist = a2.string
    Top_Song = OrderedDict({
        "Song": songname.lstrip().rstrip(),
        "Artist": artist.lstrip().rstrip()})
    Top_Charts.append(Top_Song)

pyexcel.save_as(records=Top_Charts, dest_file_name="iTunes Top Charts.xlsx")