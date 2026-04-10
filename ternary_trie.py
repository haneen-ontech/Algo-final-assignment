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

    def insert(self, word):
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, i):
        char = word[i]

        if node is None:
            node = TernaryNode(char)

        if char < node.char:
            node.left = self._insert(node.left, word, i)
        elif char > node.char:
            node.right = self._insert(node.right, word, i)
        else:
            if i + 1 < len(word):
                node.middle = self._insert(node.middle, word, i + 1)
            else:
                node.is_end = True

        return node

    def _search(self, node, prefix, i):
        if node is None:
            return None

        char = prefix[i]

        if char < node.char:
            return self._search(node.left, prefix, i)
        elif char > node.char:
            return self._search(node.right, prefix, i)
        else:
            if i == len(prefix) - 1:
                return node
            return self._search(node.middle, prefix, i + 1)

    def _collect(self, node, prefix, results):
        if node is None:
            return

        self._collect(node.left, prefix, results)

        if node.is_end:
            results.append(prefix + node.char)

        self._collect(node.middle, prefix + node.char, results)
        self._collect(node.right, prefix, results)

    def autocomplete(self, prefix):
        results = []
        node = self._search(self.root, prefix, 0)

        if node is None:
            return results

        if node.is_end:
            results.append(prefix)

        self._collect(node.middle, prefix, results)
        return results


# 🔹 MAIN PROGRAM
tst = TernaryTrie()

while True:
    print("\nChoose an option:")
    print("1. Insert a word into Ternary Trie")
    print("2. Search (Autocomplete)")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        word = input("Enter word: ")
        tst.insert(word)
        print("Word inserted!")

    elif choice == "2":
        prefix = input("Enter prefix: ")
        results = tst.autocomplete(prefix)

        if results:
            print("Suggestions:", results)
        else:
            print("No matching words found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")