import urllib.request
from html.parser import HTMLParser

def get_post(post):
    page = urllib.request.urlopen(post)

    class PageHTMLParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.date = ""
            self.title = ""
            self.content = []
            self.in_date = False
            self.in_title = False
            self.in_content = False
            self.in_link = False
            self.link = ""
            self.depth = 0
            self.current_div = []

        def handle_starttag(self, tag, attrs):
            if tag == "h2" and ('class', "\\'date-header\\'") in attrs:
                self.in_date = True
            elif tag == "h3":
                self.in_title = True
            elif tag == "div" and ('class', 'post-body entry-content') in attrs and not self.in_content:
                self.in_content = True
                self.depth += 1
                print("IN CONTENT")
                print(self.get_starttag_text())
            elif self.in_content:
                if tag == "div" and self.in_content:
                    self.depth += 1
                elif tag == "a" and self.in_content:
                    self.in_link = True
                    for name, data in attrs:
                        if name == "href":
                            self.link = data

        def handle_endtag(self, tag):
            if tag == "h2" and self.in_date:
                self.in_date = False
            elif tag == "h3" and self.in_title:
                self.in_title = False
            elif tag == "div" and self.in_content:
                self.content.append("".join(self.current_div).strip())
                self.current_div = []
                self.depth -= 1
                if self.depth == 0:
                    self.in_content = False

        def handle_data(self, data):
            if self.in_date:
                self.date += data.strip()
            elif self.in_title:
                self.title += data.replace("\\n", "").strip()
            elif self.in_content:
                self.current_div.append(data.replace("\\n", " ").replace("\\'", "'"))
                if self.in_link:
                    self.current_div.append(" [" + self.link + "]")
                    self.in_link = False

    parser = PageHTMLParser()
    data = page.read()

    #parser.feed(str(data))

    #print(parser.title + " - " + parser.date + "\n")

    #content = [x for x in parser.content if x]

    #print("\n\n".join(content))

    import re

    date = re.findall(b"<h2 class='date-header'>.*?<span>(.*?)</span>.*?</h2>", data)[0]

    print("DATE: \"" + date.decode('utf-8') + "\"")

    title = re.findall(b"<h3.*?>(.*?)</h3>", data, re.DOTALL)[0]

    print("TITLE: \"" + title.decode('utf-8').strip() + "\"")

    start = re.search(b"<div class='post-body entry-content'", data)
    end = re.search(b"<div class='post-footer'>", data)

    content = data[start.start():end.start()].decode('utf-8')
    #print(content)

    parser.feed(content)

    #print("\n\n".join(parser.content))

if __name__ == "__main__":
    get_post("file:///home/andreas/Projekt/adr_data/shouting.html")
