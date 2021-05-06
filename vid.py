from pytube import Youtube
link = input("https://youtu.be/g4ZuPZPBUMc")
video = Youtube(link)
stream = video.stream.get_highest_resolution()
stream.download()