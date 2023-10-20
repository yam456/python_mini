import pyshorteners

url=input("Enter the url: ")

def shortener(url):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(url))
shortener(url)
