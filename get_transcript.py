from youtube_transcript_api import YouTubeTranscriptApi
import sys

video_id = sys.argv[1]
filename = sys.argv[2]

ytt = YouTubeTranscriptApi()
transcript = ytt.fetch(video_id)
full_text = " ".join([t.text for t in transcript])

with open(filename, 'w', encoding='utf-8') as f:
    f.write(full_text)

print(f"Saved to {filename}")