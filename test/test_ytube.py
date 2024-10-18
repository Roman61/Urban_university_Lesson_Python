import pytube

link = "https://www.youtube.com/watch?v=J0Aq44Pze-w"
yt = pytube.YouTube(link)
yt.streams.first().download()
print("Видео успешно загружено")
