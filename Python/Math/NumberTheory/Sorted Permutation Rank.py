"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' :
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
"""

class Solution:

    # Return the rank of given string from sorted permutation of that string
    def rankPermutation(self, string):
        n, rank, i = len(string), 1, 0
        total_permutaion = self.fact(n)  # Total number of permutation
        while i < n:
            total_permutaion = total_permutaion//(n-i)
            count = self.smallComb(string, i, n-1)
            rank = rank + count*total_permutaion
            i+= 1
        return rank % 1000003
    # Counts the number of small element from string[start] in right
    def smallComb(self, string, start, end):
        count, i = 0, start+1
        while i <= end:
            if string[i] < string[start]:
                count += 1
            i+=1
        return count
    # Counts factorial of a number k
    def fact(self, k):
        f, i = 1, 1
        while i <k+1:
            f *= i
            i+=1
        return f
    # Space : O(n) # Time: O(n*n)
    def method_02(self, string):
        arr, n = list(string), len(string)
        sorted_arr = sorted(arr)
        rank, i, j = 1, 0, 0
        while i < n and j < len(sorted_arr):
            if sorted_arr[i] != arr[j]:
                rank += self.fact(len(sorted_arr)-1)
                i+= 1
            if sorted_arr[i] == arr[j]:
                del sorted_arr[i]
                j+= 1
                i = 0
        return rank%1000003





s = Solution()
print(s.rankPermutation("VIEW"))
print(s.method_02("VIEW"))
