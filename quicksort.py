# 链表相关类
# 节点类


class Node:
    def __init__(self, element=None, pointer=None):
        self.element = element
        self.pointer = pointer


# 单链表类


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            return self.head

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            answer = self.head
            self.head = self.head.pointer
            self.size = self.size - 1
            if self.is_empty():
                self.tail = None
            return answer

    def enqueue(self, e):
        newest = Node(e, None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.pointer = newest
        self.tail = newest
        self.size = self.size + 1

    def __add__(self, other):
        if not other:
            return self
        self.tail.pointer = other.head
        self.tail = other.tail
        return self


# 准备一个单链表
li = LinkedQueue()
li.enqueue(1000)
li.enqueue(10010)
li.enqueue(200)
li.enqueue(1)
li.enqueue(1)
li.enqueue(1)
li.enqueue(1)
li.enqueue(1)
li.enqueue(1)
li.enqueue(1)
li.enqueue(1)
li.enqueue(1)
li.enqueue(6)
li.enqueue(9)
li.enqueue(9)
li.enqueue(100)
li.enqueue(10000)
li.enqueue(19)
li.enqueue(11)
li.enqueue(13)
li.enqueue(120)
li.enqueue(12)
li.enqueue(12)
li.enqueue(90)


# 排序函数
def quickSort(L, pivot):
    if L.size == 1:
        return L
    small = LinkedQueue()
    big = LinkedQueue()
    equal = LinkedQueue()
    obj = L.head
    while obj:
        if obj.element < pivot.element:
            small.enqueue(obj.element)
        elif obj.element > pivot.element:
            big.enqueue(obj.element)
        elif obj.element == pivot.element:
            equal.enqueue(obj.element)
        obj = obj.pointer
    if (small.size == 0) and (big.size == 0):
        return equal
    elif small.size == 0:
        return equal + quickSort(big, big.first())
    elif big.size == 0:
        return quickSort(small, small.first()) + equal
    else:
        return quickSort(small, small.first()) + equal + quickSort(big, big.first())


# 调用排序函数：
output = quickSort(li, li.head)
# 打印内存位置
print(output)

# 打印排序好的表
p = output.head
while p:
    print(p.element, end=' ')
    p = p.pointer
