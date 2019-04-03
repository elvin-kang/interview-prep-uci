from ListNode import ListNode

# Some functions are assuming that
# list only contains numeric values

# Query/accessor functions

def len(ll):
    count = 0
    while ll != None:
        count += 1
        ll = ll.next
    return count

def sum(ll):
    total = 0
    while ll != None:
        total += ll.val
        ll = ll.next
    return total

def toString(ll):
    tostr = ''
    while ll != None:
        tostr += str(ll.val) + '->'
        ll = ll.next
    return tostr + 'None'

def list_to_ll(l):
    if l == []:
        return None
    front = rear = ListNode(l[0])
    for v in l[1:]:
        rear.next = ListNode(v)
        rear = rear.next
    return front

def find(ll, val):
    while ll != None:
        if ll.val == val:
            return ll
        ll = ll.next
    return None

def copy(ll):
    if ll == None:
        return None
    front = rear = ListNode(ll.val)
    while ll.next != None:
        ll = ll.next
        rear.next = ListNode(ll.val)
        rear = rear.next
    return front

def iterator(ll):
    while ll != None:
        yield ll.val
        ll = ll.next

# command/mutator functions

def append(ll, val):
    if ll == None:
        return ListNode(val)
    front = ll
    while ll.next != None:
        ll = ll.next
    ll.next = ListNode(val)
    return front

def add_front(ll, val):
    ll = ListNode(val, ll)

def remove_front(ll):
    if ll == None:
        return
    ll = ll.next