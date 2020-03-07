
import selectors
import sys
import asyncio
import aiohttp
import json

async def main():
    async with aiohttp.ClientSession() as client:
        await asyncio.gather(get_reddit_top('python', client),
                             get_reddit_top('programming', client),
                             get_reddit_top('compsci', client))

async def get_json(client, url):  
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()

async def get_reddit_top(subreddit, client):  
    data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        
        print(f"{score}: {title} ({link})")

    print('DONE:', subreddit + '\n')

#Since I am using python 3.8, which changed the EventLoop for asyncio
#and aiohttp does not support it just yet (https://github.com/aio-libs/aiohttp/issues/4324)
#I am changing the Event Loop type.
#for python 3.7 or when aiohttp gets updated, 
#asyncio.run(main()) is the only line you need.
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
