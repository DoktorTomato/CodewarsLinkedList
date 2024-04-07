'''
This script solves "Linked Lists - Alternating Split" problem from codewars
'''

class Node(object):
    def __init__(self, data=None, next_data=None):
        self.data = data
        self.next = next_data

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def insert_in_the_end(head, data):
    '''
    This function inserts data given in the end of the head node
    '''
    if head.next is None:
        head.next = Node(data)
    else:
        head = Node(head.data, insert_in_the_end(head.next, data))
    return head

def alternating_split(head):
    '''
    Function that takes one list and divides up its nodes to make two smaller lists
    '''
    if head is None or head.next is None:
        raise AttributeError
    res = Context(Node(), Node())
    first_ref = res.first
    second_ref = res.second
    current = head
    count = 1
    while current is not None:
        if count % 2 == 1:
            if count != 1:
                first_ref = insert_in_the_end(first_ref, current.data)
            else:
                first_ref.data = current.data
        elif count % 2 == 0:
            if count != 2:
                second_ref = insert_in_the_end(second_ref, current.data)
            else:
                second_ref.data = current.data
        current = current.next
        count += 1
    return res
