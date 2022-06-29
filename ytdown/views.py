from django.shortcuts import render
from pytube import YouTube
import os,subprocess
from django.http import HttpResponse,FileResponse


def ytdwn(request,link):
    try:
        video = YouTube('https://www.youtube.com/watch?v=%s' % link)
        stream = video.streams.get_highest_resolution()
        file = str(link)
        stream.download(output_path='/home/epgccp/epgccp/ytdown/media',filename=file)
        tmp4=open('/home/epgccp/epgccp/ytdown/media/' + file , 'rb')
        tmp5=tmp4.read()
        tmp4.close()
        os.remove('/home/epgccp/epgccp/ytdown/media/' + file)
        return HttpResponse(tmp5 , content_type='video/mp4')
    except:
        return HttpResponse ('Youtube Url Is Mistake!')

def ytlink(request):
    try:
        txt = request.GET['url']
        arr = txt.split("watch%3Fv%3D");
        arr1 = arr[-1].split("watch?v=");
        arr2 = arr1[-1].split("&");
        link = arr2[0];

        video = YouTube('https://www.youtube.com/watch?v=%s' % link)
        stream = video.streams.get_highest_resolution()
        file = str(link)
        stream.download(output_path='/home/epgccp/epgccp/ytdown/media',filename=file)
        tmp4=open('/home/epgccp/epgccp/ytdown/media/' + file , 'rb')
        tmp5=tmp4.read()
        tmp4.close()
        os.remove('/home/epgccp/epgccp/ytdown/media/' + file)
        return HttpResponse(tmp5 , content_type='video/mp4')
    except:
        return HttpResponse ('Youtube Url Is Mistake!!')

def ytmp3(request,link):
    try:
        video = YouTube('https://www.youtube.com/watch?v=%s' % link)
        stream = video.streams.filter(only_audio=True).first()
        file = str(link)
        stream.download(output_path='/home/epgccp/epgccp/ytdown/media',filename=file)
        subprocess.run(['ffmpeg','-i', os.path.join('/home/epgccp/epgccp/ytdown/media/', file),os.path.join('/home/epgccp/epgccp/ytdown/media/m1.mp3' )])
        tmp4=open('/home/epgccp/epgccp/ytdown/media/m1.mp3' , 'rb')
        tmp5=tmp4.read()
        tmp4.close()
        os.remove('/home/epgccp/epgccp/ytdown/media/' + file)
        os.remove('/home/epgccp/epgccp/ytdown/media/m1.mp3')
        return HttpResponse(tmp5 , content_type='audio/mp3')
        return FileResponse(tmp4)
    except:
        return HttpResponse ('Youtube Url Is Mistake!!!!!')


def helping(request):
    try:
        return HttpResponse ('''
        <p>Use address of youtube after watch like <br>
        <b> epgccp.pythonanaywhere.com/watch?v=PXRZaDhBf4c</b><br>
        or<br>
        link name like <br>
        <b>epgccp.pythonanaywhere.com/PXRZaDhBf4c</b><br>
        <a href="/static/epg_youtube2.xpi">youtube firefox addon 1</a></br>
        <a href="/static/epg_youtube4.xpi">youtube firefox addon 2</a></br>
        </p>
        ''')
    except:
        return HttpResponse ('Youtube Url Is Mistake!!!')