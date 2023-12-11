def swap_max_min(arr):
    max_index=arr.index(max(arr))
    min_index=arr.index(min(arr))
    arr[max_index], arr[min_index]=arr[min_index], arr[max_index]
    return arr
arr=[2,5,3,78,1,6,9]
new_arr=swap_max_min(arr)
print(new_arr)
