"""
YouTube Transcript Collector
-----------------------------
Usage:
  1. Install: pip install youtube-transcript-api
  2. Run:     python get_transcripts.py

Output: saves .md files to /research/youtube-transcripts/
"""

from youtube_transcript_api import YouTubeTranscriptApi
import os
import re

OUTPUT_DIR = "research/youtube-transcripts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Add your video targets here
# Format: ("Author Name", "Video Title", "VIDEO_ID")
VIDEOS = [
    ("Aleyda Solis",    "How to Use AI for SEO Without Killing Your Rankings",   "REPLACE_WITH_ID"),
    ("Lily Ray",        "E-E-A-T and AI Content: What the Data Shows",            "REPLACE_WITH_ID"),
    ("Kevin Indig",     "AI Content Strategy for SaaS Companies",                 "REPLACE_WITH_ID"),
    ("Kyle Roof",       "AI On-Page SEO Experiment Results",                      "REPLACE_WITH_ID"),
    ("Wil Reynolds",    "How We Use AI in Our SEO Agency Workflow",               "REPLACE_WITH_ID"),
    ("Cyrus Shepard",   "Internal Linking Strategy with AI Tools",                "REPLACE_WITH_ID"),
    ("Brendan Hufford", "AI SEO Playbook for SaaS",                              "REPLACE_WITH_ID"),
    ("Gaetano DiNardi", "B2B Content Strategy with AI",                          "REPLACE_WITH_ID"),
]


def slugify(text):
    """Convert text to a safe filename."""
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def get_transcript(video_id):
    """Fetch transcript text from YouTube video ID."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        return f"[ERROR: Could not fetch transcript — {e}]"


def save_transcript(author, title, video_id, text):
    """Save transcript as a markdown file."""
    filename = f"{slugify(author)}-{slugify(title)}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    content = f"""# {title}

**Author:** {author}
**Video ID:** {video_id}
**YouTube URL:** https://www.youtube.com/watch?v={video_id}

---

## Transcript

{text}

---

*Collected on: [Date]*
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Saved: {filepath}")


def main():
    print(f"Collecting {len(VIDEOS)} transcripts...\n")
    for author, title, video_id in VIDEOS:
        if video_id == "REPLACE_WITH_ID":
            print(f"⚠️  Skipping '{title}' — no video ID set yet")
            continue
        print(f"Fetching: {title} ({author})")
        text = get_transcript(video_id)
        save_transcript(author, title, video_id, text)

    print("\nDone! Check /research/youtube-transcripts/")


if __name__ == "__main__":
    main()
