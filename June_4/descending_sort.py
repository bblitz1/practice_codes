def largest(a):
    current_largest = a[0] 
    largest_index = 0
    for ii in range(len(a)-1):
        if current_largest < a[ii+1]:
            current_largest = a[ii+1]
            largest_index = ii + 1 
    return (largest_index, current_largest)  

#a = [12,1,6,7,9,2,11,46,10,38]
def sort(a):
    sorted_list = []
    for ii in range(len(a)):
        largest_index, largest_num = largest(a)
        sorted_list.append(largest_num)
        a.pop(largest_index)
    return(sorted_list)

