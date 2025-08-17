class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Levenshtein's with only 2 layers at a time

        if (len(word1) > len(word2)):
            word2, word1 = word1, word2
        short_word, long_word = word1, word2
        
        short_len = len(short_word)
        long_len = len(long_word)

        complete_layer = [i for i in range(short_len + 1)]
        layer = []
        print(complete_layer)

        for i in range(1, long_len + 1):
            layer = [i]
            for j in range(1, short_len + 1):
                if (short_word[-j] == long_word[-i]):
                    layer.append(complete_layer[j-1])
                else:
                    layer.append(1 + min(layer[j-1], complete_layer[j-1], complete_layer[j]))
            complete_layer = layer
            print(complete_layer)
        return complete_layer[-1]
solution = Solution()
print(solution.minDistance("intention", "execution"))