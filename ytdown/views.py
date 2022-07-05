from django.shortcuts import render
from pytube import YouTube
import os,subprocess
from django.http import HttpResponse,FileResponse
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import WebVTTFormatter
#pip install googletrans==4.0.0-rc1
from googletrans import Translator
import re


def ytdwn(request,link):
    try:
        video = YouTube('https://www.youtube.com/watch?v=%s' % link)
        stream = video.streams.get_highest_resolution()
        file = str(link)
        stream.download(output_path='/home/epgccp/epgccp/ytdown/media',filename=file)
        tmp4=open('/home/epgccp/epgccp/ytdown/media/' + file , 'rb')
        tmp5=tmp4.read()
        tmp4.close()
        fn=stream.default_filename
        fn=re.sub(r"\s+", '_', fn)
        response=HttpResponse(tmp5, content_type='video/mp4')
        response['Content-Length'] = os.path.getsize('/home/epgccp/epgccp/ytdown/media/' + file)
        response['Content-Disposition'] = 'filename=%s' % fn
        os.remove('/home/epgccp/epgccp/ytdown/media/' + file)
        return response
    except:
        return HttpResponse ('Youtube Url Is Mistake!')

def ytsub(request,link):
    #try:
        video = YouTube('https://www.youtube.com/watch?v=%s' % link)
        stream = video.streams.get_highest_resolution()
        file = str(link)
        stream.download(output_path='/home/epgccp/epgccp/ytdown/media',filename='a.mp4')

        srt=YouTubeTranscriptApi.get_transcript(link)
        #transcripts = YouTubeTranscriptApi.list_transcripts(link)
        #transcript = transcripts.find_transcript(['en'])
        #srt=transcript.translate('en').fetch()
        fmt=WebVTTFormatter()
        vtt=fmt.format_transcript(srt)

        f=open('/home/epgccp/epgccp/ytdown/media/sub.vtt', 'w', encoding='utf-8')
        f.write(vtt)
        f.close()

        f=open('/home/epgccp/epgccp/ytdown/media/sub.vtt', 'r', encoding='utf-8')
        en_sub=f.read()
        f.close()

        translator = Translator()
        fa_sub = translator.translate(en_sub, dest='fa').text
        f=open('/home/epgccp/epgccp/ytdown/media/sub1.vtt', 'w', encoding='utf-8')
        f.write(fa_sub)
        f.close()

        subprocess.run(['ffmpeg','-i', os.path.join('/home/epgccp/epgccp/ytdown/media/a.mp4' ),'-vf','subtitles=/home/epgccp/epgccp/ytdown/media/sub.vtt',os.path.join('/home/epgccp/epgccp/ytdown/media/out.mp4')])

        tmp4=open('/home/epgccp/epgccp/ytdown/media/out.mp4' , 'rb')
        tmp5=tmp4.read()
        tmp4.close()
        fn=stream.default_filename
        fn=re.sub(r"\s+", '_', fn)
        response=HttpResponse(tmp5, content_type='video/mp4')
        response['Content-Length'] = os.path.getsize('/home/epgccp/epgccp/ytdown/media/out.mp4')
        response['Content-Disposition'] = 'filename=%s' % fn
        os.remove('/home/epgccp/epgccp/ytdown/media/a.mp4')
        os.remove('/home/epgccp/epgccp/ytdown/media/sub.vtt')
        os.remove('/home/epgccp/epgccp/ytdown/media/sub1.vtt')
        os.remove('/home/epgccp/epgccp/ytdown/media/out.mp4')
        return response
    #except:
        #return HttpResponse ('Youtube Url Is Mistake!')

def ytlink(request):
    try:
        link=''
        if request.method == 'GET' and 'url' in request.GET:
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
        fn=stream.default_filename
        fn=re.sub(r"\s+", '_', fn)
        response=HttpResponse(tmp5, content_type='video/mp4')
        response['Content-Length'] = os.path.getsize('/home/epgccp/epgccp/ytdown/media/' + file)
        response['Content-Disposition'] = 'attachment; filename=%s' % fn
        os.remove('/home/epgccp/epgccp/ytdown/media/' + file)
        return response
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
        fn=stream.title + '.mp3'
        fn=re.sub(r"\s+", '_', fn)
        response = HttpResponse(tmp5 , content_type='audio/mp3' )
        response['Content-Length'] = os.path.getsize('/home/epgccp/epgccp/ytdown/media/m1.mp3')
        response['Content-Disposition'] = 'attachment; filename=%s' % fn
        os.remove('/home/epgccp/epgccp/ytdown/media/' + file)
        os.remove('/home/epgccp/epgccp/ytdown/media/m1.mp3')
        return response
    except:
        return HttpResponse (video.description)


def helping(request):
    try:
        return HttpResponse ('''
        <p>Use address of youtube after watch like - for download video -  :<br>
        <b> epgccp.pythonanywhere.com/ytlink?url=https://www.youtube.com/watch?v=xazlZh1lTpM</b><br>
        or<br>
        link name like - for play in firefox -  : <br>
        <b>epgccp.pythonanywhere.com/xazlZh1lTpM</b><br>
        and<br>
        for download Mp3 Audio : <br>
        <b>epgccp.pythonanywhere.com/mp3/xazlZh1lTpM</b><br>
        <br>
        <a href="/static/epg_youtube4.xpi">YouTube Firefox Addon</a></br>
        </p>
        ''')
    except:
        return HttpResponse ('Youtube Url Is Mistake!!!')