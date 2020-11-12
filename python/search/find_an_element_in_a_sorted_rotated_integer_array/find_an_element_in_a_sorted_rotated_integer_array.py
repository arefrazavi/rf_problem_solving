# https://practice.geeksforgeeks.org/problems/finding-number2406/1

# User function Template for python3
class Solution:

    def findNumber(self, arr, n, k):
        mid_index = len(arr) // 2
        k_position = -1
        if arr[mid_index] == k:
            k_position = mid_index
        elif arr[mid_index] < k:
            k_position = self.findNumber(arr[0:mid_index], n // 2, k)
        else:
            k_position = self.findNumber(arr[mid_index + 1:], n // 2, k)

        return k_position


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.findNumber(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
