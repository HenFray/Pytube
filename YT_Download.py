from pytube import YouTube


print("[/[/[/[Script Start]\]\]\]")

URL_VIDEO = YouTube(input("URL: "))
print("Title: {}".format(URL_VIDEO.title))
exhibit_itag = URL_VIDEO.streams.filter(file_extension='mp4')

for tag in exhibit_itag:
    print(tag)

RES = URL_VIDEO.streams.get_by_itag(input("itag(choice resolucion): "))

print("Downloading...")
RES.download()
print("Done!")

print("[/[/[/[End Script]\]\]\]")
