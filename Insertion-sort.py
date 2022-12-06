from re import U


def insertion_sort(unsorted_arr):
    for i in range(1,len(unsorted_arr)):
        key=unsorted_arr[i]
        j=i-1
        while(j>=0 and unsorted_arr[j]>key):
            unsorted_arr[j+1]=unsorted_arr[j]
            j=j-1
        unsorted_arr[j+1]=key
    return unsorted_arr

unsorted_arr=[5,1,3,7,8,2,0,6]
print(insertion_sort(unsorted_arr))
