#!/usr/bin/env python3
#nextbus.py
import sys

if len(sys.argv) != 3:
    raise SystemExit('Usage: nextbus.py route stopid\nSample: nextbus.py 22 14791')

route = sys.argv[1]
stopid = sys.argv[2]

#print('Command Options:', sys.argv)
#raise SystemExit(0)


import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route, stopid))
#print(type(u))
data = u.read()
#print("Result:\n",data)

from xml.etree.ElementTree import XML
doc = XML(data)
#print("Result:\n",doc)

#import pdb; pdb.set_trace()   #Launch debugger

for pt in doc.findall('.//pt'):
    print(pt.text)
