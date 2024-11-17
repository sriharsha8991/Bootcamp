from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
import csv

def extract_video_id(youtube_url):
    """
    Extract the video ID from a YouTube URL.
    """
    url_data = urlparse(youtube_url)
    query = parse_qs(url_data.query)
    video_id = query["v"][0] if "v" in query else url_data.path.split('/')[-1]
    return video_id

def get_transcript(youtube_url, language='en'):
    """
    Extract and return the transcript of a YouTube video given its URL.
    """
    video_id = extract_video_id(youtube_url)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        return transcript
    except Exception as e:
        return str(e)

def save_transcript_to_csv(transcript, filename="transcript.csv"):
    """
    Save the transcript to a CSV file in the current directory.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Text", "Start Time", "Duration"])

        for entry in transcript:
            writer.writerow([entry['text'], entry['start'], entry['duration']])

    print(f"Transcript saved to {filename}")

if __name__ == "__main__":
    # Replace with your YouTube video URL
    youtube_url = 'https://www.youtube.com/watch?v=yBDHkveJUf4'
    
    transcript = get_transcript(youtube_url)
    if isinstance(transcript, str):
        print("Error:", transcript)
    else:
        save_transcript_to_csv(transcript, filename="youtube_transcript.csv")