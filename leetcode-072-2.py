class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        short_word, long_word = min(word1, word2, key=len), max(word1, word2, key=len)

        short_len = len(short_word)
        long_len = len(long_word)

        complete_layer = [i for i in range(short_len + 1)]
        layer = []
        print(complete_layer)

        for i in range(1, long_len + 1):
            layer = [0] * (short_len + 1) 
            layer[0] = i
            for j in range(1, short_len + 1):
                if (short_word[-j] == long_word[-i]):
                    layer[j] = complete_layer[j-1]
                else:
                    layer[j] = 1 + min(layer[j-1], complete_layer[j-1], complete_layer[j])
            complete_layer = layer
            print(complete_layer)
        return complete_layer[-1]
solution = Solution()
print(solution.minDistance("horse", "ros"))