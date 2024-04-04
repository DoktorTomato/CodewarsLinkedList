'''
This is a script that has a solutin for the problem "Linked Lists - Sorted Insert"
'''

class Node:
    '''
    Class that describes a node object
    '''
    def __init__(self, data, next_data=None):
        self.data = data
        self.next = next_data

def build_one_two_three():
    '''
    Creates a linked list like 1 -> 2 -> 3 -> None
    '''
    return Node(1, Node(2, Node(3)))

def sorted_insert(head, data):
    '''
    Function which inserts a node into the correct 
    location of a pre-sorted linked list which is sorted in ascending order
    '''
    if head is None:
        return Node(data)
    if head.data >= data or head.data is None:
        return Node(data, head)
    else:
        head.next = sorted_insert(head.next, data)
        return head
