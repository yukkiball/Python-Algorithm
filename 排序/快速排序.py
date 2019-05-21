import random
def quick_sort(listunsort, lo, hi):
    """快速排序"""
    if lo >= hi:
        return
    j = partition(listunsort, lo, hi )
    quick_sort(listunsort, lo, j - 1)
    quick_sort(listunsort, j + 1, hi)

def partition(listunsort, lo, hi):
    """寻找轴点"""
    rnd = random.randint(lo, hi)    #选择随机轴点
    listunsort[lo], listunsort[rnd] = listunsort[rnd], listunsort[lo]
    mid = listunsort[lo]
    while lo < hi:
        while lo < hi and listunsort[hi] >= mid:
            hi -= 1
        listunsort[lo] = listunsort[hi]

        while lo < hi and listunsort[lo] <= mid:
            lo += 1
        listunsort[hi] = listunsort[lo]

    listunsort[lo] = mid
    return lo

#测试
l1 = [5, 3, 1, 2, 6, 8, 6]
quick_sort(l1, 0, len(l1) - 1)
print(l1)