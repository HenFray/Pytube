from pytube import YouTube


print("[/[/[/[Script Start]\]\]\]")

URL_VIDEO = YouTube(input("URL: "))
print("Title: {}".format(URL_VIDEO.title))
exhibit_itag = URL_VIDEO.streams.filter(file_extension='mp4')

print(exhibit_itag)

'''
[<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">,
...
<Stream: itag="394" mime_type="video/mp4" res="None" fps="30fps" vcodec="av01.0.00M.08" progressive="False" type="video">,
<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">]
'''

RES = URL_VIDEO.streams.get_by_itag(input("itag(choice resolucion): "))

RES.download()

print("[/[/[/[End Script]\]\]\]")
