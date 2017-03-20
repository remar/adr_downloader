import http.client, urllib.request, re, time, os, json

POSTS_JSON_FILE = "data/posts.json"

def get_posts():
    base = get_base()
    #page = urllib.request.urlopen("http://" + base)
    page = urllib.request.urlopen("file:///home/andreas/Projekt/adr_data/index.html")

    data = page.read()
    matches = re.findall(b"<a class='post-count-link'.*?>", data)
    matches = filter(lambda x: b"archive" in x, matches)
    archives = []
    for m in matches:
        s = m.decode('utf-8')
        match = re.search("href='(.*?)'", s)
        archives.append(match.group(1))

    posts = get_stored_list()

    for a in archives:
        if a not in posts:
            print("Getting archive " + a)
            url = "http://" + base + "/?action=getTitles&widgetId=BlogArchive1&widgetType=BlogArchive&responseType=js&path=" + a;
            arch = urllib.request.urlopen(url)
            res = arch.read().decode('utf-8')
            matches = re.findall("http://.*?\.html", res)
            matches = list(filter(lambda x: "archive" not in x, matches))
            print("\n".join(matches))
            posts[a] = matches
            time.sleep(3) # Don't hammer the server too hard

    store_list(posts)

    posts_list = []

    for key, value in posts.items():
        posts_list.extend(value)

    return sorted(posts_list)

def get_base():
    base = "thearchdruidreport.blogspot.com"
    conn = http.client.HTTPConnection(base)
    conn.request("HEAD", "/")
    r = conn.getresponse()

    if r.status == 302:
        conn.close()
        conn = http.client.HTTPConnection(base)
        conn.request("GET", "/")
        r = conn.getresponse()
        body = r.read().decode('utf-8')
        matches = re.findall("\"http://(.*?)/\"", body)
        if(len(matches) == 1):
            base = matches[0]

    conn.close()

    print("Base: " + base)

    return base

def get_stored_list():
    posts = {}
    if os.path.exists(POSTS_JSON_FILE):
        f = open(POSTS_JSON_FILE)
        posts = json.load(f)
        f.close()
    return posts

def store_list(posts):
    f = open(POSTS_JSON_FILE, "w")
    json.dump(posts, f)
    f.close()

if __name__ == "__main__":
    print(get_posts())
