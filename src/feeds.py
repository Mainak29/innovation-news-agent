import feedparser

def fetch_articles(feeds):
    articles = []
    for feed in feeds:
        parsed = feedparser.parse(feed)
        for entry in parsed.entries:
            articles.append({
                "title": entry.get("title"),
                "link": entry.get("link"),
                "summary": entry.get("summary", ""),
            })
    print(f"feeds : {feeds}, articles : {articles}")
    return articles
