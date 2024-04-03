'''
This script can parse str into linked list
'''

class Node:
    '''
    This class is a part of lined list objects
    '''
    def __init__(self, data, next_data=None):
        self.data = data
        self.next = next_data

    def __eq__(self, other: object) -> bool:
        return (self.data == other.data and
                self.next == other.next)

def linked_list_from_string(s):
    '''
    This function parses given str into linked list
    '''
    if s == "None":
        return
    data = s.split(' -> ')[0]
    if data.isnumeric():
        data = int(data)
    elif data == 'None':
        data = None
    if len(s.split(' -> ')) > 1:
        next_data = linked_list_from_string(' -> '.join(s.split(' -> ')[1:]))
    else:
        next_data = s.split(' -> ')[1]
        if next_data.isnumeric():
            next_data = int(data)
        elif next_data == 'None':
            next_data = None
    return Node(data, next_data)

if __name__ == '__main__':
    assert linked_list_from_string("1 -> 2 -> 3 -> None") == Node(1, Node(2, Node(3)))
    assert (linked_list_from_string("0 -> 1 -> 4 -> 9 -> 16 -> None") ==
            Node(0, Node(1, Node(4, Node(9, Node(16))))))
    assert linked_list_from_string("None") is None
    print('You\'r function is probably working')
