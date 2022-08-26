class Node:

    def __init__(self, obj):
        self._obj = obj
        self._next_node = None

    @property
    def obj(self):
        return self._obj

    @obj.setter
    def obj(self, val):
        self._obj = val

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        format_str = '[{}]'
        list_str = ', '.join(map(str, self))
        return format_str.format(list_str)

    def __iter__(self):
        iter_obj = self.head
        while iter_obj:
            yield iter_obj.obj
            iter_obj = iter_obj.next_node

    def __add__(self, other):
        new_list = LinkedList()
        new_list.extend(self)
        new_list.extend(other)
        return new_list

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node: Node):
        self._head = node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node: Node):
        self._tail = node

    def append(self, obj):
        node = Node(obj)
        if not self.head:
            self.head = node
            self.head.next_node = None
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node
            node.next_node = None
        self._size += 1

    def extend(self, lst):
        for x in lst:
            self.append(x)


if __name__ == '__main__':
    llist = LinkedList()
    llist.extend([1, 2, 3, 4])

    llist2 = LinkedList()
    llist2.extend([5, 6, 7])

    llist3 = LinkedList()
    llist3.extend([12, 21, 32])

    new_list = llist + llist2 + llist3

    print(llist)
    print(llist2)
    print(new_list)
    print(len(new_list))
