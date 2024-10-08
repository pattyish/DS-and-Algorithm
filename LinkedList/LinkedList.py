class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# new_node = Node(10)
# print(new_node)
# Create linked list without node


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        tem_node = self.head
        result = ''
        while tem_node is not None:
            result += str(tem_node.value)
            if tem_node.next is not None:
                result += '->'
            tem_node = tem_node.next
        return result

    def append(self, value):
        n_node = Node(value)
        if self.head is None:  # of self.length == 0
            self.head = n_node
            self.tail = n_node
        else:
            self.tail.next = n_node
            self.tail = n_node
        self.length += 1

    def prepend(self, value):
        n_node = Node(value)
        if self.head is None:
            self.head = n_node
            self.tail = n_node
        else:
            n_node.next = self.head
            self.head = n_node
        self.length += 1

    def insert(self, index, value):
        n_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = n_node
            self.tail = n_node
        elif index == 0:
            n_node.next = self.head
            self.head = n_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            n_node.next = temp_node.next
            temp_node.next = n_node
        self.length += 1
        return True

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        return

    def search(self, target):
        current = self.head
        while current:  # same as while current is not None
            if current.value == target:
                return True
            current = current.next
        return False

    def searchIndexOfTarget(self, target):
        current = self.head
        index = 0
        while current:  # same as while current is not None
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    # get node by index

    def get(self, index):
        current = self.head
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        for _ in range(index):
            current = current.next
        return current

    # Update linked list by setting new number

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    # remove first element in linked list

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def removeByIndex(self, index):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index == -1:
            return self.pop()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


new_linked_list = LinkedList()
new_linked_list.append(30)
new_linked_list.prepend(5)
new_linked_list.prepend(15)

# Access value of first node

print(new_linked_list)
new_linked_list.insert(4, 0)
new_linked_list.insert(0, 9)
print(new_linked_list)
new_linked_list.traverse()
print(new_linked_list.search(50))
print(new_linked_list.searchIndexOfTarget(50))
print(new_linked_list.searchIndexOfTarget(40))
print(new_linked_list.get(2))
new_linked_list.set_value(0, 100)
print(new_linked_list)
print(new_linked_list.pop_first())
print(new_linked_list)
print(new_linked_list.pop())
print(new_linked_list)
print(new_linked_list.delete_all())
print(new_linked_list)
# Creating linked list with node
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
