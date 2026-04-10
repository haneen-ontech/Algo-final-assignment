# TERNARY SEARCH TRIE 

# Node class for Ternary Trie
class TernaryNode:
    def __init__(self, char):
        # Character stored in this node
        self.char = char
        
        # Left child (characters < current char)
        self.left = None
        
        # Middle child (next character in word)
        self.middle = None
        
        # Right child (characters > current char)
        self.right = None
        
        # Marks end of a word
        self.is_end = False


# Ternary Trie class
class TernaryTrie:
    def __init__(self):
        # Root node starts as None
        self.root = None

    # Insert word into ternary trie
    def insert(self, word):
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, i):
        char = word[i]

        # Create node if it doesn't exist
        if node is None:
            node = TernaryNode(char)

        # Go left if character is smaller
        if char < node.char:
            node.left = self._insert(node.left, word, i)

        # Go right if character is larger
        elif char > node.char:
            node.right = self._insert(node.right, word, i)

        # Character matches
        else:
            # Move to next character in word
            if i + 1 < len(word):
                node.middle = self._insert(node.middle, word, i + 1)
            else:
                # End of word reached
                node.is_end = True

        return node

    # Search prefix (helper function)
    def _search(self, node, prefix, i):
        if node is None:
            return None

        char = prefix[i]

        # Traverse left
        if char < node.char:
            return self._search(node.left, prefix, i)

        # Traverse right
        elif char > node.char:
            return self._search(node.right, prefix, i)

        # Character matches
        else:
            # If last character of prefix, return node
            if i == len(prefix) - 1:
                return node
            
            # Continue searching in middle
            return self._search(node.middle, prefix, i + 1)

    # Collect words (DFS traversal)
    def _collect(self, node, prefix, results):
        if node is None:
            return

        # Traverse left subtree
        self._collect(node.left, prefix, results)

        # If node marks end of word, add it
        if node.is_end:
            results.append(prefix + node.char)

        # Traverse middle subtree (build word)
        self._collect(node.middle, prefix + node.char, results)

        # Traverse right subtree
        self._collect(node.right, prefix, results)

    # Autocomplete function
    def autocomplete(self, prefix):
        results = []

        # Find node corresponding to last char of prefix
        node = self._search(self.root, prefix, 0)

        if node is None:
            return results

        # If prefix itself is a word
        if node.is_end:
            results.append(prefix)

        # Collect all words below this node
        self._collect(node.middle, prefix, results)

        return results

    # Display all words of ternary tree
    def display(self):
        print("\nTernary Trie Structure:")
        self._display_helper(self.root, "")

    def _display_helper(self, node, prefix):
        if node is None:
            return

        # Traverse left
        self._display_helper(node.left, prefix)

        # If end of word, print it
        if node.is_end:
            print(prefix + node.char)

        # Traverse middle (build word)
        self._display_helper(node.middle, prefix + node.char)

        # Traverse right
        self._display_helper(node.right, prefix)


# Main program for user interaction

# Create Ternary Trie object
tst = TernaryTrie()

while True:
    print("\nChoose an option:")
    print("1. Insert a word into Ternary Trie")
    print("2. Search (Autocomplete)")
    print("3. View Trie (All Words)")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Insert word
    if choice == "1":
        word = input("Enter word: ")
        tst.insert(word)
        print("Word inserted!")

    # Autocomplete search
    elif choice == "2":
        prefix = input("Enter prefix: ")
        results = tst.autocomplete(prefix)

        if results:
            print("Suggestions:", results)
        else:
            print("No matching words found.")

    # =Display trie contents
    elif choice == "3":
        tst.display()

    # Exit program
    elif choice == "4":
        print("Goodbye!")
        break

    # Invalid input
    else:
        print("Invalid choice.")