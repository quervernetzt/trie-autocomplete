from collections import defaultdict


class TrieNode:
    def __init__(self: object) -> None:
        """Constructor.
        """

        self.children: defaultdict = defaultdict(TrieNode)
        self.is_word: bool = False


class Trie(object):
    def __init__(self: object) -> None:
        """Constructor.
        """
        self.root: TrieNode = TrieNode()

    def insert(self: object, word: str) -> None:
        """Add a word to the trie.

            Time Complexity = O(len(word))
            Space Complexity = O(len(word))

            Parameters
            ----------
            word : str, required
                The word to add.
        """

        if not word:
            return None
        if not isinstance(word, str):
            raise TypeError("Input word has to be of type str...")
        if len(word) == 0:
            return None

        current_node: TrieNode = self.root

        for char in word:
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self: object, prefix: str) -> TrieNode:
        """Find the Trie node that represents this prefix.

            Time Complexity = O(len(prefix))
            Space Complexity = O(1)

            Parameters
            ----------
            prefix : str, required
                The prefix to find the Trie node for.

            Returns
            ----------
            TrieNode
                Returns the Trie node for the prefix.
        """
        if not prefix:
            return None
        if not isinstance(prefix, str):
            raise TypeError("Input word has to be of type str...")
        if len(prefix) == 0:
            return None

        current_node: TrieNode = self.root

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None

        return current_node

    def suffixes(
            self: object,
            prefix: str) -> set:
        """Find all suffixes starting from a given Trie node that together with the prefix represented by the Trie node are a complete word.

            Time Complexity = O(len(prefix)) + O(<number of nodes in trie>)
            Space Complexity = O(<number of nodes in trie>)

            Parameters
            ----------
            prefix : str, required
                The prefix to find the Trie node for.

            Returns
            ----------
            set
                Returns a set with the existing suffixes.
        """

        if not prefix or len(prefix) == 0:
            return []

        prefix_node: TrieNode = self.find(prefix)
        if not prefix_node:
            return []

        suffixes: set = set()

        def suffixes_helper(
                current_node: TrieNode,
                suffix: str = "") -> None:

            if current_node.is_word:
                if suffix != "":
                    suffixes.add(suffix)

            for char in current_node.children:
                next_node: TrieNode = current_node.children[char]
                suffixes_helper(next_node, suffix + char)

        suffixes_helper(prefix_node)

        return suffixes
