import urllib.request, time

def get_post(url):
    print("Getting " + url)
    while True:
        try:
            page = urllib.request.urlopen(url)
            break
        except:
            print("Failed to get post " + url + ", retrying in 5 seconds")
            time.sleep(5)
    data = page.read()
    return data.decode('utf-8')

def get_path(post):
    return "/".join(post.split("/")[-3:])
