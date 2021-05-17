
## Chapter 13


import twurl
import urllib
import json
import ssl
print("Hello welcome to Ex 14\n")


# TWITTER_URL1 = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
url1 = False
## friends url
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
url2 = False

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

## read twitter data
while True:
    acct = input('Enter twitter account: ')
    if (len(acct) < 1):
        break

    url = twurl.augment(TWITTER_URL,
            {'screen_name': acct, 'count': '10'})

    print("Retrieving", url)
    conn = urllib.request.urlopen(url, context = ctx)
    data = conn.read().decode()
    #print(data[:200])

    ## load json
    js = json.loads(data) ## returns list of dicts
    #print(json.dumps(js, indent = 6))

    ## This line works if we are using url1
    if url1 == True:
        lst = js[0] #pick first dict from the list
        u = lst['user']['screen_name']
        print("==== Username ====: ", u)

    else:
        for u in js['users']:
            ## for every user, pick the screen_name
            friend = u['screen_name']
            print(friend)

    ##get headers
    headers = dict(conn.getheaders())
    print("==== Remaining ====: ", headers['x-rate-limit-remaining'])
