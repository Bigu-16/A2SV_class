class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        merged_word1 = ""
        merged_word2 = ""
        if merged_word1.join(word1) == merged_word2.join(word2):
            return True
        return False