from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    """Return True if the URL has a valid scheme and netloc."""
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])
