'''Project consist in scraping hacker news and eliminating all stories with less than 100 upvotes'''

import requests
from bs4 import BeautifulSoup
import pprint

r = requests.get("https://news.ycombinator.com/news")
r2 = requests.get
soup = BeautifulSoup(r.text, "html.parser")

# Picking elements we need: votes and links
subtext = soup.select(".subtext")
links = soup.select(".titlelink")


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({'title' : title, 'link' : href, "votes" : points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))
