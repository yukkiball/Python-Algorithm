def bubble_sort(listunsort):
    """冒泡排序O(N^2)"""

    """低效版本"""
    # for j in range(len(listunsort)):
    #     for i in range(len(listunsort) - 1):
    #         if listunsort[i] > listunsort[i + 1]:
    #             listunsort[i], listunsort[i + 1] = listunsort[i + 1], listunsort[i]
    # return listunsort

    """高效版本"""
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(listunsort) - 1):
            if listunsort[i] > listunsort[i + 1]:
                listunsort[i], listunsort[i + 1] = listunsort[i + 1], listunsort[i]
                sorted = False


#测试
l1 = [5, 3, 1, 2, 6]
bubble_sort(l1)
print(l1)