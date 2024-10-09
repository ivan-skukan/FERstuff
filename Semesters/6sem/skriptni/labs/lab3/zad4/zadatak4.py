import urllib.request
import re
import collections
from urllib.parse import urlparse

def main():
    url = "http://www.fer.unizg.hr"
    response = urllib.request.urlopen(url)
    mybytes = response.read()
    mystr = mybytes.decode("utf8")
    print(mystr)
    links = re.findall(r'<a href=".*"', mystr)
    print(len(links)) #175
    for link in links:
        print(link)
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    # Make a list of all hosts without repetition
    links = re.findall(r'href="http[s]?://([^"]+)"', mystr)
    links = set(links)
    for link in links:
        print(link)
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    #count repetition of hosts
    links = re.findall(r'href="http[s]?://([^\/"]+)[/"]', mystr)
    c = collections.Counter(links)
    for link in c:
        print(f"{link}: {c[link]}")
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    #find emails
    emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', mystr)
    print(emails)
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    #find all img links
    img_links = re.findall(r'<img\s*src\s*=\s*[\'"]([^"\']*)[\'"]', mystr)
    print("broj linkova na slike:",len(img_links))
if __name__ == "__main__":
    main()