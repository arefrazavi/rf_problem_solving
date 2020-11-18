# https://leetcode.com/problems/implement-trie-prefix-tree
# Data structure for typeahead (search-as-you-go) search

class TrieNode:

    def __init__(self, data=None):
        self.data = data
        # Children can be as many as alphabet nodes_count.
        self.children = {}
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        # Insert each char in tree if it doesn't exit.
        for char in word:
            if not current_node.children.get(char):
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]

        # Mark the last node as the end of the word
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        for char in word[:-1]:
            if not current_node.children.get(char):
                return False
            current_node = current_node.children[char]

        if not current_node.children.get(word[-1]):
            return False
        else:
            return current_node.children[word[-1]].is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for char in prefix:
            if not current_node.children.get(char):
                return False
            current_node = current_node.children[char]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)