""" 
Given a string s, find the length of the longest substring without repeating characters.

 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
def longest_sub_palindrome(s):      
        visited = ''
        longest = 0
		#1. for each character in s
        for char in s:
			#2. check if c is seen
            if char not in visited:
			#3. if not seen, add to seen list 
                visited+=char
            #4 if seen, slice seen list to previous c
            # for example, if c is 'a' and seen list is 'abc'
            # you will be slicing previous 'a'(seen.index(c)+1), thus seen list become 'bc'
            # then add the current 'a' bc + a, seenlist = 'bca'
            else:
                visited = visited[visited.index(char) + 1:] + char
            #5 check max length between current max with new length of seen
            longest = max(longest, len(visited))
        return longest

print(longest_sub_palindrome("abcabcbb"))