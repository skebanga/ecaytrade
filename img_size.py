#!/usr/bin/python

href = "http://www.ecaytrade.com/images/850833_2015081308.jpg"

imgdata = urllib2.urlopen(href)
image_type,width,height = imageInfo.getImageInfo(imgdata)

print image_type
print width
print height

