import re

def parse_post(path):
    name = (path.split("/")[-1]).split(".")[0]

    f = open(path)
    data = f.read()
    f.close()

    date = re.findall("<h2 class='date-header'>.*?<span>(.*?)</span>.*?</h2>", data)[0]

    title = re.findall("<h3.*?>(.*?)</h3>", data, re.DOTALL)[0]
    title = title.strip()

    start = re.search("<div class='post-body entry-content'", data)
    end = re.search("<div class='post-footer'>", data)

    content = data[start.start():end.start()]

    images = re.findall("<img.*?src=[\"'](.*?)[\"'].*?/>", content)

    uid = parse_date(date) + "-" + name

    return {"uid": uid, "title":title, "date":date, "content":content, "images":images}

def parse_date(date):
    # Date comes in the form: "day_of_week, month day, year"
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    split = date.split(",")
    year = split[2].strip()
    month = str(months.index((split[1].strip().split(" ")[0])) + 1).zfill(2)
    day = split[1].strip().split(" ")[1]
    return year + "-" + month + "-" + day


if __name__ == "__main__":
    dates = ["Wednesday, November 16, 2016",
             "Wednesday, September 05, 2012"]
    for date in dates:
        print(parse_date(date))

    post = parse_post("data/raw/2006/05/after-prosthetic-society.html")

    print("UID: \"" + post["uid"] + "\"")
    print("Title: \"" + post["title"] + "\"")
    print("Date: \"" + post["date"] + "\"")
    
    print("example path: data/txt/" + post["uid"] + ".txt")
