def search_rec(list, x, lo, hi):
    """递归版二分查找返回小于等于该元素的最大秩"""
    if lo > hi:
        return lo - 1
    mid = (lo + hi) // 2
    # if list[mid] > x:
    #     return search_rec(list, x, lo, mid - 1)
    # elif list[mid] < x:
    #     return search_rec(list, x, mid + 1, hi)
    # else:
    #     return mid
    if list[mid] > x:
        return search_rec(list, x, lo, mid - 1)
    else:
        return search_rec(list, x, mid + 1, hi)

def search_iter(list, x, lo, hi):
    """二分查找迭代版返回小于等于该元素的最大秩"""
    while lo <= hi:
        mid = (lo + hi) >> 1
        # if list[mid] < x:
        #     lo = mid + 1
        # elif list[mid] > x:
        #     hi = mid - 1
        # else:
        #     return mid
        if list[mid] > x:
            hi = mid - 1

        else:
            lo = mid + 1

    return lo - 1


#测试
l1 = [1, 3, 4, 5, 6, 7]
print(search_rec(l1, 7, 0, len(l1) - 1))
print(search_iter(l1, 3, 0, len(l1) - 1))
