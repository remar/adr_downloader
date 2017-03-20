import urllib.request, re

def get_post(post):
    page = urllib.request.urlopen(post)
    data = page.read()

    date = re.findall(b"<h2 class='date-header'>.*?<span>(.*?)</span>.*?</h2>", data)[0].decode('utf-8')

    print("DATE: \"" + date + "\"")

    title = re.findall(b"<h3.*?>(.*?)</h3>", data, re.DOTALL)[0].decode('utf-8')
    title = title.strip()

    print("TITLE: \"" + title.strip() + "\"")

    start = re.search(b"<div class='post-body entry-content'", data)
    end = re.search(b"<div class='post-footer'>", data)

    content = data[start.start():end.start()].decode('utf-8')

    name = (post.split("/")[-1]).split(".")[0]

    return {"name":name, "title":title, "date":date, "content":content}

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
