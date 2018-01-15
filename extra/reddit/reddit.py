# This script connect to reddit and search links, next he save in file. That's all.
# With me, success 475 links on articles and 195 unique domain.
# You see in file site_lists.txt
# Manual for get token: https://github.com/reddit/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

import praw
import re
import json

# connect to API reddit
CLIENT_ID = 'ID'
CLIENT_SECRET = 'SECRET'
USER_AGENT = 'my user agent'

# keywords
SUBREDDIT_NAME = 'worldnews'
KEY_WORD = 'bitcoin'
PARAMS = {'sort': 'new', 'limit': None}


reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
my_list = []
for submission in reddit.subreddit(SUBREDDIT_NAME).search(KEY_WORD, **PARAMS):
    my_list.append({'title': submission.title, 'url': submission.url})
for l in my_list:
    l['short_url'] = re.search('(https?://.*?)/', l['url']).group(1)
with open('site_lists.txt', 'w') as f:
    f.write(json.dumps(my_list))
