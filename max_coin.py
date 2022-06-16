def max_coin(piles) ->int :
    piles.sort()
    res,n=0,len(piles)
    for i in range(len(piles)//3):
        res += piles[n-(i+1)*2]
    return res
def max_coinv2(A) -> int:
     #sum( sorted(piles)[len(piles) / 3::2] )
     return   sum(sorted(A)[len(A) // 3::2])
print(max_coin([2,4,1,2,7,8]))
print(max_coinv2([2,4,1,2,7,8]))