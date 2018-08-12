import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best', 'outtmpl': '/MP3/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=SKhipQqpjOg'])