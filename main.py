from typing import List
from tests.tests_trie import TestCasesTrie
from solution.trie import TrieNode, Trie

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    test_trie: TestCasesTrie = TestCasesTrie()

    test_trie.insert_input_word_is_none_return_nothing()
    test_trie.insert_input_word_is_empty_return_nothing()
    test_trie.insert_input_word_is_fine_return_nothing()
    test_trie.insert_input_word_is_not_str_return_nothing()

    test_trie.insert_input_word_is_fine_return_nothing()
    test_trie.find_input_word_is_empty_return_none()
    test_trie.find_input_word_is_not_str_return_none()
    test_trie.find_input_word_is_fine_search_for_prefix_that_exists_return_trie_node()
    test_trie.find_input_word_is_fine_search_for_prefix_that_not_exists_return_none()

    test_trie.suffixes_prefix_is_none_return_empty_list()
    test_trie.suffixes_prefix_is_empty_return_empty_list()
    test_trie.suffixes_prefix_not_in_trie_return_empty_list()
    test_trie.suffixes_empty_trie_return_empty_list()
    test_trie.suffixes_multiple_characters_in_trie_return_list_with_suffixes()

    ###################################
    # Demo
    ###################################
    trie: Trie = Trie()

    trie.insert("hello")
    trie.insert("hella")
    trie.insert("hellalo")

    suffixes_list: List[str] = trie.suffixes("h")
    print(suffixes_list) # {'ella', 'ellalo', 'ello'}