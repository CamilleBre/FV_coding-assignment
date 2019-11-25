# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import defaultdict

class Database(object):
    """    This is a class for 
      
    Attributes: 
        graph (list): 
        img (dict): 
        sib (dict)
    """
  


    def __init__(self,graph=("core", None)):
        """    
        The constructor for Database Class.
      
        Attributes: 
            graph (list): 
            img (dict): 
            sib (dict) 
        """

        # Create a reference abstract category ("core") if not already present to instantiate the graph
        if graph[0] != ("core", None):
            graph.insert(0,("core", None))
     
        # Instantiate the attributes 
        self.graph=graph
        self.extract={}
        #self.extract_status= {} 
        self.sib={}
        
        # Compute and update the number of siblings of each node in the initial graph 
        #for item in self.graph[1:]:
        #    self.sib[item[0]] = self.count_sib(item[0])
     
     



    def count_sib(self, node_to_count):
        """    
        The function to count the number of siblings for one node (or list of nodes)
      
        Parameters: 
            node_to_count (str) 
            
        Returns:
            nb_sib (int) : number of siblings of the node 
            
        """
        
        # Find the parent node of node_to_count 
        parent = [item[1] for item in self.graph[1:] if item[0]==node_to_count][0]
        
        # Compute the number of sibling nodes(=having the same parent)
        nb_sib = len([item[0] for item in self.graph[1:] if item[1]==parent])-1
   
        return nb_sib
    
              
    
    def add_nodes(self,nodes_to_add):
        """ 
        Add one or several nodes and edit the graph
        
        Parameters:
        node_to_add  (list of tuples) :
            
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
                    
        
        #self.update_extract_status()  
        
        # Update sib
       # for item in self.graph[1:]:
        #    self.sib[item[0]] = self.count_sib(item[0])
            
           
                    
    def add_extract(self,new_extract):
        """ 
        Add an extract to img attribute of the Database
        
        Parameters
        extract : dictionnay key=image, value=node
        """
        self.extract.update(new_extract)
        
        for key in new_extract:
            for value in new_extract[key]:
                if value in [item[0] for item in self.graph]:
                    self.sib[str(key+','+value)]=self.count_sib(value)
                else: 
                    self.sib[str(key+','+value)]=0
                
            
    
#    def update_extract_status(self): 
#        
#        for key in self.extract_status.keys():
#            if  self.extract_status[key]=='':
#            
#                # Initialize a dict for status and temp_status to temporary save the status of each label of an image 
#                #status = defaultdict(list)
#                temp_status = defaultdict(list)
#
#            
#                # Is there any label for the image?
#                if self.extract[key] == []:
#                    self.extract_status[key] = "valid"
#                    
#                else:
#                    # Is the label of the image a node of the graph?
#                    for node in self.extract[key]:
#                        
#                        if node not in [item[0] for item in self.graph]:
#                            temp_status[key].append("invalid")
#                            
#                        else:
#                            # Does the node have new siblings since the extract was added?
#                            if node in self.sib.keys():
#                                new_nb_sib = self.count_sib(node) 
#                                
#                                if new_nb_sib > self.sib[node]:
#                                    temp_status[key].append("coverage_staged")
#                                    
#                                # Does the node have any child node? 
#                                else:
#                                    if node in [item[1] for item in self.graph]:
#                                        temp_status[key].append("granularity_staged")
#            
#                                    else: 
#                                        temp_status[key].append("valid")
#                    
#                       
#                                            
#                        # Returns one status for each image
#                        if "invalid" in temp_status[key]:
#                            self.extract_status[key] = "invalid"
#                        elif "coverage_staged" in temp_status[key]:
#                            self.extract_status[key] = "coverage_staged"
#                        elif "granularity_staged" in temp_status[key]:
#                            self.extract_status[key] = "granularity_staged"
#                        else: self.extract_status[key]= "valid"
#    
#        
        
        
           
    def get_extract_status(self):
        """ 
        Return the status of 
        
        Parameters:
        extract : dictionnay key=image, value=node
        
        Returns:
        """
        # Initialize a dict for status and temp_status to temporary save the status of each label of an image 
        status = defaultdict(list)
        temp_status = defaultdict(list)
        
        # For each image of the img dict, for each label, verify the status.
        for key in self.extract:
            
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
                                
                            # Does the node have any child node? 
                        else:
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
            
        #Update 
        #for item in self.graph[1:]:
        #    self.bro[item[0]] = self.count_bro(item[0])
        #status = dict(zip(self.status_extract.keys(),[self.status_extract.values()[key][1] for key in self.status_extract.keys()]))
        print(status)
        
        return(status)

      
                    
            
