

def smaller_than_current(nums):
        result = {}
       
        for index, number in enumerate(sorted(nums)):
            if number not in result:
                result[number] = index
       
        return [result[n] for n in nums]

print(smaller_than_current([8,1,2,2,3]))