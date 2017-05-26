import os

def as_html(parsed_post, replace_img_urls = False):
    if not os.path.isdir("data/html"):
        os.mkdir("data/html")

    path = "data/html/" + parsed_post["uid"] + ".html"

    if replace_img_urls:
        for image in parsed_post["images"]:
            new_path = "img/" + image.split("/")[-1]
            parsed_post["content"] = parsed_post["content"].replace(image, new_path)

    f = open(path, "w", encoding = 'utf-8')
    f.write(make_html(parsed_post))
    f.close()

def make_html(parsed_post):
    return ("<html>"
            + "<head><meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/></head>"
            + "<body><h1>" + parsed_post["title"] + "</h1>"
            + "<h3>" + parsed_post["date"] + "</h3>"
            + parsed_post["content"] + "</body></html>")
