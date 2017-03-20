#  get list of posts, listdownloader
#  for each post
#    run postdownloader
#    store post in json file

import postdownloader, os

if not os.path.isdir("data"):
    os.mkdir("data")

posts = ["file:///home/andreas/Projekt/adr_data/shouting.html"]

for post in posts:
    print(postdownloader.get_post(post))
