from random import randint
unsorted_list = [randint(1, 100) for i in range(13)]
element = randint(1, 100)


def buble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def binary_search(value, a):
    n = len(a)
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == value:
            print('Element found!!')
            return mid
        elif a[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    print('Element not found!!')


print(f'Unsorted list: {unsorted_list}')
sorted_list = buble_sort(unsorted_list)
print(f'Sorted list: {sorted_list}')
print(f'Element to find: {element}')
print(f'Element position: {binary_search(element, sorted_list)}')
