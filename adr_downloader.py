import listdownloader, postdownloader, os, time

if not os.path.isdir("data"):
    os.mkdir("data")

#posts = listdownloader.get_posts()
posts = listdownloader.get_posts_cached()

def get_path(url):
    return "data/raw/" + postdownloader.get_path(url)

for post_url in posts[0:6]:
    path = get_path(post_url)

    if not os.path.exists(path):
        # download and store it
        post_data = postdownloader.get_post(post_url)
        path_dir = "/".join(path.split("/")[:-1])
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
        f = open(path, "w")
        f.write(post_data)
        f.close()
        time.sleep(5)
    else:
        print("Already got " + path)
