import urllib.request
from html.parser import HTMLParser

#page = urllib.request.urlopen("http://thearchdruidreport.blogspot.se")
page = urllib.request.urlopen("file:///home/andreas/Projekt/adrdownload/index.html")

class ListHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.posts = []
        self.in_archive = False
        self.in_posts = False

    def handle_starttag(self, tag, attrs):
        if tag == "div" and ('id', "\\'BlogArchive1_ArchiveList\\'") in attrs:
            self.in_archive = True
            print("In archive")
        elif self.in_archive:
            if tag == "ul" and ('class', "\\'posts\\'") in attrs:
                self.in_posts = True
            elif tag == "a" and self.in_posts:
                for name, data in attrs:
                    if name == "href":
                        self.posts.append(data)


    def handle_endtag(self, tag):
        if tag == "div" and self.in_archive:
            self.in_archive = False
        if tag == "ul" and self.in_posts:
            self.in_posts = False

    def handle_data(self, data):
        pass

parser = ListHTMLParser()
data = page.read()

parser.feed(str(data))

print(parser.posts)
