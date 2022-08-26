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
        self._iter = self.head
        while self._iter:
            yield self._iter.obj
            self._iter = self._iter.next_node

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

    def append_list(self, lst):
        for x in lst:
            self.append(x)


if __name__ == '__main__':
    llist = LinkedList()
    llist.append_list([1, 2, 3, 4, 5, 6, 7])

    print(llist)

    l = list(map(lambda x: x * 2, llist))
    print(l)

