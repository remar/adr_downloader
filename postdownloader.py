import urllib.request

def get_post(url):
    print("Getting " + url)
    page = urllib.request.urlopen(url)
    data = page.read()
    return data.decode('utf-8')

def get_path(post):
    return "/".join(post.split("/")[-3:])
