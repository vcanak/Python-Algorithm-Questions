"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11

"""
def minimumTotal(triangle) -> int:
    n = len(triangle)
    cur_row, next_row = [0]*n, triangle[n-1]        
    for level in range(n-2,-1,-1):
        for i in range(level+1):
            cur_row[i] = triangle[level][i] + min(next_row[i], next_row[i+1])
        cur_row, next_row = next_row, cur_row
    return next_row[0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))