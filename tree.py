class Node():
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node is not None and (node not in self.children):
            self._children.append(node)
            node.parent = self
        if self._parent is not None and not node._children:
            return

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None
        if not node._children:
            return

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent == node:
            return
        former = self._parent
        if former:
            former.remove_child(self)
        if node is not None:
            self._parent = node
            node.add_child(self)
        else:
            self._parent = None

    def depth_search(self, value):
        if self.value == value:
            return self
        for child in self.children:
            result = child.depth_search(value)
            if result is not None:
                return result

        # s = list()
        # s.append(self)

        # while len(s) > 0:
        #     node = s.pop()
        #     if node.value == value:
        #         return node
        #     s = node.children + s

    def breadth_search(self, value):
        s = list()
        s.append(self)

        while len(s) > 0:
            node = s.pop()
            if node.value == value:
                return node
            s += node.children
