import requests
import json

# Make an API call, and store the response.

json.dump(submission_ids,outfile,indent=3)

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

ourfile = open('hn2.json', 'w')
json.dump(r.json(), ourfile, indent=4)


# Explore the structure of the data.


sub_list = []

for sub_id in submission_ids:
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(sub_id) + '.json'
    r = requests.get(url)
    '''print(f"id: {sub_id}\t\tstatus: {r.status_code}")'''

    response_dict = r.json()

    a_dict = {
        'title': response_dict['title'],
        'hn_link': 'https://news.ycombinator.com/item?id='(sub_id),
        'comments': response_dict['descendants'],
    }

    sub_list.append(a_dict)

print(sub_list)

#sub_list = sorted(sub_list,key=lambda x: x['comments'], reverse=True)
from operator import itemgetter
sub_list = sorted(sub_list, key=itemgetter('comments'), reverse=True)





for d in sub_list:
    print(f"Title: {d['title']}")
    print(f"Discussion link: {d['hn_link']}")
    print(f"No. of comments: {d['comments']}")

