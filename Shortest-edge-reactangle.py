
"""
You are given an array rectangles where rectangles[i] = [li wi] rectangle of length li and width wi

You can cut the ith rectangle to from square with a side length of k if both k<=li and k<=wi

Return the number of rectangles that can make square with a side length of maxLen

Example:
Input : rectangles = [[5,8],[3,9],[5,12],[16,5]]
Output: 3
Explanation : The largest squares you can get from each rectangle are of lengths. [5,3,5,5]
The largest possible is of length 5, and you can get it out of 3 rectangles
"""
def squares(rectangles):
    cut_lengths=[]
    for rec in rectangles:
        cut_lengths.append(min(rec))
    maxval= max(set(cut_lengths), key = cut_lengths.count)
    return cut_lengths.count(maxval)

print(squares([[5,8],[3,9],[5,12],[16,5]]))