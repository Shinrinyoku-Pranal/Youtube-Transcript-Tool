import yt_dlp
import whisper

def download_audio(url, output="audio.mp3"):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output


def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    audio_file = download_audio(url)
    text = transcribe_audio(audio_file)
    print("\n--- TRANSCRIPT ---\n")
    print(text)

