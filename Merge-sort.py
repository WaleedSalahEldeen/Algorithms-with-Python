def merge(arr, a, b, c):
	nod1 = b - a + 1
	mod2 = c - b
	L = [0] * nod1 #create list with a number of nod1 elements 
	R = [0] * mod2
	for i in range(0, nod1):
		L[i] = arr[a + i]
	for j in range(0, mod2):
		R[j] = arr[b + 1 + j]
	i = j = 0		
	k = a	
	while i < nod1 and j < mod2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < nod1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < mod2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, a, b):
	if a < b:
		m = a+(b-a)//2
		mergeSort(arr, a, m)
		mergeSort(arr, m+1, b)
		merge(arr, a, m, b)


arr = [5,6,8,2,5,1,0]

mergeSort(arr, 0, len(arr)-1)



