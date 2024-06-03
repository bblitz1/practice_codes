
def smallest(a):
    current_smallest = a[0] 
    smallest_index = 0
    for ii in range(len(a)-1):
        if current_smallest > a[ii+1]:
            current_smallest = a[ii+1]
            smallest_index = ii + 1
    return (smallest_index, current_smallest)  

a = [12,1,6,7,9,2,11,46,10,38]
sorted_list = []
for ii in range(len(a)):
    smallest_index, smallest_num = smallest(a)
    sorted_list.append(smallest_num)
    a.pop(smallest_index)
print(sorted_list)

    
