from django.db import models
from bs4 import BeautifulSoup
import requests
import goslate

def Crawler(target_url):
    req = requests.get(target_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.select(
        'body > div.fluid > article > div > div.l-main-container > div > div > div.l-main-container > div > div.article-entry.text > p'
        )
    contents_body = ''
    for ptag in body:
        contents_body += ptag.getText()

    title = soup.find("meta",  property="og:title")
    url = soup.find("meta",  property="og:url")
    image = soup.find("meta",  property="og:image")

    contents_title = title["content"] if title else "No Title"
    contents_url = url["content"] if url else "No Url"
    contents_image= image["content"] if image else ""

    return contents_body, contents_title, contents_url, contents_image

def Translator(contents_body, contents_title, contents_url, contents_image):
    gs = goslate.Goslate()
    return gs.translate(contents_body, 'ko'), gs.translate(contents_title, 'ko')

