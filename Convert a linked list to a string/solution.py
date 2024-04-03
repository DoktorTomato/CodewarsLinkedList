'''
This script has a function that "stringifies" the linked list given
'''

class Node():
    '''
    This class is a part of lined list objects
    '''
    def __init__(self, data, next_data = None):
        self.data = data
        self.next = next_data

def stringify(node:Node):
    '''
    This function "stringifies" the linked list given
    '''
    res = ''
    try:
        res += str(node.data)
    except AttributeError:
        res += 'None'
    if isinstance(node, Node) and isinstance(node.next, Node):
        res += ' -> '
        res += stringify(node.next)
    elif isinstance(node, Node):
        res += ' -> '
        res += str(node.next)
    return res

if __name__ == '__main__':
    assert stringify(Node(1, Node(2, Node(3)))) == "1 -> 2 -> 3 -> None"
    assert (stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))) ==
            "0 -> 1 -> 4 -> 9 -> 16 -> None")
    assert stringify(None) == 'None'
    print('You\'r function is probably working')
