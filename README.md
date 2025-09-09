## YouTube Transcription Bot

A Python tool that downloads YouTube audio and transcribes it to text using OpenAI Whisper. Works with any video, even if captions are unavailable.

# How it Works

Replace the Never gonna give you up' youtube link with your link of the youtube video you want to transcribe.

Select the Whisper type (Default is base)

Downloads audio from YouTube videos using yt-dlp.

Convert audio to MP3 using ffmpeg.

Transcribe audio to text with Whisper (tiny, base, small, medium, large).

Transcript is printed in the terminal.

Works offline after setup (Whisper models are local).
