#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# The answer is guaranteed to fit in a 32-bit integer.


def get_decodings_count(encoded_string: str, alphabet_size: int = 26) -> int:
    """
    Get number of ways to decode the given string using dynamic programming.
    """
    encode_string_len = len(encoded_string)
    # string starting with 0 is not decodable.
    if not encode_string_len or encoded_string[0] == '0':
        return 0

    # decondings_count[i] store the number of ways to decode subtring encoded_string[:i].
    decodings_count = {0: 1, 1: 1}

    for i in range(2, encode_string_len + 1):
        decodings_count[i] = 0
        # If substring doesn't ends with 0, we can consider ith subtring as a single digit and decode the substring in all ways we could decode the encoded_string[:i-1].
        if encoded_string[i - 1] > '0':
            decodings_count[i] = decodings_count[i - 1]

        # If the substring ends with a two-digit number between 10 and 26, we can consider it as a two-digit number, decode the sutring in all ways we could decode the encoded_string[:i-2].
        if 10 <= int(encoded_string[i - 2:i]) <= alphabet_size:
            decodings_count[i] += decodings_count[i - 2]

    return decodings_count[encode_string_len]


if __name__ == '__main__':
    print('Enter an encoded string with only digits')
    encode_string = input()
    print(get_decodings_count(encode_string))
