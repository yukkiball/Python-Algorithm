#基于MAXPQ的堆排序
def swim_max(listunsort, rank):
    """上浮操作"""
    while rank > 0 and listunsort[(rank - 1) // 2] < listunsort[rank]:
        listunsort[rank], listunsort[(rank - 1) // 2] = listunsort[(rank - 1) // 2], listunsort[rank]
        rank = (rank - 1) // 2




def sink_max(listunsort, rank, length):
    """下沉操作"""

    while 2 * rank + 1 < length:
        j = 2 * rank + 1
        if j < length - 1 and listunsort[j] < listunsort[j + 1]:
             j += 1
        if not listunsort[j] > listunsort[rank]:
            break
        listunsort[j], listunsort[rank] = listunsort[rank], listunsort[j]
        rank = j

def heap_sort_max(listunsort):
    """堆排序O(NlogN)"""
    N = len(listunsort)
    for i in range(len(listunsort) - 1, -1, -1):
        sink_max(listunsort, i, len(listunsort))

    while N > 0:
        listunsort[0], listunsort[N - 1] = listunsort[N - 1], listunsort[0]
        N -= 1
        sink_max(listunsort, 0, N)


#测试
l1 = [5, 3, 1, 2, 6, 8, 6]
heap_sort_max(l1)
print(l1)


#基于MINPQ的堆排序
def sink_min(listunsort, rank, length):
    """下沉"""
    while 2 * rank + 1 < length:
        j = 2 * rank + 1
        if j < length - 1 and listunsort[j] > listunsort[j + 1]:
            j += 1
        listunsort[rank], listunsort[j] = listunsort[j], listunsort[rank]
        rank = j

def heap_sort_min(listunsort):
    N = len(listunsort)
    #建堆
    for i in range(N - 1, -1, -1):
        sink_min(listunsort, i, N)

    for i in range(1, len(listunsort)):
        N -= 1
        sink_min(listunsort, i, N)

#测试
l2 = [7, 3, 1, 0, 9, 8, 6]
heap_sort_max(l2)
print(l2)
