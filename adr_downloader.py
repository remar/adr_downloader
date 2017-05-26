import listdownloader, postdownloader, imagedownloader, postparser, os, time, html

if not os.path.isdir("data"):
    os.mkdir("data")

posts = listdownloader.get_posts()

def get_path(url):
    return "data/raw/" + postdownloader.get_path(url)

for post_url in posts:
    path = get_path(post_url)

    if not os.path.exists(path):
        post_data = postdownloader.get_post(post_url)
        path_dir = "/".join(path.split("/")[:-1])
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
        f = open(path, "w", encoding = 'utf-8')
        f.write(post_data)
        f.close()
        time.sleep(5) # Don't hammer the server too hard

    parsed_post = postparser.parse_post(path)

    imagedownloader.get_images(parsed_post["images"], "data/html/img")

    html.as_html(parsed_post, replace_img_urls = True)
