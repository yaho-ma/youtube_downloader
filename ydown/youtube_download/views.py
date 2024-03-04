from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from pytube import YouTube

from django.http import FileResponse
import tempfile
import os


def ytb_down(request):
    return render(request, 'ytb_main.html')


def download_chosen_resolution(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        resolution = request.POST.get('resolution')

        print("download_chosen_resolution: URL:", url)  # Debugging statement

        if url is None or resolution is None:
            return HttpResponseBadRequest("URL or resolution not provided.")




        try:
            youtube_obj = YouTube(url)
        except Exception as e:
            return HttpResponseBadRequest(f"Error: {e}")

        video = youtube_obj.streams.filter(res=resolution).first()
        if video:
            try:
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                video.download(output_path=temp_file.name)

                # Close the file to release resources before serving for download
                temp_file.close()

                with open(temp_file.name, 'rb') as f:
                    response = FileResponse(f)
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(video.title)}.mp4"'

                    # Delete the temporary file after serving
                    os.unlink(temp_file.name)
                    return response
            except Exception as e:
                return HttpResponse(f"Error downloading video: {e}")
        else:
            return HttpResponse("Video with the chosen resolution not found.")

    return HttpResponse("Failed to download the video.")


def yt_download(request):
    url_from_user = request.GET.get('url_from_user')
    print('yt_download function ULR_FROM_USER: ', url_from_user)

    youtube_obj = YouTube(url_from_user)
    resolutions = []
    strm_all = youtube_obj.streams.all()

    for i in strm_all:
        resolutions.append(i.resolution)
    resolutions = list(dict.fromkeys(resolutions))

    embed_link = url_from_user.replace("watch?v=", "embed/")
    embed_link = embed_link.split("&")[0]

    # print("embed link: ", embed_link)
    return render(request,
                  'yt_download.html',
                  {'resolutions': resolutions,  # this is a dictionary with key value pair
                   'embd': embed_link,
                   'url_from_user': url_from_user
                   })
