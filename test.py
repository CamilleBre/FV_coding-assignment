#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:38:58 2019

@author: camille
"""

from database import Database

# Initial graph
build=[("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
# Extract
extract={"img001": ["A", "B"], "img002": ["A", "C1"], "img003": ["B", "E"]}
# Graph edits
edits=[("A1", "A"), ("A2", "A"), ("C2", "C")]

db=Database(build)
db.add_nodes(edits)
db.add_extract(extract)
db.get_extract_status()
