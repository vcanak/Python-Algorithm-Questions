"""
Question
Paramenters:

array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 USD is equal to 0.77 GBP
an array containing a 'from' currency and a 'to' currency
Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency.
Your return value should be a number.

Example:
You are given the following parameters:

Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
To/From currency ['GBP', 'AUD']
Find the rate for the 'To/From' curency. In this case, the correct result is 1.89.
"""
from collections import defaultdict,deque


def getRatio(start, end, data):
    currency_table = defaultdict(list)
    
    for node in data:
        currency_table[node[0]].append([node[1],node[2]])
        currency_table[node[1]].append([node[0], 1.0/node[2]])
        
    queue = deque()
    queue.append((start,1.0))
    visited = set()
    while queue:
        current_node, ratio = queue.popleft()
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node in currency_table:
            values = currency_table.get(current_node)
            next = {}
            
            for val in values:
                next[val[0]] = val[1]
            
            for key in next:
                if key not in visited:
                    if key == end:
                        return ratio * next[key]
                    queue.append((key,ratio*next[key]))
    return -1
            
#from ,to ,ratio
data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]
print(getRatio("GBP", "AUD", data))