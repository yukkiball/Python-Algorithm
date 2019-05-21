def merge_sort(listunsort, lo, hi):
    """归并排序O(NlogN)"""
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    merge_sort(listunsort, lo, mid)
    merge_sort(listunsort, mid + 1, hi)
    merge(listunsort, lo, mid, hi)

def merge(listunsort, lo, mid, hi):
    """归并"""
    listcopy = listunsort[:]
    k = i = lo; j = mid + 1
    while i <= mid or j <= hi:
        if i <= mid and (j > hi or listcopy[i] < listcopy[j]):
            listunsort[k] = listcopy[i]
            i += 1
            k += 1
        if j <= hi and (i > mid or listcopy[j] <= listcopy[i]):
            listunsort[k] = listcopy[j]
            j += 1
            k += 1


#测试
l1 = [5, 3, 1, 2, 6, 8, 6]
merge_sort(l1, 0, len(l1) - 1)
print(l1)