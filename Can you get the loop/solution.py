'''
This is the solution for "Can you get the loop ?" problem
'''

def loop_size(node):
    '''
    This function returns a length of the loop in the list given
    '''
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count = 1
            while slow != fast:
                count += 1
                slow = slow.next
            return count
    return None
