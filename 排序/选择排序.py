def selection_sort(listunsort):
    """选择排序O(N^2)"""
    for i in range(len(listunsort) - 1):
        min = i
        for j in range(i + 1, len(listunsort)):
            if listunsort[j] < listunsort[min]:
                min = j
        listunsort[i], listunsort[min] = listunsort[min], listunsort[i]
    return listunsort

l1 = [5, 3, 1, 2, 6]
print(selection_sort(l1))