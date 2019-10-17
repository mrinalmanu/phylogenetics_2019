#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 23:32:33 2019

@author: mrinalmanu
"""

"""Part I

"""

import sys
from Bio import Phylo
from io import StringIO  
from ete3 import Tree, TreeStyle, NodeStyle
import matplotlib.pyplot as plt
import lxml.etree as ET
import random
from pylab import savefig
import re

with open('/home/mrinalmanu/Documents/life.txt', 'r') as file:
    for item in file:
        treedata = ''.join('{}'.format(item))

handle = StringIO(treedata)
tree = Phylo.read(handle, "newick")

"""Saving an ascii tree to a file"""

stdoutOrigin=sys.stdout 
sys.stdout = open('/home/mrinalmanu/Documents/output_phylo/ascii_phylo_life.txt', 'w')
Phylo.draw_ascii(tree)
sys.stdout.close()
sys.stdout=stdoutOrigin

####################


''' Just right click and save'''
Phylo.draw(tree)
savefig(path+'look.png', dpi = 600)


"""Exporting tree as an XML file"""

Path = '/home/mrinalmanu/Documents/output_phylo/'

lines = tree_data
root = ET.Element("root")
for l in lines:
  elems = l.split(":")
  if len(elems) == 2:
    elems = map(lambda x: x.strip(), elems)
    line = ET.SubElement(root, "line")
    item1 = ET.SubElement(line, "item1")
    item2 = ET.SubElement(line, "item2")
    item1.text = elems[0]
    item2.text = elems[1]

tree = ET.ElementTree(root)
tree.write(path+'life.xml', pretty_print=True)


###########################################################################

t = Tree('{}'.format(treedata), format =1)
circular_style = TreeStyle()
circular_style.show_branch_length = True # show branch length
circular_style.show_branch_support = True # show support
circular_style.mode = "c" # draw tree in circular mode
circular_style.scale = 100


t.render(path+"beautiful_life_tree.png", w=3000, units="mm", tree_style=circular_style)
t.render(path+"beautiful_life_tree.pdf", w=3000, units="mm", tree_style=circular_style)

species = []
for node in t.get_leaf_names():
    species.append(node)

random_nodes = []

i = 0
for i in range(0, 42):
    random_nodes.append(str(random.choice(species)))
    i = i + 1
    
""" For extreme situations use this to cleane the name and prune trees """
#clean_nodes = [re.sub(r'\n--', '', elem) for elem in random_nodes]
# new_t = t
# for item in clean_nodes:
#     print('Pruning: {}{}{}'.format("'",item,"'"))
#    new_t.prune('{}{}{}'.format("'",item,"'"))
    

# Creates an independent node style for each node, which is
# initialized with a red foreground color.
new_t.prune(random_nodes)

""" Getting this tree in some new style other than the basic """
# Basic tree style
ts = TreeStyle()
ts.show_leaf_name = True

for n in new_t.traverse():
   nstyle = NodeStyle()
   nstyle["fgcolor"] = "red"
   nstyle["size"] = 15
   n.set_style(nstyle)

# Let's now modify the aspect of the root node
new_t.img_style["size"] = 30
new_t.img_style["fgcolor"] = "blue"

 
new_t.render(path+"beautiful_pruned_life_tree.png", w=3000, units="mm", tree_style=circular_style)
new_t.render(path+"beautiful_pruned_life_tree.pdf", w=3000, units="mm", tree_style=circular_style)


""" End of code """
