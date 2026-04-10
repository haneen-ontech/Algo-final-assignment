# standard trie

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

    # DFS to collect words
    def _collect(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)

        for char in node.children:
            self._collect(node.children[char], prefix + char, results)

    # Autocomplete
    def autocomplete(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []
        self._collect(node, prefix, results)
        return results


# 🔹 MAIN PROGRAM (USER CONTROLS EVERYTHING)
trie = Trie()

while True:
    print("\nChoose an option:")
    print("1. Insert a word into Trie")
    print("2. Search (Autocomplete)")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        word = input("Enter word: ")
        trie.insert(word)
        print("Word inserted!")

    elif choice == "2":
        prefix = input("Enter prefix: ")
        results = trie.autocomplete(prefix)

        if results:
            print("Suggestions:", results)
        else:
            print("No matching words found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")