from django.shortcuts import render
from pytube import YouTube
import os
from django.http import HttpResponse,FileResponse


def ytdwn(request,link):
    try:
        video = YouTube('https://www.youtube.com/watch?v=%s' % link)
        stream = video.streams.get_highest_resolution()
        file = str(link)
        '''
        ft=open('/home/epgccp/epgccp/ytdown/tmpfile','r')
        tmp2=ft.read()
        ft.close()
        if os.path.isfile('/home/epgccp/epgccp/ytdown/media/' + tmp2 ):
                os.remove('/home/epgccp/epgccp/ytdown/media/' + tmp2)
        ft=open('/home/epgccp/epgccp/ytdown/tmpfile','w')
        ft.write(file)
        ft.close()
        '''
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
        linkstr = arr2[0];

        video = YouTube('https://www.youtube.com/watch?v=%s' % linkstr)
        stream = video.streams.get_highest_resolution()
        file = str(linkstr)
        ft=open('/home/epgccp/epgccp/ytdown/tmpfile','r')
        tmp2=ft.read()
        ft.close()
        if os.path.isfile('/home/epgccp/epgccp/ytdown/media/' + tmp2 ):
                os.remove('/home/epgccp/epgccp/ytdown/media/' + tmp2)
        ft=open('/home/epgccp/epgccp/ytdown/tmpfile','w')
        ft.write(file)
        ft.close()
        stream.download(output_path='/home/epgccp/epgccp/ytdown/media',filename=file)
        return FileResponse(open('/home/epgccp/epgccp/ytdown/media/' + file , 'rb'))
    except:
        return HttpResponse ('Youtube Url Is Mistake!!')

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