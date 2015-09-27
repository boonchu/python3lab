#! /usr/bin/env python
class Tree:
    def __init__(self, type, height, fruit = None):
        self.type = type
        self.height = height
        if fruit:
            self.fruit = fruit
        else:
            self.fruit = None
    def __str__(self):
        temp = "Tree type: " + self.type
        temp += ", height: " + str(self.height)
        temp += ", fruit: " + str(self.fruit)
        return temp
        
tree1 = Tree("spruce", 40)
print tree1
tree2 = Tree("apple", 10, "apples")
print tree2

set_of_trees = set([])

set_of_trees.add(tree1)
set_of_trees.add(tree2)

print "\nThese are the trees in the set: "
for item in list(set_of_trees):
    print item
