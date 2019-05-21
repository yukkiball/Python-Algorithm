def Qucik3_way(listunsort, lo, hi):
    """三路快排"""
    if lo >= hi:
        return
    lt = lo; i = lo + 1; gt = hi    #三指针维护小于、等于、大于区域
    mid = listunsort[lo]
    while i <= gt:
        if listunsort[i] < mid:
            listunsort[i], listunsort[lt] = listunsort[lt], listunsort[i]
            i += 1
            lt += 1
        elif listunsort[i] > mid:
            listunsort[i], listunsort[gt] = listunsort[gt], listunsort[i]
            gt -= 1
        else:
            i += 1
    Qucik3_way(listunsort, lo, lt - 1)
    Qucik3_way(listunsort, gt + 1, hi)

#测试
l1 = [5, 3, 1, 2, 6, 8, 6]
Qucik3_way(l1, 0, len(l1) - 1)
print(l1)