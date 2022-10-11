import pyshorteners
long_url = input("Enter the URl to shorten: ")
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)

print("The Shortnened URL is "+ short_url)