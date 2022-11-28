def selection_sort(A):
    n = len(A)
    swap_count = comp_count = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if A[min_idx] > A[j]:
                min_idx = j

            comp_count += 1
        if i != min_idx:
            A[i], A[min_idx] = A[min_idx], A[i]
            swap_count += 1
    print('The array after sorting : \n', A)
    print('Number of comparison : \n', comp_count)
    print('Number of swapping : \n', swap_count)


def bubble_sort(A):
    for i in range(num):
        swapped = False
        for j in range(0, num - i - 1):
           if arr[j] > arr[j + 1]:

               swapped = True
               break
        break
    return swapped


arr = []

num = int(input('Enter the number of elements in the list : '))
print('Enter the elements in the list : ')

for i in range(num):
    ele = int(input())
    arr.append(ele)

result = bubble_sort(arr)
if result == False:
    print('The entered array is already sorted : \n')
    print(arr)
    print('Number of comparison : ', num - 1)
    print('Number of swapping : ', 0)
else:
    selection_sort(arr)