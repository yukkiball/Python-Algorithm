def merge_sort(listunsort, lo, hi):
    """归并排序O(NlogN)"""
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    merge_sort(listunsort, lo, mid)
    merge_sort(listunsort, mid + 1, hi)
    merge(listunsort, lo, mid, hi)


#自底向上的归并排序
def merge_sort_2(listunsort):
    sz = 1
    while sz < len(listunsort):    #子数组大小
        for lo in range(0, len(listunsort) - sz, 2 * sz):  #子数组起始索引
            merge(listunsort, lo, lo + sz - 1, min(lo + 2 * sz -1, len(listunsort) - 1))
        sz += sz

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
# merge_sort(l1, 0, len(l1) - 1)
merge_sort_2(l1)
print(l1)