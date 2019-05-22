class MinPQ:
    """优先级队列(最小的在队首)"""
    def __init__(self, list):
        self.list = list
        #建堆(从下往上下沉)
        for i in range(len(list) - 1, -1, -1):
            self.sink(i)

    #下沉
    def sink(self, rank):
        while 2 * rank + 1 < len(self.list):
            j = 2 * rank + 1
            if j < len(self.list) - 1 and self.list[j] > self.list[j + 1]:
                j += 1
            if self.list[rank] < self.list[j]:
                break
            self.list[rank], self.list[j] = self.list[j], self.list[rank]
            rank = j

    #上浮
    def swim(self, rank):
        while rank > 0 and self.list[(rank - 1) // 2] > self.list[rank]:
            self.list[rank], self.list[(rank - 1) // 2] = self.list[(rank - 1) // 2], self.list[rank]
            rank = (rank - 1) // 2

    #插入
    def insert(self, ele):
        self.list.append(ele)
        self.swim(len(self.list) - 1)


    #删除最小
    def delmin(self):
        min = self.list[0]
        self.list[0], self.list[-1] = self.list[-1], self.list[0]
        self.list.pop()
        self.sink(0)
        return min

#测试
l1 = [5, 3, 1, 2, 6, 8, 6]
pq = MinPQ(l1)
print(pq.list)
pq.delmin()
print(pq.list)
pq.insert(0)
print(pq.list)
pq.insert(1)
print(pq.list)
while pq.list:
    print(pq.delmin())