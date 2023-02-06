import hashlib


def _hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


class MerkleTree:

    def __init__(self, leaves):
        self.leaves = leaves
        self.nodes = []
        self._create_tree()

    def _create_tree(self):
        if len(self.leaves) == 0:
            return

        if len(self.leaves) == 1:
            self.nodes = self.leaves
            return

        parent_level = []
        for i in range(0, len(self.leaves), 2):
            left = self.leaves[i]
            if i + 1 < len(self.leaves):
                right = self.leaves[i + 1]
                parent = _hash(left + right)
            else:
                parent = _hash(left + left)
            parent_level.append(parent)

        self.leaves = parent_level
        self.nodes = parent_level + self.nodes
        self._create_tree()

    def root(self):
        if not self.nodes:
            return None
        return self.nodes[-1]