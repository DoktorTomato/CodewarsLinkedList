'''
Solution for "Linked Lists - Move Node" problem
'''

class Node:
    def __init__(self, data, next_data=None):
        self.data = data
        self.next = next_data

class Context:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def push(head, data):
    '''
    This function pushes new data to the given head
    '''
    if head is None:
        return Node(data)
    return Node(data, head)

def build_one_two_three():
    '''
    Creates a linked list like 1 -> 2 -> 3 -> None
    '''
    return Node(1, Node(2, Node(3)))

def move_node(source, dest):
    if source is None:
        raise ValueError
    new_source = source.next
    new_dest = Node(source.data, dest)
    return Context(new_source, new_dest)
