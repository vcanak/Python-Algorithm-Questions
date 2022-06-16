def dest_city(paths)->str:
    out_count = {}
    for path in paths:
        city_a, city_b = path
        out_count[city_a] = out_count.get(city_a,0) + 1
        out_count[city_b] = out_count.get(city_b,0)
    
    for city in out_count:
        if out_count[city]==0:
            return city
print(dest_city( [ ["London","New York"], ["New York","Lima"], ["Lima","Sao Paolo"] ]  ))

def dest_cityv2(paths)->str:
    city_a,city_b = map(set,zip(*paths))
    print(map(set,zip(*paths)))
    return (city_b - city_a).pop()
print(dest_cityv2( [ ["London","New York"], ["New York","Lima"], ["Lima","Sao Paolo"] ]  ))