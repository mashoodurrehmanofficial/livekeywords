import urllib.request,json
from bs4 import BeautifulSoup 
import pafy

def youtube_video_fetcher(url):
  try:
    keyword_storage = [] 
    page = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(page,'html.parser')
    video = pafy.new(url)
    
    
    title = video.title
    views = video.viewcount
    thumbnail = video.thumb
 
    # title = soup.select('span.watch-title')[0]['title'] 
    # views = soup.find("div", attrs={"class": "watch-view-count"}).text[:-7].replace(",", "")
    # thumbnail = 'https://img.youtube.com/vi/'+url.split('=')[1].split('"')[0]+'/0.jpg'
 
    
    raw_keywords = page.split('<script >')[-5].split('keywords')[1].split('[')[1].split(']')[0].split(',')
    for keyword in raw_keywords:
      keyword = keyword[2:-2]
      keyword_storage.append(keyword)
  except:
    title=""
    views=""
    thumbnail=""
    keyword_storage= []
    return(title,views,thumbnail,list(keyword_storage))
  
  return(title,views,thumbnail,list(keyword_storage))

