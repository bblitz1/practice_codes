list = [1,6,7,9,2,11,46,10,38]
print("min:", min(list))
print("max:", max(list))

def smallest(list):
    small = min(list)
    for ii in list:
        if ii < small:
            small = ii
    return small
print("smallest is", smallest(list))

def largest(list):
    large = max(list)
    for ii in list:
        if ii > large:
            large = ii
        return large
print("largest is", largest(list))
