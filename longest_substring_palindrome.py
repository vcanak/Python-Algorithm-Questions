""" 
Given a string s, return the longest palindromic substring in s.
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""
def longestPalindrome(s: str) -> str:
        longest = ""
        def findLongest(s, left, right):
            while left>=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        
        for i in range(len(s)):
            s1 = findLongest(s, i, i)
            if len(s1) > len(longest): 
                longest = s1
            
            s2 = findLongest(s, i, i+1)
            if len(s2) > len(longest): 
                longest = s2
                
        return longest
s = "abb"
s="ac"
s = "babad"
#print(s[0:1])
print(longestPalindrome(s))