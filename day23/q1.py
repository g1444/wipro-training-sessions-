import requests
import threading 
import time

urls=["https://www.google.com",
      "https://www.yahoo.com",
      "https://www.rediff.com",
      "https://www.amazon.in"
      ]

def downloadfiles(url):
    try:
        response=requests.get(url)
        filename=url.split("/")[-1]+".txt"

        with open(filename,"w",encoding="utf-8") as f:
            f.write(response.text)
        print(f"Downloaded:{filename}")
    except Exception as e:
        print(f"error downloading: {e}")

starttime=time.time()
for url in urls:
    downloadfiles(url)

seqentialtime=time.time()-starttime
print(f"\n download time: {seqentialtime}")

threads=[]

startingtime=time.time()
for url in urls:
    thread=threading.Thread(target=downloadfiles,args=(url,))
    threads.append(thread)
    thread.start()

threadingtime=time.time()-startingtime
print(f"\n threading download time:{threadingtime}")