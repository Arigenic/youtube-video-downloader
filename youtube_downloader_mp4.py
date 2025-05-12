import yt_dlp

# Replace these with your actual YouTube video URLs
video_urls = [
    "https://www.youtube.com/watch?v=YGZLvKAFeYI&ab_channel=Sota",
    "https://www.youtube.com/watch?v=HRywgxrbahA&ab_channel=KINGAMV%27s%E5%A4%A2"
]

# Download options
ydl_opts = {
    'format': 'bestvideo+bestaudio[ext=m4a]/best',
    'merge_output_format': 'mp4',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
    'outtmpl': '%(title)s.%(ext)s',
    'quiet': True
}

# Download process
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("Starting download...")
    ydl.download(video_urls)
    print("Download complete.")

