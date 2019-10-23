#!/usr/bin/env python
# coding: utf-8

# In[28]:


#libraries
import pandas
import numpy


# In[29]:


#part1 - selecting only lines from ligand
#importing the table
ring = pandas.read_csv("/home/diego/Dropbox/jupyter/examples/model.000.01_edges.txt", sep = '\t')

#selecting rows from the ligand
ring2 = ring.loc[ring['NodeId1'] >= 'B']


#part2 - selecting residues from the ligand
#only numbers from the NodeID1
# using join() + isnumeric() + list comprehension + map() 
# Extracting numbers from list of strings 
lista = list(map(lambda sub:int(''.join(
    [ele for ele in sub if ele.isnumeric()])), list(ring2['NodeId1']))) 

lista

