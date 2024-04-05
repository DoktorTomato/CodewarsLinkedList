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
    res = Node(None)
    end_point = res
    cur = head.data
    nxt = head.next
    oncemore = iter([True, False])
    while nxt is not None or next(oncemore):
        if nxt is not None and cur == nxt.data:
            nxt = nxt.next
        else:
            if res.data is None:
                res.data = cur
                if nxt is not None:
                    cur = nxt.data
                    nxt = nxt.next
            else:
                end_point.next = Node(cur)
                end_point = end_point.next
                if nxt is not None:
                    cur = nxt.data
                    nxt = nxt.next
    return res

if __name__ == '__main__':
    assert Node(1, Node(2, Node(3, Node(4)))) == remove_duplicates(Node(1, Node(2, Node(3, Node(4)))))
