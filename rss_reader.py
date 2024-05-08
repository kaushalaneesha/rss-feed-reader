# https://www.nasa.gov/feeds/iotd-feed/
import feedparser

feed_url = input("Enter RSS feed URL: ")
feed = feedparser.parse(feed_url)
if feed.bozo:
    print("Invalid RSS URL")
else:
    for entry in feed.entries:
        print("Title: ", entry.title)
        print("Summary:  ", entry.description)
        print("Link: ", entry.link)
        print("Published: ", entry.published)
        print("")