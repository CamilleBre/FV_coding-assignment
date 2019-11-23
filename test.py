#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:38:58 2019

@author: camille
"""

import json 


from database import Database

# Initial graph
build=[("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
# Extract
extract={"img001": ["A", "B"], "img002": ["A", "C1"], "img003": ["B", "E"]}
# Graph edits
edits=[("A1", "A"), ("A2", "A"), ("C2", "C")]


db=Database(build)
db.add_extract(extract)
db.add_nodes(edits)
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

 db = Database(graph_build)
 db.add_extract(img_extract)
 db.add_nodes(graph_edits)
 obtained_status = db.get_extract_status()
 
 if obtained_status == expected_status: 
    print ("YOUPI ÇA MARCHE !!!!") 
 else: 
    print("oh non" )
    
    
#[obtained_status[i] != expected_status[i] for i in expected_status.keys()]

## 0,4,7
#obtained_status[0]

 