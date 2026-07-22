import threading
import requests
import time
import asyncio
import aiohttp

def get_data_sync(urls):
    st = time.time()

    jsonArray = []
    for url in urls:
        jsonArray.append(requests.get(url).json())

    et = time.time()
    elapsedTime = et-st
    print(f"Execution time: {elapsedTime} seconds")

    return jsonArray

class ThreadingDownloader(threading.Thread):

    jsonArray = []

    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.jsonArray.append(response.json())
        return response.json()

def get_data_threadding(urls):
    st = time.time()

    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)


    for t in threads:
        t.join()
        #print(t) #this line shows threads


    et = time.time()
    elapsedTime = et - st
    print(f"Execution time: {elapsedTime} seconds")


async def getDataAsync_butAsWrapper(urls):
    st = time.time()
    jsonArray = []

    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as resp:
                jsonArray.append(await resp.json())

    et = time.time()
    elapsedTime = et-st
    print(f"Execution time: {elapsedTime} seconds")
    return jsonArray


async def get_data(session, url, jsonArray):
    async with session.get(url) as resp:
        jsonArray.append(await resp.json())



async def get_data_async_concurrently(urls):
    st = time.time()
    json_array = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session,url,json_array)))
        await asyncio.gather(*tasks)

    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, " seconds")
    return json_array

urls = ["https://postman-echo.com/delay/3"] * 10
#get_data_sync(urls) #38.80 secs
#get_data_threadding(urls) #5 secs
#asyncio.run(getDataAsync_butAsWrapper(urls)) #32 secs
asyncio.run(get_data_async_concurrently(urls)) #3.41 secs