'''
Solution for "Linked Lists - Get Nth Node" problem
'''

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next_data=None):
        self.data = data
        self.next = next_data
    
def get_nth(node, index):
    '''
    Function that gets the element of linked list with given index
    '''
    if index == 0:
        return Node(node.data)
    index -= 1
    return get_nth(node.next, index)
  