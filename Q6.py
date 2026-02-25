def round_to_one(lst):
    return list(map(lambda x:round(x,1),lst))
print(round_to_one([3.14159,2.71828,1.61803]))
