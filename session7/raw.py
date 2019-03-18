# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pyexcel
# from collections import OrderedDict

# # 1. Creat connection
# url = 'https://dantri.com.vn/'
# conn = urlopen(url)
# # Download page
# raw_data = conn.read()
# html_content = raw_data.decode('utf-8')

# # 2. Find ROI
# soup = BeautifulSoup(html_content, "html.parser")
# ul = soup.find("ul","ul1 ulnew")
# li_list = ul.find_all("li")


# # 3. Extract ROI
# newslist = []
# for li in li_list:
#     h4 = li.h4
#     a = h4.a
#     title = a.string
#     link = url + a["href"]
#     News = OrderedDict({
#         "Title": title.lstrip().rstrip(),
#         "Link": link.lstrip().rstrip()})
#     newslist.append(News)
#     # print("Title:",title.lstrip())
#     # print("Link:",link)
#     # print("*"*50)
# print(newslist)


# # 4. Save DATA
# pyexcel.save_as(records=newslist, dest_file_name="Báo Hôm Nay.xls")


