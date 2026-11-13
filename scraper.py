import trafilatura


def get_article(url: str) -> str | None:
    """Download a web page and return only the article text."""
    try:
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            return None
        return trafilatura.extract(downloaded)
    except Exception:
        return None
