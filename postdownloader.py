import urllib.request
from html.parser import HTMLParser

#page = urllib.request.urlopen("http://thearchdruidreport.blogspot.se/2016/11/when-shouting-stops.html")
page = urllib.request.urlopen("file:///home/andreas/Projekt/adr_downloader/live.html")

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
        elif tag == "div" and ('class', "\\'post-body") in attrs and not self.in_content:
            self.in_content = True
            self.depth += 1
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

start = re.search(b"<div class='post-body entry-content'", data)
end = re.search(b"<div class='post-footer'>", data)

print(data[start.start():end.start()].decode('utf-8'))
