import argparse
import requests

def Download_file(url,localname=None):
    if localname is None:
        localname = url.rsplit("/",1)[1]
    r = requests.get(url, allow_redirects=True)
    open(localname, 'wb').write(r.content)

parser = argparse.ArgumentParser()

parser.add_argument('url',help="url of file to be downloaded")
parser.add_argument("-o",help="File name")

args = parser.parse_args()
print(args.url)
print(args.o) 

Download_file(args.url,args.o)

