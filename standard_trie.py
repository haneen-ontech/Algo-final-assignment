# TRIE DATA STRUCTURE

# Node class for Trie
class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        # Key = character, Value = TrieNode
        self.children = {}
        
        # Boolean flag to mark end of a word
        self.is_end = False


# Trie class
class Trie:
    def __init__(self):
        # Root node (empty node)
        self.root = TrieNode()

    # Insert a word into trie
    def insert(self, word):
        node = self.root
        
        # Loop through each character in the word
        for char in word:
            # If character not present, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            
            # Move to the next node
            node = node.children[char]
        
        # Mark the end of the word
        node.is_end = True

    # DFS helper to collect words
    def _collect(self, node, prefix, results):
        # If current node marks end of a word, store it
        if node.is_end:
            results.append(prefix)

        # Recursively traverse all children
        for char in node.children:
            self._collect(node.children[char], prefix + char, results)

    # Autocomplete function
    def autocomplete(self, prefix):
        node = self.root

        # Traverse Trie using given prefix
        for char in prefix:
            if char not in node.children:
                return []  # No match found
            node = node.children[char]

        # Collect all words starting from this prefix
        results = []
        self._collect(node, prefix, results)
        return results

    # Display Trie
    def display(self):
        print("\nTrie Structure:")
        self._display_helper(self.root, "")

    def _display_helper(self, node, prefix):
        # If it's a complete word, print it
        if node.is_end:
            print(prefix)

        # Recursively print all children
        for char in node.children:
            self._display_helper(node.children[char], prefix + char)


# Main program for user interaction

# Create Trie object
trie = Trie()

while True:
    print("\nChoose an option:")
    print("1. Insert a word into Trie")
    print("2. Search (Autocomplete)")
    print("3. View Trie (All Words)")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Insert a word
    if choice == "1":
        word = input("Enter word: ")
        trie.insert(word)
        print("Word inserted!")

    # Autocomplete search
    elif choice == "2":
        prefix = input("Enter prefix: ")
        results = trie.autocomplete(prefix)

        if results:
            print("Suggestions:", results)
        else:
            print("No matching words found.")

    # Display trie contents
    elif choice == "3":
        trie.display()

    # Exit program
    elif choice == "4":
        print("Goodbye!")
        break

    # Invalid input
    else:
        print("Invalid choice.")