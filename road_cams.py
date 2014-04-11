import urllib2
import calendar
import time
import os

pre = 'http://www.511.nebraska.gov/atis/snaps/cam'
post = '.jpg'
cams = ('201', 'Dodge Street at 102nd'), ('202', 'West Dodge at 118th, looking east'), ('203', 'West Dodge and 125th'), ('204', 'I-680 and Maple'), ('205', 'I-680 and Fort Street'), ('206', 'I-480 at Dodge Street'), ('207', 'I-480 and North Freeway'), ('209', 'I-480 and the Missouri River'), ('210', 'I-480 and Leavenworth'), ('211', 'I-80 and I-480'), ('212', 'I-80 at I-480 junction'), ('213', 'I-80 at 13th Street'), ('215', 'Highway 75 and L Street'), ('216', 'Highway 75 and Gilmore Avenue'), ('218', 'I-80 at 72nd Street'), ('219', 'I-80 and 84th Street'), ('220', 'I-80 and I-680 junction'), ('221', 'I-80 and I-680 north of I Street'), ('222', 'I-80 at Giles Road'), ('223', 'I-80 at 144th Street'), ('224', 'I-80 at Highway 370'), ('280', 'I-80 at the Missouri River')

"""

# make the directories

for thing in cams:
    os.mkdir(thing[0])

# make a lookup csv
z = open('lookup.txt', 'wb')
for thing in cams:
    print thing[0]
    z.write(thing[0] + "," + thing[1] + "\n")
    
"""

for n in range(0, 3600000, 300000):
    for thing in cams:
        os.chdir(thing[0])
        now = calendar.timegm(time.gmtime())
        filename = str(now) + post
        print thing[1], now
        f = open(filename, 'wb')
        current = pre + thing[0] + post
        f.write(urllib2.urlopen(current).read())
        f.flush()
        f.close()
        os.chdir(os.pardir)
    time.sleep(300)
    
"""
import time
import requests
from requests.exceptions import HTTPError

f = open('log.txt','ab')
pre = "http://www.511.nebraska.gov/atis/snaps/cam"
post = ".jpg"

def LeadZero(q):
    if len(str(q)) == 1:
        return "00" + str(q)
    elif len(str(q)) == 2:
        return "0" + str(q)
    else:
        return str(q)

for x in range(0,1000):
    baseurl = pre + LeadZero(x) + post
    try:
        r = requests.get(baseurl)
        r.raise_for_status()
    except HTTPError:
        print LeadZero(x) + ' failed'
    else:
        print LeadZero(x) + ' succeeded'
        f.write(r.url + "\n")
    time.sleep(1)

f.flush()
f.close()
"""