import os
import datetime
import shutil

cameraroll = "../Pictures/Camera Roll" # Put your camera roll folder here!
allfiles = os.listdir(cameraroll)
print(len(allfiles))

pics = []
filtered = filter(lambda x: "." in x, allfiles)
l = 0
for x in filtered:
    l += 1
    pics.append(x)

for p in pics:
    timeraw = os.path.getmtime("{}/{}".format(cameraroll, p))
    timestamp = datetime.datetime.fromtimestamp(timeraw)
    month = "{:02d}".format(timestamp.month)
    year = str(timestamp.year)
    print("{} {} {}".format(p, year, month))

    if not os.path.exists("{}/{}".format(cameraroll, year)):
        os.makedirs("{}/{}".format(cameraroll, year))

    if not os.path.exists("{}/{}/{}".format(cameraroll, year, month)):
        os.makedirs("{}/{}/{}".format(cameraroll, year, month))

    orig = "{}/{}".format(cameraroll, p)
    dest = "{}/{}/{}/{}".format(cameraroll, year, month, p)
    shutil.move(orig, dest)
    
