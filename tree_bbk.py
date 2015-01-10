class Node:
    def __init__ (self, article):
        self.article = article
        self.children = []
        self.parent = None

    def print_(self, level = 0):

        print ("{0} {1}\n".format('\t'*level, self.article) )
        for child in self.children:
            child.print_(level + 1)


class Tree:
    def __init__ (self):
        self.nodes = {}

    def push(self, item):
        article, parent = item
        if parent not in self.nodes:
            self.nodes[parent] = Node(parent)
        if article not in self.nodes:
            self.nodes[article] = Node(article)
        if parent == article:
            return
        self.nodes[article].parent = self.nodes[parent]
        self.nodes[parent].children.append(self.nodes[article] )




    @property
    def roots(self):return (x for x in self.nodes.values() if not x.parent)




