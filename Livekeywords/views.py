from django.shortcuts import render
from .main_keyword_fetcher import main_keyword_fetcher
from .youtube_video_tags import youtube_video_fetcher
# Create your views here.

def keyword_fetcher(request): 
  try:
    if request.method == 'POST':
      query = request.POST['query']
      language = request.POST['language']
      google = 'google' in request.POST
      youtube = 'youtube' in request.POST
      bing = 'bing' in request.POST
      yahoo = 'yahoo' in request.POST
      wikipedia = 'wikipedia' in request.POST
      print(google,youtube,bing,yahoo)
      print(language)
      if (google==youtube==bing==yahoo==wikipedia==False):
        google=yahoo=youtube=bing=wikipedia=True
      if language=='': language='en'
      all_keywords = main_keyword_fetcher(query,google,youtube,bing,yahoo,wikipedia,language)
      # print(all_keywords)
      google_data = all_keywords[0]
      youtube_data = all_keywords[1]
      bing_data = all_keywords[2]
      yahoo_data = all_keywords[3]
      wikipedia_data = all_keywords[4]
      all_data = list(set(google_data).union(set(youtube_data),set(bing_data),set(yahoo_data),set(wikipedia_data)))
      # mean_time = all_keywords[4]
      x =language
      context = {
        "title" : "Live Keywords",
        "query" : query,
        'language': language ,
        "google_data":google_data,
        "youtube_data":youtube_data,
        "bing_data":bing_data,
        "yahoo_data":yahoo_data,
        "wikipedia_data":wikipedia_data,
        "all_data":all_data,
        
        "google_check":google,
        "youtube_check":youtube,
        "bing_check":bing,
        "yahoo_check":yahoo,
        "wikipedia_check":wikipedia,
        
        # "mean_time":mean_time,
        'total_results':len(list(google_data))+len(list(youtube_data))+len(list(wikipedia_data))+len(list(bing_data))+len(list(yahoo_data))
      }
      return render(request, 'keyword_fetcher.html',context)
  except:
    pass
  return render(request, 'keyword_fetcher.html' ,{"title" : "Live Keywords",})


def youtube_video_tags(request):
  def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
  if request.method == 'POST':
    link = request.POST['link']
    print(link)
    # https://www.youtube.com/watch?v=huUBFHIe6fE
    message = ''
    if link == "https://www.youtube.com/watch?v=" or link[:32] != "https://www.youtube.com/watch?v=":
      message = "Not a Valid Link" 
    else:
      message='' 
      
    video_data = youtube_video_fetcher(link)
    title = video_data[0]
    views = video_data[1]
    thumbnail = video_data[2]
    keywords = video_data[3]
    print(video_data)
    context = {
      'title': 'Youtube Video Tags',
      'link': link,
      'message': message,
      'title':title,
      'views':views,
      'thumbnail':thumbnail,
      'keywords':keywords,
      'data': 1
    }
    return render(request, 'youtube_video_tags.html', context)
    def visitor_ip_address(request):
      x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
      if x_forwarded_for:
          ip = x_forwarded_for.split(',')[0]
      else:
          ip = request.META.get('REMOTE_ADDR')
      return ip
  # ip = visitor_ip_address()
  context = {"data": visitor_ip_address(request=request)}
  return render(request, 'youtube_video_tags.html',context)
