"""Telegram echo bot — replies with the same text the user sends."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


def _token() -> str:
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        raise SystemExit(
            "TELEGRAM_BOT_TOKEN is not set. Copy .env.example to .env and add your bot token from @BotFather."
        )
    return token


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Hi. Send any text message and I will echo it back."
        )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.text is not None:
        await update.message.reply_text(update.message.text)


def main() -> None:
    app = Application.builder().token(_token()).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    # Don't process pending updates when the bot is restarted
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
