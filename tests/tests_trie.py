import unittest
from typing import List
from solution.trie import TrieNode, Trie


class TestCasesTrie(unittest.TestCase):
    def insert_input_word_is_none_return_nothing(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = None

        # Act & Assert
        trie.insert(input_word)
    
    def insert_input_word_is_empty_return_nothing(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = ""

        # Act & Assert
        trie.insert(input_word)

    def insert_input_word_is_fine_return_nothing(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = "hello"

        # Act & Assert
        trie.insert(input_word)
    
    def insert_input_word_is_not_str_return_nothing(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: int = 123

        # Act & Assert
        self.assertRaises(TypeError, trie.insert, input_word)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def find_input_word_is_none_return_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = None

        # Act
        result: TrieNode = trie.find(input_word)

        # Assert
        self.assertIsNone(result)
    
    def find_input_word_is_empty_return_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = ""

        # Act
        result: TrieNode = trie.find(input_word)

        # Assert
        self.assertIsNone(result)

    def find_input_word_is_not_str_return_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = 123

        # Act & Assert
        self.assertRaises(TypeError, trie.find, input_word)

    def find_input_word_is_fine_search_for_prefix_that_exists_return_trie_node(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = "hello"
        prefix: str = "hel"

        # Act
        trie.insert(input_word)
        result: TrieNode = trie.find(prefix)

        # Assert
        self.assertIsInstance(result, TrieNode)

    def find_input_word_is_fine_search_for_prefix_that_not_exists_return_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = "hello"
        prefix: str = "gel"

        # Act
        trie.insert(input_word)
        result: TrieNode = trie.find(prefix)

        # Assert
        self.assertIsNone(result)
    
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def suffixes_prefix_is_none_return_empty_list(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = "hello"
        prefix: str = None

        # Act
        trie.insert(input_word)
        result: TrieNode = trie.suffixes(prefix)

        # Assert
        self.assertFalse(result)
    
    def suffixes_prefix_is_empty_return_empty_list(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = "hello"
        prefix: str = ""

        # Act
        trie.insert(input_word)
        result: TrieNode = trie.suffixes(prefix)

        # Assert
        self.assertFalse(result)

    def suffixes_prefix_not_in_trie_return_empty_list(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        input_word: str = "hello"
        prefix: str = "test"

        # Act
        trie.insert(input_word)
        result: TrieNode = trie.suffixes(prefix)

        # Assert
        self.assertFalse(result)
    
    def suffixes_empty_trie_return_empty_list(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        prefix: str = "test"

        # Act
        result: TrieNode = trie.suffixes(prefix)

        # Assert
        self.assertFalse(result)
        
    def suffixes_multiple_characters_in_trie_return_list_with_suffixes(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        word_list: List[str] = [
            "f", "fun", "function", "factory", "factories",
            "he", "hello", "hella", "hellalo"
        ]
        for word in word_list:
            trie.insert(word)

        # Act
        prefix_0: str = "f"
        prefix_1: str = "fu"
        prefix_2: str = "fact"
        prefix_3: str = "factories"
        prefix_4: str = "h"
        prefix_5: str = "he"
        prefix_6: str = "hel"
        prefix_7: str = "hella"

        result_0: set = trie.suffixes(prefix_0)
        result_1: set = trie.suffixes(prefix_1)
        result_2: set = trie.suffixes(prefix_2)
        result_3: set = trie.suffixes(prefix_3)
        result_4: set = trie.suffixes(prefix_4)
        result_5: set = trie.suffixes(prefix_5)
        result_6: set = trie.suffixes(prefix_6)
        result_7: set = trie.suffixes(prefix_7)

        # Assert
        self.assertSetEqual(result_0, {"actory", "un", "actories", "unction"})
        self.assertSetEqual(result_1, {"n", "nction"})
        self.assertSetEqual(result_2, {"ories", "ory"})
        self.assertSetEqual(result_3, set())
        self.assertSetEqual(result_4, {"e", "ello", "ella", "ellalo"})
        self.assertSetEqual(result_5, {"llalo", "llo", "lla"})
        self.assertSetEqual(result_6, {"lo", "lalo", "la"})
        self.assertSetEqual(result_7, {"lo"})