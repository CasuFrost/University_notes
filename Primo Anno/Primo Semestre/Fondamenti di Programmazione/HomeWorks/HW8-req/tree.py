# -*- coding: utf-8 -*-

class Tree:
    def __init__(self, v):
        self.children = []
        self.value = v
    
    def AddChildValue(self, v):
        self.children.append(Tree(v))
    
    def AddChild(self, tree):
        self.children.append(tree)
        
    def isLeaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False
    
    def __repr__(self, prefix=""):
        result = str(self.value) + "\n"
        prefix += "=|"
        for c in self.children:
            result += prefix + c.__repr__(prefix)
        return result
    