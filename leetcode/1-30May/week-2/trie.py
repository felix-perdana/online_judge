#credit to: https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
#improved by replacing array with dictionary

class Trie:

    def __init__(self, c=""):
        """
        Initialize your data structure here.
        """
        self.char = c
        self.children = {}
        self.isWord = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for w in word:
            next = node.children.get(w)
            if next == None:
                newNode = Trie(w)
                node.children[w] = newNode
                node = newNode
            else:
                node = next
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for w in word:
            node = node.children.get(w)
            if node == None:
                return False

        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for w in prefix:
            node = node.children.get(w)
            if node == None:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
