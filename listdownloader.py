import http.client, urllib.request, re, time

def get_posts():
    base = get_base()
    #page = urllib.request.urlopen(base)
    page = urllib.request.urlopen("file:///home/andreas/Projekt/adr_downloader/index.html")

    data = page.read()
    matches = re.findall(b"<a class='post-count-link'.*?>", data)
    matches = filter(lambda x: b"archive" in x, matches)
    archives = []
    for m in matches:
        s = m.decode('utf-8')
        match = re.search("href='(.*?)'", s)
        archives.append(match.group(1))

    posts = []

    for a in archives:
        print("Getting archive " + a)
        url = base + "/?action=getTitles&widgetId=BlogArchive1&widgetType=BlogArchive&responseType=js&path=" + a;
        arch = urllib.request.urlopen(url)
        res = arch.read().decode('utf-8')
        matches = re.findall("http://.*?\.html", res)
        matches = filter(lambda x: "archive" not in x, matches)
        print("Found these posts:")
        print("\n".join(matches))
        posts.extend(matches)
        time.sleep(5) # Don't hammer the server too hard

    return posts

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

    return base

if __name__ == "__main__":
    print(get_base())
