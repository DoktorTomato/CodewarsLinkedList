'''
This is a script that has a solutin for the problem "Swap Node Pairs In Linked List"
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

def swap_pairs(head):
    '''
    Function that swaps each pair of nodes in the list, then returns the head node of the list
    '''
    if head is None or head.next is None:
        return head
    head_ref = head
    new_head_ref = head.next
    nxt = None
    temp = None
    while True:
        nxt = head_ref.next
        temp = nxt.next
        nxt.next = head_ref
        if temp is None or temp.next is None:
            head_ref.next = temp
            break
        head_ref.next = temp.next
        head_ref = temp
    return new_head_ref
