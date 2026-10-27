class Solution:
    def kthCharacter(self, k: int) -> str:
        def word_extender( curr_word : str, size : int ) -> str:
            if size >= k :
                return curr_word[k-1]
            for i in range(size):
                curr_word += chr(ord(curr_word[i])+1)
            size *= 2
            return word_extender( curr_word, size )
        return word_extender( 'a', 1 )