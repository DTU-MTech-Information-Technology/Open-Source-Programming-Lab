import urllib
import urllib.request


def test_page(url):
    try:
        urllib.request.urlopen(url)
        return True
    except:
        return False


print("Testing http://google.co.in -", test_page("http://google.co.in"))
print("Testing http://404.org -", test_page("http://404.org"))
