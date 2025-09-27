import datetime, os
from src.config import FEEDS, KEYWORDS, DRY_RUN
from feeds import fetch_articles
from summarizer import summarize
from email_functionality import send_email

def run_once():
    print("Fetching articles...")
    print(f"FEEDS: {FEEDS}")
    articles = fetch_articles(FEEDS)
    filtered = [a for a in articles if any(k in a['title'].lower() for k in KEYWORDS)]
    
    if not filtered:
        print("No matching articles today.")
        return
    
    for article in filtered[:1]:  # limit to 1 posts daily
        prompt = f"Write a LinkedIn post summarizing this innovation/tech news in a not so professional & informative engaging tone.\n\nTitle: {article['title']}\nLink: {article['link']}\nSummary: {article['summary']}"
        draft = summarize(prompt)
        
        # timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # out_path = f"out/draft_{timestamp}.md"

        # os.makedirs("out", exist_ok=True)
        # with open(out_path, "w") as f:
        #     f.write(draft)
        
        # print(f"Draft saved: {out_path}")
        if not DRY_RUN:
            print("Calling Sent email function here...")
            subject = "Post of the Day | " + str(datetime.datetime.now().strftime("%-d_%b"))
            send_email(os.getenv("TO_AADRESS"),subject,draft)


if __name__ == "__main__":
    run_once()
