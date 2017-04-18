import os, urllib

def get_images(images, save_path):
    for image in images:
        short_name = image.split("/")[-1]
        path = save_path + "/" + short_name
        if not os.path.exists(path):
            get_image(image, path)

def get_image(image_url, path):
    print("Getting " + image_url)
    while True:
        try:
            page = urllib.request.urlopen(image_url)
            break
        except:
            print("Failed to get image " + image_url + ", retrying in 5 seconds")
            time.sleep(5)
    data = page.read()
    path_dir = "/".join(path.split("/")[:-1])
    if not os.path.exists(path_dir):
        os.makedirs(path_dir)
    f = open(path, "wb")
    f.write(data)
    f.close()
