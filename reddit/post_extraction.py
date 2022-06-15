import requests
import json 
 
subreddit = 'france'
count = 10
timeframe = 'day' #hour, day, week, month, year, all
listing = 'top' # controversial, best, hot, new, random, rising, top
 
def get_reddit(subreddit,count):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()
 
post = get_reddit(subreddit,count)

print(f"Top {count} {timeframe} sur r/{subreddit}:")

for i in range(count):
   
    if listing != 'random':
        title = post['data']['children'][i]['data']['title']
        url = post['data']['children'][i]['data']['url']
    else:
        title = post[i]['data']['children'][i]['data']['title']
        url = post[i]['data']['children'][i]['data']['url']

    print(i+1, "-", f'\x1b]8;;{url}\x1b\\{title}\x1b]8;;\x1b\\') # hyperlink
