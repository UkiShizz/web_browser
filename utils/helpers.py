from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    """Ensure the URL has a scheme; default to http if missing."""
    parsed = urlparse(url)
    if not parsed.scheme:
        return "http://" + url
    return url
