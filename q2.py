

class Node:
    def __init__(self, element=None, pointer=None):
        self.element = element
        self.pointer = pointer


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



def test():
    # Prepare a linked list
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
    head = li.head

    def testPrint(output):
        while output:
            print(output.element, end=' ')
            output = output.pointer
    # RUn my program
    output = quickSort(head)
    # Print the output
    testPrint(output)
    print()
    print('The head of linked list is:', output, 'You can check it.')



def plt(li):
    a = li.head
    while a:
        print(a.element)
        a = a.pointer


def quickSort(head):
    def recurse(li, pivot):
        print("_____________This. start")
        print('pivot', pivot.element)
        if li.size == 1:
            print('ultimate returned', li.head.element)
            print("_____________This. ended")
            return li
        small = LinkedQueue()
        big = LinkedQueue()
        equal = LinkedQueue()
        obj = li.head
        n = 0
        # This is Partition
        while obj:
            if obj.element < pivot.element:
                small.enqueue(obj.element)
            elif obj.element > pivot.element:
                big.enqueue(obj.element)
            elif obj.element == pivot.element:
                n = n + 1
                equal.enqueue(obj.element)
            obj = obj.pointer

        print('small')
        plt(small)
        print('equal')
        plt(equal)
        print('big')
        plt(big)

        # This is Recursion
        if (small.size == 0) and (big.size == 0):
            print('back -00: equal')
            plt(equal)
            print('_________________End of this')
            return equal
        elif small.size == 0:
            print('back -01: equal and returned big')
            print('__equal')
            q = equal
            plt(q)
            print('_____big')
            p = recurse(big, big.first())
            plt(p)
            back = q + p
            print('back is')
            plt(back)
            print('_________________End of this')
            return back

        elif big.size == 0:
            print('back -10: equal and returned small')
            print('_____small')
            q = recurse(small, small.first())
            plt(q)
            print('__equal')

            p = equal
            plt(p)
            print('_____back')
            back = q + p
            plt(back)
            print('_________________End of this')
            return back
        else:
            print('back -11: equal and returned small and big')
            print('______small')
            q = recurse(small, small.first())
            plt(q)
            print('__equal')
            p = equal
            plt(p)
            print('______big')

            o = recurse(big, big.first())
            plt(o)
            print('_____back')
            back = q + p + o

            plt(back)
            print('_________________End of this')
            return back

    # This is initializer
    li = LinkedQueue()
    # Get a head
    pivot = head
    while head:
        li.enqueue(head.element)
        head = head.pointer
    # Start sorting
    rlist = recurse(li, pivot)
    # End of sorting
    print('Final ouput')
    plt(rlist)
    return rlist.head
    # Output


test()
