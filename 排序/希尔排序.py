def Shell_sort(listunsort):
    """希尔排序O(N^(1.3-2)"""
    h = 1
    while h < len(listunsort) // 3:
        h = h * 3 + 1   #使用序列(3^k - 1) // 2
    while h >= 1:
        for i in range(h, len(listunsort)):
            for j in range(i, h - 1, -h):
                if listunsort[j] < listunsort[j - h]:
                    listunsort[j], listunsort[j - h] = listunsort[j - h], listunsort[j] #h数组有序
        h //= 3


#测试
l1 = [5, 3, 1, 2, 6]
Shell_sort(l1)
print(l1)
