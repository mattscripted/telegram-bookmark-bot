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
- [Poetry](https://python-poetry.org/) for dependencies and lockfile (`package-mode = false` application layout)
- [python-telegram-bot](https://docs.python-telegram-bot.org/)

### Prerequisites
- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation)

### Run the echo bot locally
1. Install dependencies: `poetry install`
2. Copy `.env.example` to `.env` and set `TELEGRAM_BOT_TOKEN` to the token from @BotFather (see below). Do not commit `.env` (it is gitignored).
3. From the repo root: `poetry run python src/main.py`
4. Open your bot in Telegram, send `/start`, then send any text; the bot should echo it back.

### Bot token (BotFather)
1. In Telegram, open **@BotFather**.
2. Send **`/newbot`**, choose a display name and a username ending in `bot`.
3. Copy the **HTTP API token** into `.env` as `TELEGRAM_BOT_TOKEN=...`.
4. If a token is ever exposed, revoke it in BotFather and create a new one.

### Project layout
- Application code lives under `src/` (e.g. `src/main.py`).
