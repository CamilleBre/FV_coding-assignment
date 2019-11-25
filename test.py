#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the code to test the class Database

Created on Mon Nov 25 14:05:39 2019

@author: camille
"""

import json

from database import Database



## Test on a basic dataset

build = [("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]

extract = {"img001": ["A", "B"], "img002": ["A", "C1"]}

edits = [("B1", "B"), ("C2", "C")]

extract2 = {"img003": ["A", "C1"], "img004": ["B"]}

edits2 =[ ("C3", "C")]

# Create a Database initialized with graph = build to test the constructor
db=Database(build)

# Add an extract to test the add_extract function
db.add_extract(extract)

# Get the extract status to test the get_extract_status function
db.get_extract_status()

# Add nodes to test the add_nodes function
db.add_nodes(edits)

# Verify the new extract status
db.get_extract_status()

# Add an other extract
db.add_extract(extract2)

# Verify the new extract status
db.get_extract_status()

# Add other nodes
db.add_nodes(edits2)

# Verify the new extract status
db.get_extract_status()




### The on the provided dataset 

# Import the data 
with open('./data/graph_build.json', 'rb') as f:
    graph_build = json.load(f)
 
with open('./data/img_extract.json', 'rb') as f:
    img_extract = json.load(f)
 
with open('./data/graph_edits.json', 'rb') as f:
    graph_edits = json.load(f)
 
with open('./data/expected_status.json', 'rb') as f:
    expected_status = json.load(f)

# Create a Database initialized with graph = graph_build 
db2 = Database(graph_build)
 
# Add the extract img_extract
db2.add_extract(img_extract)
 
# Check the extract status
db2.get_extract_status()
 
# Add the nodes graph_edits
db2.add_nodes(graph_edits)
 
# Get the final 
final_status = db2.get_extract_status()
 
#Compare the final status with expected status 
if final_status == expected_status: 
    print ("YOUPIII!!!!") 
    
else: 
    print("oh no..." )
    
    for key in expected_status.keys():
        if final_status[key] != expected_status[key]:
            print("Image "+ key + " get status "+ final_status[key] + "while expected " +expected_status[key])
            
