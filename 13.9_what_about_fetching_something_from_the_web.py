import urllib.request

url = "https://thinkmoult.com/why-revit-is-shit.html"
destination_filename = "revit_web.txt"

urllib.request.urlretrieve(url, destination_filename)