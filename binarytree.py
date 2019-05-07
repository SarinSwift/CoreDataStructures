#!python


from queue import LinkedQueue
from stack import LinkedStack


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.right == None and self.left == None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.right != None or self.left != None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best and worst case running time: O(logn)"""
        # if the node has both a left and a right
        if self.left and self.right:
            leftSide = self.left.height()
            rightSide = self.right.height()
            return max(leftSide, rightSide) + 1
        # has only left node
        elif self.left:
            return self.left.height() + 1
        # has only right node
        elif self.right:
            return self.right.height() + 1
        # no children found
        else:
            return 0        # when the function returns after the recursive function call ends.

class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best and worst case running time: O(h) where h is the height of the node"""
        # Check if root node has a value and if so calculate its height
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: O(logn)
        Worst case running time: O(n) when an unbalance tree looks like a linked list"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(logn) since it has a minimum of Ologn levels
        Worst case running time: O(h) where h is the height of the tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # node = self._find_node_iterative(item)

        # Return the node's data if found, or None
        return node.data if node != None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: O(logn)
        Worst case running time: O(n) where n is the total # of nodes"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = BinaryTreeNode(item)
            # Increase the tree size
            self.size += 1
            return

        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)

        if item < parent.data:
            # Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        # Check if the given item should be inserted right of parent node
        elif item > parent.data:
            # Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        # Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(logn)
        Worst case running time: O(n) where the tree looks like a linked list"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(logn)
        Worst case running time: O(n) where the tree looks like a linked list"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: O(logn) where n goes up to the node of the child
        Worst case running time: O(n) where the item is the last node"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""

        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)  # Hint: Remember to update the parent parameter
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)  # Hint: Remember to update the parent parameter

    # def delete(self, item):
    #     """Remove given item from this tree, if present, or raise ValueError.
    #     TODO: Best case running time: ??? under what conditions?
    #     TODO: Worst case running time: ??? under what conditions?"""
    #     # TODO: Use helper methods and break this algorithm down into 3 cases
    #     # based on how many children the node containing the given item has and
    #     # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            # self._traverse_in_order_recursive(self.root, items.append)
            self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since we visit every node, but mostly O(3n)
        Memory usage: O(logn) for the depth of the tree"""
        if node is not None:
            # Traverse left subtree, if it exists
            self._traverse_in_order_recursive(node.left, visit)
            # Visit this node's data with given function
            visit(node.data)
            # Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since we visit every node
        Memory usage: O(logn) for the depth of the tree"""
        # -create an empty stack
        # -curr variable which starts off with the self.root (will be updated in a while loop!!)
        # -go in a while loop while true (will be false when the stack is empty)
        #   -call push() on curr while there's a value
        #   -update the curr to become the curr's left
        #   -once we hit a None value:
        #       - we'd want to pop() off the stack
        #       - append it to the list
        #       - update curr to be the recently popped node's right node
        #       - however, if the stack is empty in here, we set the while loop to false and exit the function!

        stack = LinkedStack()       # will act as the recursive call
        curr = self.root            # start at the root
        stillLoop = True            # loop until the stack is empty

        while stillLoop:
            # we're at the end of a leaf node
            if curr == None:
                if stack.length() > 0:
                    node = stack.pop()
                    visit(node.data)
                    curr = node.right
                # our stack is empty so we can finally return once all the nodes have been visited
                else:
                    stillLoop = False
            # we can still go down the left side
            else:
                stack.push(curr)
                curr = curr.left

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            # self._traverse_pre_order_recursive(self.root, items.append)
            self._traverse_pre_order_iterative(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since we visit every node
        Memory usage: O(h) where h is the height of the tree"""
        if node != None:
            # Visit this node's data with given function. Appending the node's data to our items array
            visit(node.data)
            # Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.left, visit)
            # Traverse right subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since we visit every node
        Memory usage: O(h) where h is the height of the tree"""
        # -create an empty stack and push the root node in there
        # -loop through while the stack isn't empty
        #   -pop() on the stack
        #   -push() the right node of the node we just popped off the stack
        #   -pop() and left node of the node we just popped off the stack

        stack = LinkedStack()
        stack.push(node)            # since we're starting in the middle, we start the stack off with self.root

        while not stack.is_empty():
            toPop = stack.pop()
            if toPop == None:
                continue        # skip this one
            visit(toPop.data)       # add in the data
            stack.push(toPop.right) # add the right before the left since this is a stack,
            stack.push(toPop.left)  #   the next time we look in the stack, the left will be seen before the right!!


    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            # self._traverse_post_order_recursive(self.root, items.append)
            self._traverse_post_order_iterative(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since we visit every node
        Memory usage: O(h) where h is the height of the tree"""
        if node is not None:
            # Traverse left subtree, if it exists
            self._traverse_post_order_recursive(node.left, visit)
            # Traverse right subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit)
            # Visit this node's data with given function
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) since we visit every node
        Memory usage: O(h) where h is the height of the tree"""
        # NOT WORKING
        # leftStack = LinkedStack()
        # rightStack = LinkedStack()
        # theRoot = node          # stays the same until end
        # curr = node             # will update this variable in the while loop
        # # visit all the left nodes
        # leftStack.push(theRoot.left)
        # while not leftStack.is_empty():
        #     toPop = leftStack.pop()
        #     if toPop == None:
        #         continue
        #     visit(toPop.data)
        #     leftStack.push(toPop.right)
        #     leftStack.push(toPop.left)
        #     print(leftStack.list)
        # # visit all the right nodes
        # rightStack.push(theRoot.right)
        # while not rightStack.is_empty():
        #     toPop = rightStack.pop()
        #     if toPop == None:
        #         continue
        #     visit(toPop.data)
        #     rightStack.push(toPop.right)
        #     rightStack.push(toPop.left)
        # # before returning, we add the mid node (self.root)
        # visit(theRoot.data)

        # WORKING
        # -create 2 stacks where the second stack will be what we return starting from the peek to the end
        # -start the first stack with the root node
        # -loop through first stack while isn't empty
        #   - pop from the first stack then add it to our second stack
        #   - push left of the popped item
        #   - push right of the popped item
        # -after our second stack has all the nodes, we can append to the list as we call pop() method
        startStack = LinkedStack()
        endStack = LinkedStack()
        startStack.push(node)

        while not startStack.is_empty():
            toPop = startStack.pop()

            if toPop == None:
                continue

            endStack.push(toPop)
            startStack.push(toPop.left)
            startStack.push(toPop.right)

        while not endStack.is_empty():
            visit(endStack.pop().data)


    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Visits its neighbors
        Run time: O(n) where n is the number of nodes in the entire tree. O(4n)
        Memory usage: O(w) where w is the width of the tree
                        O(2^h) worst case bottom most level of tree
                        (n+1) / 2"""
        # Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.is_empty():
            # Dequeue node at front of queue
            node = queue.dequeue()

            if node is not None:
                # Visit this node's data with given function
                visit(node.data)
                # Enqueue this node's left child
                if node.left != None:
                    queue.enqueue(node.left)
                # Enqueue this node's right child
                if node.right != None:
                    queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
