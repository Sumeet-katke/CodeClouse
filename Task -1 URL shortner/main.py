import pyshorteners

url = input('Enter the URL: ')

def shortner(url):
    s = pyshorteners.Shortener()
    stringg = s.tinyurl.short(url)
    return stringg

print(f'\nShortened URL: {shortner(url)}')