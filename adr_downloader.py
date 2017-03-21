#  get list of posts, listdownloader
#  for each post
#    run postdownloader
#    store post in json file

import listdownloader, postdownloader, os

if not os.path.isdir("data"):
    os.mkdir("data")

posts = ["file:///home/andreas/Projekt/adr_data/shouting.html"]

#posts = listdownloader.get_posts()
posts = listdownloader.get_posts_cached()

# Only get first post for now
post_url = posts[0]

path = "data/raw/" + postdownloader.get_path(post_url)
path_dir = "/".join(path.split("/")[:-1])

print(path_dir)

if not os.path.exists(path):
    # download and store it
    pass

#print(postdownloader.get_post(post))
