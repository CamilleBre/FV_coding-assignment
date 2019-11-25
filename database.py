# -*- coding: utf-8 -*-
"""
This is the class Database

Created on Mon Nov 23 10:06:37 2019

@author: camille
"""

from collections import defaultdict

class Database(object):
    """    
    This is a class for data structure relevant for food classification.
      
    Attributes: 
        graph (list): A list of tuples (child_node,parent_node) defining a graph stucture. 
        extract (dict): A dictionary where keys are image names and values node IDs (strings).
        sib (dict): A dictionary where keys are image names with node IDS and values numbers of siblings of the node in the graph 
        at the moment t when the extract is added.
    """
  

    def __init__(self, graph=("core", None)):
        """    
        The constructor for Database Class.
        
        Parameters:
            graph (list): A list of tuples (child_node,parent_node) defining a graph stucture. 
      
        """

        # Create a reference abstract category ("core") if not already present to instantiate the graph
        if graph[0] != ("core", None):
            graph.insert(0, ("core", None))
     
        # Instantiate the attributes 
        self.graph = graph
        self.extract = {}
        self.sib = {}
     

    def count_sib(self, node_to_count):
        """    
        The function to count the number of siblings for one node.
      
        Parameters: 
            node_to_count (str): node ID 
            
        Returns:
            nb_sib (int) : number of siblings of the node 
            
        """
        
        # Find the parent node of node_to_count 
        parent = [item[1] for item in self.graph[1:] if item[0]==node_to_count][0]
        
        # Compute the number of sibling (=having the same parent) nodes
        nb_sib = len([item[0] for item in self.graph[1:] if item[1]==parent])-1
   
        return nb_sib
    
              
    def add_nodes(self, nodes_to_add):
        """ 
        Add one or several nodes and edit the graph
        
        Parameters:
            node_to_add (list) : A list of tuples (child_node,parent_node) to be added to the existing graph
            
        """
        
        for new_child, new_parent in [item for item in nodes_to_add if item != ("core", None)]:  
            if len([item for item in self.graph if new_child in item])>0:
                print("Node " + new_child + " already exists")
                
            else:
                if len([item for item in self.graph if new_parent in item])==0:
                    print("Error:" + new_parent + " can't be a parent node because it doesn't exist")
                    
                else:
                    self.graph.insert(max([i for i, item in enumerate(self.graph) if new_parent in item])+1,(new_child, new_parent))
                    print("Node " + new_child + " added")
                    
                    
    def add_extract(self, new_extract):
        """ 
        Add an extract to extract attribute of the Database object.
        
        Parameters:
            new_extract (dict): A dictionary where keys are image names and values node IDs (strings) to be added to the existing extract
        """
        
        # Update the extract attribute considering the new extract
        self.extract.update(new_extract)
        
        # Count the number of siblings of each node of each image from the new_extract when added and save these values in sib attribute
        for key in new_extract:
            for value in new_extract[key]:
                if value in [item[0] for item in self.graph]:
                    self.sib[str(key+','+value)]=self.count_sib(value)
                else: 
                    self.sib[str(key+','+value)]=0
                
          
    def get_extract_status(self):
        """ 
        Return the status of the extract.
                
        Returns:
            status (dict): a dictionary where keys are names of images in the extract and values the status of each image. 
        """
        # Initialize an empty dict for status 
        status = defaultdict(list)

        
        # For each image of the extract attribute, for each label of the image, verify the status.
        for key in self.extract:
            # Initialize a temp_status, a dict to temporary save a status of each label of an image
            temp_status = defaultdict(list) 
            
            # Is there any label for the image?
            if self.extract[key] == []:
                status[key] = "valid"
                
            else:
                # Is the label of the image a node of the graph?
                for node in self.extract[key]:
                    
                    if node not in [item[0] for item in self.graph]:
                        temp_status[key].append("invalid")
                        
                    else:
                        # Does the node have new siblings since the extract was added?
                        new_nb_sib = self.count_sib(node) 
                            
                        if new_nb_sib > self.sib[str(key+','+node)]:
                            temp_status[key].append("coverage_staged")
                                                           
                        else:
                            # Does the node have any child node? 
                            if node in [item[1] for item in self.graph]:
                                temp_status[key].append("granularity_staged")
        
                            else: 
                                temp_status[key].append("valid")
                
                   
                                        
                    # Returns one status for each image
                    if "invalid" in temp_status[key]:
                        status[key] = "invalid"
                    elif "coverage_staged" in temp_status[key]:
                        status[key] = "coverage_staged"
                    elif "granularity_staged" in temp_status[key]:
                        status[key] = "granularity_staged"
                    else: status[key]= "valid"
            
        print(status)
        
        return(status)

      
                    
            
