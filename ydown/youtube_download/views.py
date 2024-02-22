from django.shortcuts import render
from pytube import YouTube


def ytb_down(request):
    return render(request, 'ytb_main.html')


def yt_download(request):
    print('yt_download view is called')  # перевірка виклику
    url = request.GET.get('url')
    print(request.GET)

    youtube_obj = YouTube(url)
    resolutions = []
    strm_all = youtube_obj.streams.all()

    for i in strm_all:
        resolutions.append(i.resolution)
    resolutions = list(dict.fromkeys(resolutions))

    print('resolutions:', resolutions)
    print('url: ', url)

    embed_link = url.replace("watch?v=", "embed/")
    embed_link = embed_link.split("&")[0]


    print("embed link: ", embed_link)
    return render(request,
                  'yt_download.html',
                  {'resolutions': resolutions, 'embd': embed_link})
