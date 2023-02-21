import requests
from bs4 import BeautifulSoup
import pprint

# https://beautiful-soup-4.readthedocs.io/en/latest/

# select elements or css selectors -> span class (dot . ) or id (pound #)
# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')

# print out various pieces of information
# print(soup.body)
# print(soup.body.contents)
# print(soup.title)

# find all methods search for specific tags and return, like links
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# or first item only
# print(soup.find('a'))

# return first object without find
# print(soup.a)

# print(soup.find(id="score_24273602"))
# print(soup.select("#score_24273602"))   # outputs in a list
# select grabs the data using a CSS selector, where '.' means 'class', '#' means 'id', etc.

# print(soup.select('a')[0])    
# grabs all the 'a' tags, and print only the first one, as this is a list, and we want the 0th item

# print(soup.select(".score")[0])# grabs all the class="score" tags
# for our purposes, we want the a tag, title, but also score/points (id attribute)
# grab link and title with score 150+
links = soup.select('.titleline')
subtext = soup.select('.subtext')
# votes = soup.select('.score')
# print(links[0])
# print(votes[0])

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

pprint.pprint(create_custom_hn(links, subtext))
# create_custom_hn(links, subtext)