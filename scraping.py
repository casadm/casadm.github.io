from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

url= "https://github.com/humanitiesprogramming/scraping-corpus"
#print(url + "/subdomain")
html = request.urlopen(url).read()
# print(html[:2000])
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all("a")[0:10]
#print(soup.text.replace("\n", "")[0:1000])
#print(soup.select(".content"))
#
# for link in soup.select("td.content a"):
#     print(link.text)
#     print("https://github.com/humanitiesprogramming/scraping-corpus/" + url)
#
links_html = soup.select("td.content a")
urls = []
for link in links_html:
    url = link["href"].replace("blob/", "")
    urls.append("https://raw.githubusercontent.com" + url)
#print(urls)
corpus_texts = []
for url in urls:
    # print(url)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace("/n", "")
    corpus_texts.append(text)
print(corpus_texts)
