# telegram-bookmark-bot

## High-Level

### Problems
- I often save and share links from various websites (like BlueSky and Twitter) on Telegram
- I need to convert these links to a preview-friendly format, so their previews will work (e.g. bsky.app -> fxbsky.app)
- I often want to find older bookmarks, but I only remember a vague description, not when I saved it or what it was
- I often have an image, and want to find the original source

### Project Goals
At a high-level, I want to:
- Send a bookmark to the Telegram bot
- Get back a preview-friendly version
- Find previous bookmarks through a fuzzy search
- Find previous bookmarks through a reverse image search

## Development

### Tech Stack
- Python
  - Opportunity to learn Python
  - The project may shift towards AI/ML, so Python is friendlier
- [python-telegram-bot](https://docs.python-telegram-bot.org/)
