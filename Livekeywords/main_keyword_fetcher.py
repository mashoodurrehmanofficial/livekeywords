import urllib.request,re,requests,json
import time

# query = "python"

# < =========================================== http://clients1.google.com/ and suggestqueries ===>> LANGUAGE 'hl':'xx' CHANGES THE RESULT ====================================== >
# print('=================================== seek "Languages Codes"  for help ==============================================')
 
 
def main_keyword_fetcher(query,google,youtube,bing,yahoo,wikipedia,language):
  try:
    
        # t1 = int(round(time.time() * 1000))
    # print('========================================= GOOGLE ========================================')
    if google:
      google_url1 = 'http://suggestqueries.google.com/complete/search?q=ob&client=toolbar&q='+query+" "
      params = {'client':'firefox', 'q':query.replace(' ','+'),'hl': language,"ds":"yt"}
      google1x = requests.get(google_url1,params=params).json()[1:][0]
      google1 = [x.replace('+',' ') for x in google1x] 
      google_url2 = "http://suggestqueries.google.com/complete/search?hl="+language+"&client=firefox&q="+query+" "
      google2 = requests.get(google_url2).json()[1] 
      GOOGLE = list(set(google1).union(set(google2)))  
    else:GOOGLE=[]
    
    # print('============================================== YOUTUBE ===================================')
    if youtube:  
      youtube_url1 = "https://suggestqueries.google.com/complete/search?hl="+language+"&ds=yt&client=youtube&hjson=t&cp=1&q="+query+" " 
      youtube1x = requests.get(youtube_url1).json()[1]
      YOUTUBE = [x[0] for x in youtube1x]   
    else:YOUTUBE=[]
    # print('============================================ BING ===========================================')
    if bing:
      bing_url = "https://api.bing.com/osjson.aspx?query="+query+" "
      BING = requests.get(bing_url).json()[1] 
    else:BING=[]
    # print('============================================ YAHOO =====================================')
    if yahoo:  
      yahoo_url = "http://sugg.search.yahoo.net/sg/?output=json&nresults=18&command="+query+" "
      yahoo1 = requests.get(yahoo_url).json()
      YAHOO = [ x['key'] for x in yahoo1['gossip']['results']] 
    else:YAHOO=[]
    
    
    # print('============================================ YAHOO =====================================')
    if wikipedia:
      wikipedia_url = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=15&format=json&callback=portalOpensearchCallback&search="+query.replace(' ','%20')+" "
      wikipedia1 = requests.get(wikipedia_url).content.decode('utf-8')
      wikipedia_split = wikipedia1.split('"],["",""')[0].split(',[')[1:]
      WIKIPEDIA = [x.replace('"','') for x in wikipedia_split][0].split(',') 
      if WIKIPEDIA == [']']: WIKIPEDIA = []
    else:WIKIPEDIA=[]  

    # t2 = int(round(time.time() * 1000))
    # mean_time = (t2-t1)/1000
    return GOOGLE,YOUTUBE,BING,YAHOO,WIKIPEDIA
  except:pass
 
 
 
# print(main_keyword_fetcher(query))