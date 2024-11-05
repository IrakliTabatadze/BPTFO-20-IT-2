class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top_node = None
        self.length = 0

    def empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1

    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            raise IndexError('Stack is empty')


stack = Stack()
# print(stack.empty())
# print(stack.size())

stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)
# print(stack.empty())
# print(stack.size())


print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
# print(stack.empty())
# print(stack.size())
