def selection_sort(arr):
    n=len(arr)
    
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
                
        arr[i],arr[min_index]=arr[min_index],arr[i]
        
my_list=list(map(int,input("enter:").split()))
print("original list:",my_list)
selection_sort(my_list)
print()
print("sorted list:",my_list)