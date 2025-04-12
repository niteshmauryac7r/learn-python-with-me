import multiprocessing
import requests
import concurrent.futures


url = "https://picsum.photos/200/300"
pros = []

def function1(url,name):
    print(f"Started Downloading {name}")
    r = requests.get(url, allow_redirects=True)
    open(f'image_testingfiles/{name}.jpg', 'wb').write(r.content)
    print(f"Finished Download {name}")

if __name__ == "__main__":
    # for i in range(500):
    #     #function1(url,i)
    #     p = multiprocessing.Process(target=function1,args=[url,i])
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #     p.join()
    url = [url for _ in range(60)]
    l = [i for i in range(60)]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(function1,url,l)
        for result in results:
            print(result)