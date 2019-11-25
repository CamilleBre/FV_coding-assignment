#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:05:39 2019

@author: camille
"""

import json

from database import Database

build=[("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
extract={"img001": ["A", "B"], "img002": ["A", "C1"]}
edits=[("B1", "B"), ("C2", "C")]
extract2={"img003": ["A", "C1"], "img004": ["B"]}
edits2 =[("C3", "C")]

db=Database(build)

db.add_extract(extract)

db.get_extract_status()

db.add_nodes(edits)

db.get_extract_status()

db.add_extract(extract2)

db.get_extract_status()

db.add_nodes(edits2)

db.get_extract_status()




### Import data 

with open('./data/graph_build.json', 'rb') as f:
 graph_build = json.load(f)
 
with open('./data/img_extract.json', 'rb') as f:
 img_extract = json.load(f)
 
with open('./data/graph_edits.json', 'rb') as f:
 graph_edits = json.load(f)
 
with open('./data/expected_status.json', 'rb') as f:
 expected_status = json.load(f)

 db2 = Database(graph_build)
 db2.add_extract(img_extract)
 db2.get_extract_status()
 db2.add_nodes(graph_edits)
 get_status2={}
 get_status2 = db2.get_extract_status()
 
 if get_status2 == expected_status: 
    print ("YOUPI ÇA MARCHE !!!!") 
 else: 
    print("oh non" )
