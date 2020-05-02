#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET
top = []
in_file = open('map.xml', "rb")
tree = ET.parse(in_file)
root = tree.getroot()
for obj in root.iter('object'):
    cls = obj.find('name').text
    xmlbox = obj.find('bndbox')
    b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
         int(xmlbox.find('ymax').text))
    x = (b[2]+b[0]) // 2
    y = (b[3]+b[1]) // 2
    with open("node.txt",'a') as fp:
        fp.write("{} {} {}".format(cls,x,y)+'\n')
    top.append([cls, (b[2] + b[0]) // 2, (b[3] + b[1]) // 2])
