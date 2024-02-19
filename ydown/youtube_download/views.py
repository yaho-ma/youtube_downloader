from django.shortcuts import render
from pytube import YouTube

def ytb_down(request):
    return render(request, 'ytb_main.html')


def yt_download(request):
    print('yt_download view is called') #перевірка виклику

    url = request.GET.get('url')
    print('url: ', url)
    return render(request, 'yt_download.html')