# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:08:33 2015

@author: KHADIJA
"""


from items import *


room_hallway_g_w = { 
        "name": "hallway, G, W",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}



room_hallway_g_e = {
    "name": "hallway, G, E",

    "description":
    """Y...............................................


    .""",

    "exits": {"": ""}, 

    "items": []
}  



room_hallway_g_c_w = {
    "name": "hallway, G, C, W",

    "description": 
    """Y...............................................


    .""",

    "exits": {"": ""},

    "items": []
}



room_hallway_g_c_e = {
    "name": "hallway, G, C, E",

    "description": 
    """Y...............................................


    .""",

    "exits": {"": ""},

    "items": []
}

            
            
room_dining_w = { 
        "name": "dining room, G, W",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    



room_dining_e = {
    "name": "dining room, G, E",

    "description":
    """Y...............................................


    .""",

    "exits": {"": ""},

    "items": []
}


 
room_kitchen = { 
        "name": "kitchen,G",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}     


room_offfice = { 
        "name": "office,G",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}  
    
room_lounge_e = { 
        "name": "lounge, G, E",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    


room_lounge_w = {
    "name": "lounge, G, W",

    "description": 
    """Y...............................................


    .""",

    "exits": {"": ""}, 

    "items": []
}



room_store = { 
        "name": "store,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    

room_pantry = { 
        "name": "pantry,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    

room_torture = { 
        "name": "torture,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    

room_hallway_b = { 
        "name": "hallway,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    

room_secret = { 
        "name": "secret room,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    

room_workshop = { 
        "name": "workshop,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    

room_winecellar = { 
        "name": "wine cellar,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    

room_hallway_f_s = { 
        "name": "hallway, F1, S",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    


room_hallway_f_e = {
    "name": "hallway, F1, E",

    "description":
    """Y................................................


    .""",

    "exits": {"": ""},

    "items": []
}


room_hallway_f_n = {
    "name": "hallway, F1, N",

    "description":
    """Y.................................................


    .""",

    "exits": {"": ""},

    "items": []
}


room_hallway_f_w = {
    "name": "hallway, F1, W",

    "description": 
    """Y..................................................


    .""",

    "exits": {"": ""},

    "items": []
}


room_child = { 
        "name": "child bedroom,F1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    


room_store = { 
        "name": "store,F1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    


room_bathroom = { 
        "name": "bathroom,F1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    

room_master = { 
        "name": "master bedroom,F1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"" : ""},

    "items": []
}    


rooms = { 
        
       "hallway, G, W": room_hallway_g_w,
       "hallway, G, E": room_hallway_g_e,
       "hallway, G, C, W": room_hallway_g_c_w,
       "hallway, G, C, E": room_hallway_g_c_e,
       "dining room, G, W": room_dining_w,
       "dining room, G, E": room_dining_e,
       "kitchen,G": room_kitchen,
       "office,G": room_office,
       "lounge, G, E": room_lounge_e,
       "lounge, G, W": room_lounge_w,
       "store,F-1": room_store,
       "pantry,F-1": room_pantry,
       "torture,F-1": room_torture,
       "hallway,F-1": room_hallway,
       "secret room,F-1": room_secert,
       "workshop,F-1": room_workshop,
       "wine cellar,F-1": room_winecellar,
       "hallway, F1, S": room_hallway_f_s,
       "hallway, F1, E": room_hallway_f_e,
       "hallway, F1, N": room_hallway_f_n,
       "hallway, F1, W": room_hallway_f_w,
       "child bedroom,F1": room_child,
       "store,F1": room_store,
       "bathroom,F1": room_bathroom,
       "master bedroom,F1": room_master
 }