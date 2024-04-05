'''
This is a script that has a solutin for the problem "Linked Lists - Remove Duplicates"
'''

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

def remove_duplicates(head):
    '''
    Function which takes a list sorted in
    increasing order and deletes any duplicate 
    nodes from the list
    '''
    if head is None:
        return None
    if head.next is None:
        return head
    if head.next.data != head.data:
        return Node(head.data, remove_duplicates(head.next))
    try:
        while head.next.data == head.data:
            head.next = head.next.next
        return Node(head.data, remove_duplicates(head.next))
    except AttributeError:
        return head
