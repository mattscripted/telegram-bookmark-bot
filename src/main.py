"""Telegram bot entrypoint — wires handlers and polling."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from handlers import start, on_text_message

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


def _token() -> str:
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        raise SystemExit(
            "TELEGRAM_BOT_TOKEN is not set. Copy .env.example to .env and add your bot token from @BotFather."
        )
    return token


def main() -> None:
    app = Application.builder().token(_token()).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text_message))
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
