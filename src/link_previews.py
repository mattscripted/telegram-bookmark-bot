"""Parse http(s) URLs from chat text and map them to preview-friendly canonical URLs.

Preview links only replace the hostname (see ``_HOST_PREVIEW``). Incoming hosts may include
``www.``; preview hosts never do.
"""

from __future__ import annotations

import re
from typing import Final
from urllib.parse import urlparse, urlunparse

# Loose scan for URLs in a message (order preserved; use len(urls) for none / many).
_HTTP_URL_IN_TEXT: Final = re.compile(r"https?://[^\s]+", re.IGNORECASE)

# Source host key (lowercase, no ``www.``) -> preview host (never includes ``www.``).
_HOST_PREVIEW: Final[dict[str, str]] = {
    "bsky.app": "fxbsky.app",
    "x.com": "fixupx.com",
    "furaffinity.net": "fxraffinity.net",
}


def get_http_urls_in_text(text: str) -> list[str]:
    """Return each ``http://`` / ``https://`` span in ``text``, in order."""
    return _HTTP_URL_IN_TEXT.findall(text or "")


def _get_host_key(hostname: str | None) -> str:
    """Lowercase hostname with optional leading ``www.`` removed, for rule lookup."""
    if not hostname:
        return ""
    host = hostname.lower()
    if host.startswith("www."):
        return host[4:]
    return host


def get_preview_friendly_url(url: str) -> str | None:
    """Return an ``https`` URL with the preview hostname, or ``None`` if the host is unknown.

    Strips query, fragment, and ``;params``; path is unchanged.
    """
    parsed = urlparse(url)
    key = _get_host_key(parsed.hostname)
    preview_host = _HOST_PREVIEW.get(key)

    if preview_host is None:
        return None
        
    rebuilt = parsed._replace(
        scheme="https",
        netloc=preview_host,
        params="",
        query="",
        fragment="",
    )
    return urlunparse(rebuilt)
