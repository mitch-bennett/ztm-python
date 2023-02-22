import requests
from bs4 import BeautifulSoup
import pprint

# https://beautiful-soup-4.readthedocs.io/en/latest/

# select elements or css selectors -> span class (dot . ) or id (pound #)
# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors

res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

all_links = links + links2
all_subtext = subtext + subtext2

print(len(links))
print(len(all_links))
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(all_links, all_subtext))
pprint.pprint(create_custom_hn(links, subtext))
# create_custom_hn(links, subtext)