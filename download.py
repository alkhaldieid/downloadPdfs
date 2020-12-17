
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys

def get_pdfs(url, folder_location):
    response = requests.get(url, folder_location)
    soup= BeautifulSoup(response.text, "html.parser")
    if not os.path.exists(folder_location):
        os.mkdir(folder_location)
    for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)
if __name__=="__main__":
    url = sys.argv[0]
    folder_location  = sys.argv[1]
    get_pdfs(url, folder_location)

    # url = 'http://hothle.com/book/book-1.html'
    # folder_location = '/home/alkhaldieid/library/hothail'
