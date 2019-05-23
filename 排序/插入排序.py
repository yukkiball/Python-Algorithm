def insertion_sort(listunsort):
    """插入排序O(N^2)"""
    for i in range(1, len(listunsort)):
        """低效版"""
        # for j in range(i, 0, -1):
        #     if listunsort[j] < listunsort[j - 1]:
        #         listunsort[j - 1], listunsort[j] = listunsort[j], listunsort[j - 1]
        #     else:
        #         break
        """高效版(使用赋值)"""
        temp = listunsort[i]
        j = i
        while j > 0 and listunsort[j - 1] > temp:
            listunsort[j] = listunsort[j - 1]
            j -= 1
        listunsort[j] = temp


#测试
l1 = [5, 3, 1, 2, 6]
insertion_sort(l1)
print(l1)