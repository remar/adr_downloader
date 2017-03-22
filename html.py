import os

def as_html(parsed_post):
    if not os.path.isdir("data/html"):
        os.mkdir("data/html")

    path = "data/html/" + parsed_post["uid"] + ".html"

    f = open(path, "w")
    f.write(make_html(parsed_post))
    f.close()

def make_html(parsed_post):
    return ("<html><body><h1>" + parsed_post["title"] + "</h1>"
            + "<h3>" + parsed_post["date"] + "</h3>"
            + parsed_post["content"] + "</body></html>")
