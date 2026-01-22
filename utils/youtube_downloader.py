def download_video(url):
    try:
        from pytube import YouTube
    except ImportError:
        print("pytube kurulu değil. Kurulum: pip install pytube")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Video indirildi.")
    except Exception as e:
        print("Video indirilemedi (pytube bazen YouTube değişince hata verebilir).")
        print("Hata:", e)