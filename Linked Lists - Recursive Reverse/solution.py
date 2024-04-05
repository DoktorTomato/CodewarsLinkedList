'''
This is a script that has a solutin for the problem "Linked Lists - Recursive Reverse"
'''

"""
Node(2, Node(1, Node(3, Node(6, Node(5)))))
|
Node(5, Node(6, Node(3, Node(1, Node(2)))))
"""

class Node:
    '''
    Class that describes a node object
    '''
    def __init__(self, data, next_data=None):
        self.data = data
        self.next = next_data
    def __eq__(self, value: object) -> bool:
        return (self.data == value.data and
                self.next == value.next)
    def __repr__(self) -> str:
        return f'Node({self.data}, {self.next})'

def insert_in_the_end(head, data):
    '''
    This function inserts data given in the end of the head node
    '''
    if head.next is None:
        head.next = Node(data)
    else:
        head = Node(head.data, insert_in_the_end(head.next, data))
    return head

def reverse(lst):
    '''
    Function that recursively reverses a linked list.
    '''
    if lst is None:
        return None
    if lst.next is None:
        return Node(lst.data)
    if lst.next.next is None:
        return Node(lst.next.data, Node(lst.data))
    else:
        return insert_in_the_end(reverse(lst.next), lst.data)

if __name__ == '__main__':
    lst = Node(2, Node(1, Node(3, Node(6))))
    assert insert_in_the_end(lst, 14) == Node(2, Node(1, Node(3, Node(6, Node(14))))), insert_in_the_end(lst, 14)
    print('done')
