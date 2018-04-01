
class LinkedListNode:
    data = None
    next = None

    def __init__(self, data, next):
        self.data = data
        self.next = next

    def set_next(self, next):
        self.next = next




linked_list = LinkedListNode(1, None)
start_node = linked_list

temp_node = LinkedListNode(2,None)
linked_list.set_next(temp_node)
linked_list = temp_node
temp_node = LinkedListNode(3,None)
linked_list.set_next(temp_node)


def print_linked_list(linked_list: LinkedListNode):
    node = linked_list
    while node:
        print(str(node.data), sep=' ', end=' ')
        node = node.next


print_linked_list(start_node)

print("\nChanging directions")


def reverse_linked_list(linked_list: LinkedListNode):
    if not linked_list:
        return

    def reverse_linked_list_recursion(start_node: LinkedListNode, prev_node: LinkedListNode,
                                      current_node: LinkedListNode):
        if current_node:
            start_node = current_node
        else:
            return start_node

        next_node = current_node.next
        current_node.set_next(prev_node)
        return reverse_linked_list_recursion(start_node, current_node, next_node)

    return reverse_linked_list_recursion(linked_list, None, linked_list)


print_linked_list(reverse_linked_list(start_node))


