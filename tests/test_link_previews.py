"""Tests for link_previews — URL extraction and preview-friendly transforms."""

from __future__ import annotations

import pytest

from link_previews import get_http_urls_in_text, get_preview_friendly_url


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("no link", []),
        (
            "https://bsky.app/profile/u/post/p1",
            ["https://bsky.app/profile/u/post/p1"],
        ),
        (
            "see https://x.com/u/status/1 and https://www.furaffinity.net/view/1",
            ["https://x.com/u/status/1", "https://www.furaffinity.net/view/1"],
        ),
    ],
)
def test_get_http_urls_in_text(text: str, expected: list[str]) -> None:
    assert get_http_urls_in_text(text) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        # Bluesky — host with and without www.
        (
            "https://bsky.app/profile/u/post/p1",
            "https://fxbsky.app/profile/u/post/p1",
        ),
        (
            "https://www.bsky.app/profile/u/post/p1",
            "https://fxbsky.app/profile/u/post/p1",
        ),
        # X — host with and without www.
        (
            "https://x.com/u/status/1",
            "https://fixupx.com/u/status/1",
        ),
        (
            "https://www.x.com/u/status/1",
            "https://fixupx.com/u/status/1",
        ),
        # FurAffinity — host with and without www.
        (
            "https://furaffinity.net/view/1",
            "https://fxraffinity.net/view/1",
        ),
        (
            "https://www.furaffinity.net/view/1/",
            "https://fxraffinity.net/view/1/",
        ),
    ],
)
def test_get_preview_friendly_url_recognized(raw: str, expected: str) -> None:
    assert get_preview_friendly_url(raw) == expected


@pytest.mark.parametrize(
    "raw",
    [
        "https://example.com/foo",
        "https://twitter.com/user/status/1",
        "not a url",
    ],
)
def test_get_preview_friendly_url_unrecognized(raw: str) -> None:
    assert get_preview_friendly_url(raw) is None


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (
            "https://bsky.app/profile/u/post/pid?utm_source=x&ref=y#section",
            "https://fxbsky.app/profile/u/post/pid",
        ),
        (
            "https://x.com/u/status/1?foo=bar#section",
            "https://fixupx.com/u/status/1",
        ),
        (
            "https://www.furaffinity.net/view/99/?x=1#section",
            "https://fxraffinity.net/view/99/",
        ),
    ],
)
def test_get_preview_friendly_url_strips_query_and_fragment(
    raw: str, expected: str
) -> None:
    assert get_preview_friendly_url(raw) == expected
