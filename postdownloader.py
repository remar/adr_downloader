import urllib.request, re

def get_post(post):
    page = urllib.request.urlopen(post)
    data = page.read()

    date = re.findall(b"<h2 class='date-header'>.*?<span>(.*?)</span>.*?</h2>", data)[0].decode('utf-8')

    print("DATE: \"" + date + "\"")

    title = re.findall(b"<h3.*?>(.*?)</h3>", data, re.DOTALL)[0].decode('utf-8')
    title = title.strip()

    print("TITLE: \"" + title.strip() + "\"")

    start = re.search(b"<div class='post-body entry-content'", data)
    end = re.search(b"<div class='post-footer'>", data)

    content = data[start.start():end.start()].decode('utf-8')

    name = (post.split("/")[-1]).split(".")[0]

    return {"name":name, "title":title, "date":date, "content":content}

if __name__ == "__main__":
    print(get_post("file:///home/andreas/Projekt/adr_data/shouting.html")["title"])
