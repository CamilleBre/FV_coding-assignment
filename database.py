# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import defaultdict

class Database(object):

    def __init__(self,graph=("core", None),img={}):

     #Créer une liste de tuples 
     if graph[0] != ("core", None):
         graph.insert(0,("core", None))
     
    
     self.graph=graph
     self.img=img
     self.last_added=[]
                
    def add_nodes(self,nodes_to_add):
#    """ Add one or several nodes and edit the graph
#    
#    Parameters
#    ----------
#    node_to_add : list of tuples 
#    """
        
    #### RAJOUTER DES CONDITIONS POUR NONE 
        self.last_added=[]
        for new_child, new_parent in [item for item in nodes_to_add if item != ("core", None)]:  
            if len([item for item in self.graph if new_child in item])>0:
                print(" CE NOEUD EXISTE DEJA!")
            else:
                if len([item for item in self.graph if new_parent in item])==0:
                    print("Noeud parent inexistant!")
                else:
                    self.graph.insert(max([i for i, item in enumerate(self.graph) if new_parent in item])+1,(new_child, new_parent))
                    print("noeud", new_child, "ajouté!")
                    self.last_added.append((new_child, new_parent))
      
    def add_extract(self,extract):
        """ Add an extract as a dict 
        
        Parameters
        ----------
        extrat : dictionnay key=image, value=node
        """
        self.img.update(extract)
        
    
#    def get_extract_status(self):
#        status={}
#        for key in self.img:
#            nkey = len([item for item in self.graph if item[1] == self.img[key][0]])
#            
#            if nkey > 1:
#                status[key]="granularity_staged"
#            elif nkey == 1:
#                status[key]="coverage_staged"
#            else:
#                if len([item for item in self.graph if item[0] == self.img[key][0]]) == 0:
#                    status[key]="invalid"
#                else: status[key]="valid"
#                
#        print(status) 
#        
        
       
     
#    def get_extract_status(self):
#        status = defaultdict(list)
#        temp_status = defaultdict(list)
#        for key in self.img:
#            for i in range(0,len(self.img[key])-1):
#                nkey = len([item for item in self.graph if item[1] == self.img[key][i]])
#                
#                if nkey > 1:
#                    try: temp_status[key].append("granularity_staged")
#                    except KeyError:
#                        temp_status[key]=("granularity_staged")
#                elif nkey == 1:
#                    try: temp_status[key].append("coverage_staged")
#                    except KeyError:
#                        temp_status[key]="coverage_staged"
#                else:
#                    if len([item for item in self.graph if item[0] == self.img[key][i]]) == 0:
#                        try: temp_status[key].append("invalid")
#                        except KeyError:
#                            temp_status[key]="invalid"
#                    else: 
#                        try: temp_status[key].append("valid")
#                        except KeyError:
#                            temp_status[key]="valid"
#                        
#            print(temp_status)        
#            if "invalid" in temp_status[key]:
#                status[key] = "invalid"
#            elif "coverage_staged" in temp_status[key]:
#                status[key] = "coverage_staged"
#            elif "granularity_staged" in temp_status[key]:
#                status[key] = "granularity_staged"
#            else: status[key]= "valid"
#            
#            
#        print(status) 
                
        
    
#    def get_extract_status(self):
#        status = defaultdict(list)
#        temp_status = defaultdict(list)
#        for key in self.img:
#            for i in range(0,len(self.img[key])):
#                nkey = len([item for item in self.graph if item[1] == self.img[key][i]])
#                
#                if nkey > 1:
#                    temp_status[key].append("granularity_staged")
#                elif nkey == 1:
#                    temp_status[key].append("coverage_staged")
#    
#                else:
#                    if len([item for item in self.graph if item[0] == self.img[key][i]]) == 0:
#                        temp_status[key].append("invalid")
#                    else: 
#                        temp_status[key].append("valid")
#                print(i)
#                print(temp_status)
#            
#            if "invalid" in temp_status[key]:
#                status[key] = "invalid"
#            elif "coverage_staged" in temp_status[key]:
#                status[key] = "coverage_staged"
#            elif "granularity_staged" in temp_status[key]:
#                status[key] = "granularity_staged"
#            else: status[key]= "valid"
#            
#            
#        print(status) 
        
        
    def get_extract_status(self):
        status = defaultdict(list)
        temp_status = defaultdict(list)
        for key in self.img:
            for i in range(0,len(self.img[key])):            
                if len([item for item in self.graph if item[1] == self.img[key][i]]) >= 1:
                    temp_status[key].append("granularity_staged")
                else:
                    if len([item for item in self.graph if item[0] == self.img[key][i]]) == 0:
                        temp_status[key].append("invalid")
                    else: 
                        if [item[1] for item in self.graph if item[0] == self.img[key][i]][0] in [item[1] for item in self.last_added if item[0]!=self.img[key][i]]:
                            temp_status[key].append("coverage_staged")
                        else:
                            temp_status[key].append("valid")
            
            if "invalid" in temp_status[key]:
                status[key] = "invalid"
            elif "coverage_staged" in temp_status[key]:
                status[key] = "coverage_staged"
            elif "granularity_staged" in temp_status[key]:
                status[key] = "granularity_staged"
            else: status[key]= "valid"
            
            
        print(status) 

        
        


