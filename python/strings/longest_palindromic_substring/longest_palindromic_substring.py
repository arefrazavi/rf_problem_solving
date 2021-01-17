class Solution:
    def longestPalindrome(self, input_str: str) -> str:
        longest_palindrome = ''
        str_len = len(input_str)
        i = 0
        while i < str_len:
            palindrome = input_str[i]
            k = i + 1
            # Find a pivot string which all of its chars are equal to current char.
            while k < str_len and (input_str[i] == input_str[k]):
                palindrome += input_str[k]
                k += 1

            j = i - 1
            # Check right and left of pivot string to search for longer palindrome
            while j >= 0 and k < str_len and input_str[j] == input_str[k]:
                palindrome = input_str[j] + palindrome + input_str[k]
                j -= 1
                k += 1

            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome
            i += 1

        return longest_palindrome