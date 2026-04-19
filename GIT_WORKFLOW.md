# Git Workflow — Commit Per Expert

Run these commands after adding each expert's content.

## Initial Setup (once)

```bash
git clone https://github.com/Trijuwadi/Readme.git
cd YOUR_REPO

# Copy all starter files into the repo
# Then:
git add README.md research/sources.md get_transcripts.py
git commit -m "Initial structure: README, sources, transcript script"
git push
```

---

## Per Expert Workflow

After you collect one expert's LinkedIn posts + YouTube transcript:

```bash
# Stage their files
git add research/linkedin-posts/aleyda-solis.md
git add research/youtube-transcripts/aleyda-solis-*.md

# Commit with a clear message
git commit -m "Add Aleyda Solis: 5 LinkedIn posts + 1 YouTube transcript"

# Push
git push
```

---

## Suggested Commit Order

| Commit | What to include |
|--------|----------------|
| 1 | `README.md`, `sources.md`, `get_transcripts.py` |
| 2 | Aleyda Solis posts + transcript |
| 3 | Lily Ray posts + transcript |
| 4 | Kevin Indig posts + transcript |
| 5 | Kyle Roof transcript |
| 6 | Wil Reynolds posts + transcript |
| 7 | Cyrus Shepard posts + transcript |
| 8 | Eli Schwartz posts + book notes |
| 9 | Brendan Hufford posts + transcript |
| 10 | Ryan Law posts + blog articles |
| 11 | Gaetano DiNardi posts + transcript |
| 12 | Final README update |

---

## Quick Commands

```bash
git status           # See what's changed
git add .            # Stage all changes
git log --oneline    # See commit history
```
