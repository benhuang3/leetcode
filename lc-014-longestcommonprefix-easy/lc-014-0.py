class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def findLastMatchingIndex():
            len_list = [len(i) for i in strs]
            for i in range(min(len_list)):
                c_i = strs[0][i]
                for str_j in strs:
                    if str_j[i] != c_i:
                        return i
            return min(len_list)

        return strs[0][0:findLastMatchingIndex()]
                


        