# classic trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert word
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    # Helper to collect words
    def _dfs(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)

        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)

    # Autocomplete
    def autocomplete(self, prefix):
        node = self.root

        # Traverse prefix
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        self._dfs(node, prefix, results)
        return results


# 🔹 Testing
words = ["Sample", "Samplers", "Same", "Sampling", "Summer", "Sad"]

trie = Trie()
for word in words:
    trie.insert(word)

# ternary trie

class TernaryNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.is_end = False


class TernaryTrie:
    def __init__(self):
        self.root = None

    # Insert word
    def insert(self, word):
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, index):
        char = word[index]

        if node is None:
            node = TernaryNode(char)

        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.middle = self._insert(node.middle, word, index + 1)
            else:
                node.is_end = True

        return node

    # Search prefix node
    def _search(self, node, prefix, index):
        if node is None:
            return None

        char = prefix[index]

        if char < node.char:
            return self._search(node.left, prefix, index)
        elif char > node.char:
            return self._search(node.right, prefix, index)
        else:
            if index == len(prefix) - 1:
                return node
            return self._search(node.middle, prefix, index + 1)

    # Collect words
    def _dfs(self, node, prefix, results):
        if node is None:
            return

        self._dfs(node.left, prefix, results)

        if node.is_end:
            results.append(prefix + node.char)

        self._dfs(node.middle, prefix + node.char, results)
        self._dfs(node.right, prefix, results)

    # Autocomplete
    def autocomplete(self, prefix):
        results = []
        node = self._search(self.root, prefix, 0)

        if node is None:
            return results

        if node.is_end:
            results.append(prefix)

        self._dfs(node.middle, prefix, results)
        return results


# 🔹 Testing
words = ["Sample", "Samplers", "Same", "Sampling", "Summer", "Sad"]

tst = TernaryTrie()
for word in words:
    tst.insert(word)

print(tst.autocomplete("Sam"))

print(trie.autocomplete("Sam"))
