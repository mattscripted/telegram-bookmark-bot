"""Telegram command and message handlers."""

from __future__ import annotations

from telegram import Update
from telegram.ext import ContextTypes

from link_previews import get_http_urls_in_text, get_preview_friendly_url


async def start(update: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Hi. Send one link at a time and I will reply with a preview-friendly version "
            "(Bluesky, X, or FurAffinity) without extra query parameters."
        )


async def on_text_message(update: Update, _context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or update.message.text is None:
        return

    urls = get_http_urls_in_text(update.message.text)

    if len(urls) > 1:
        await update.message.reply_text(
            "Please send only one link at a time so Telegram can show a preview."
        )
        return

    if not urls:
        await update.message.reply_text(
            "Send a single link and I will reply with a preview-friendly version you can open."
        )
        return

    friendly = get_preview_friendly_url(urls[0])
    if friendly is None:
        await update.message.reply_text("That link is not recognized.")
    else:
        await update.message.reply_text(friendly)
