# https://leetcode.com/problems/longest-common-subsequence/submissions/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcs_len_dict = {}
        lcs_len = self.find_lcs(text1, text2, 0, 0, lcs_len_dict)
        return lcs_len

    def find_lcs(self, text1: str, text2: str, i: int, j: int, lcs_len_dict: dict):
        if i >= len(text1) or j >= len(text2):
            return 0

        key = (i, j)
        if key in lcs_len_dict:
            return lcs_len_dict[key]

        if text1[i] == text2[j]:
            lcs_len_dict[key] = self.find_lcs(text1, text2, i + 1, j + 1, lcs_len_dict) + 1
        else:
            lcs_len_dict[key] = max(self.find_lcs(text1, text2, i + 1, j, lcs_len_dict),
                                    self.find_lcs(text1, text2, i, j + 1, lcs_len_dict))

        return lcs_len_dict[key]
