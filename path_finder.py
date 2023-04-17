from tree import Node


class KnightPathFinder:
    def __init__(self, root):
        x, y = root
        self._root = Node((x, y))
        self._considered_positions = {(x, y)}

    def get_valid_moves(self, pos):
        x, y = pos
        deltas = (
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
            (2, 1),
            (-2, 1),
            (2, -1),
            (-2, -1),
        )
        possibleMoves = list()
        for delta in deltas:
            newX = x + delta[0]
            newY = y + delta[1]
            if newX in range(8) and newY in range(8):
                possibleMoves.append((newX, newY))
        return set(possibleMoves)

    def new_move_positions(self, pos):
        posMoves = self.get_valid_moves(pos)
        diffMoves = posMoves - self._considered_positions
        self._considered_positions |= posMoves
        return diffMoves

    def build_move_tree(self):
        s = list()
        s.append(self._root)

        while len(s) > 0:
            newest = s.pop(0)
            starting_pos = newest.value
            newMoves = self.new_move_positions(starting_pos)
            for move in newMoves:
                tempNode = Node(move)
                newest.add_child(tempNode)
                s.append(tempNode)

    def find_path(self, end_position):
        end_pos = end_position
        end_node = self._root.breadth_search(end_pos)
        return self.trace_to_root(end_node)

    def trace_to_root(self, end_node):
        path = list()
        temp = end_node
        path.append(temp.value)
        while temp.parent is not None:
            temp = temp.parent
            path = [temp.value] + path
        return path


finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((2, 1)))  # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3)))  # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
print(finder.find_path((7, 6)))  # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]
