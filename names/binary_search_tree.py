"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque

# from queue.py import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        ## if there's no tree, instantiate the BSTNode
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

        
    # Binary Search #
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()
        
        # current_node = self.right
        # while current_node.right is not None:
        #     current_node = current_node.right
        # return current_node.value
        
           
            


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self is None:
            return
        if self.left is not None:
            self.left.in_order_print(node)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(node)
        
        
        
       

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        items = []
        items.append(self)
        while len(items) > 0:
            current = items.pop(0)
            print(current.value)
            if current.left is not None:
                items.append(current.left)
            if current.right is not None:
                items.append(current.right)
        
            
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        items = []
        items.append(self)
        while len(items) > 0:
            current = items.pop()
            print(current.value)
            if current.left is not None:
                items.append(current.left)
            if current.right is not None:
                items.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required
## identical to in_order_print, just a different order!!! ##
    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass
## identical to in_order_print, just a different order!!! ##
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.in_order_print(5)
bst.bft_print(1)
    
    #  items = Queue()
    #     items.enqueue(self.value)
    #     while self.size > 0:
    #         print(self.value)
    #         if self.left is not None:
    #             items.enqueue(self.left.value)
    #         if self.right is not None:
    #             items.enqueue(self.right.value)
    #         items.dequeue()
