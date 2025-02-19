#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:32:30 2025

@author: jamesbean
"""

from chimerax.core.commands import run 


#enter the model id of the symmetrised capsid model
symmetrised_model_ID = "2"


#set this value to the model ID desired for  output center of mass marker set
marker_set_ID = "100"


#enter chain IDs relevant to the model that was symmetrised 
chains = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
     
          "R","S"]

#loops over all symmetry generated models of symmetrised_model_id
for i in range(1,61):
   
    
    for k in chains:
        
        
        #places marker for evert chain in every generated symmetry copy e.g. 
        #2.60/A
        run(session, f"measure center #{symmetrised_model_ID}.{i}/{k} mark \
            true modelId #{marker_set_ID}")


#enhances visability of markers. 
run(session,f"marker change #{marker_set_ID} color red radius 5")