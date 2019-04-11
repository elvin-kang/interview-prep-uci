from .TreeNode import TreeNode

# *** Not a self balancing tree ***

def size(atree):
    if atree == None:
        return 0
    else:
        return 1 + size(atree.left) + size(atree.right)

def height(atree):
    if atree == None:
        return -1
    else:
        return 1 + max(height(atree.left), height(atree.right))

def list_to_tree(alist):
    if alist == None:
        return None
    else:
        return TreeNode(alist[0], list_to_tree(alist[1]), list_to_tree(alist[2]))

def tree_to_list(atree):
    if atree == None:
        return None
    else:
        return [atree.val, tree_to_list(atree.left), tree_to_list(atree.right)]

def print_BST(atree, indent_char='.', indent_delta=2):
    def print_tree(indent, atree):
        if atree == None:
            return None
        else:
            # in-order
            print_tree(indent + indent_delta, atree.right)
            print(indent * indent_char + str(atree.val))
            print_tree(indent + indent_delta, atree.left)
    print_tree(0, atree)

def search(atree, val):
    if atree == None:
        return None
    if val == atree.val:
        return atree
    elif val < atree.val:
        return search(atree.left, val)
    else: # val > atree.val
        return search(atree.right, val)

def add(atree, val):
    if atree == None:
        return TreeNode(val)
    if val < atree.val:
        atree.left = add(atree.left, val)
        return atree
    elif val > atree.val:
        atree.right = add(atree.right, val)
        return atree
    else:
        return atree

def add_all(atree, vals):
    for v in vals:
        atree = add(atree, v)
    return atree

def copy(atree):
    if atree == None:
        return None
    else:
        return TreeNode(atree.val, copy(atree.left), copy(atree.right))

def equal(t1, t2):
    if t1 == None or t2 == None:
        return t1 == t2
    else:
        return t1.val == t2.val and equal(t1.left, t2.left) and equal(t1.right, t2.right)

