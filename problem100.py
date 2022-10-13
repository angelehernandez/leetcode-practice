# Definition for a binary tree node.
class TreeNode:

    # this is not the true class definition
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    """

    inputs = [
        ([1,2,3], [1,2,3]),
        ([1,2], [1,None,2]),
        ([1,2,1], [1,1,2]),
        ([None, None, None], [None, None, None]),
    ]
    outputs = [
        True,
        False,
        False,
        True,
        ]

    def __init__(self):
        results = []
        for i in range(len(self.inputs)):
            results.append(self.isSameTree(
                TreeNode(self.inputs[i][0]), #p
                TreeNode(self.inputs[i][1]), #q
            ))

            if results[i] == self.outputs[i]:
                print(f"Test[{i}] Result: Passed!")
            else:
                print(f"Test[{i}] Result: Failed!")

    def BFS_method(self, p, q) -> bool:
        """Verifies that trees are equal using BFS method (FIFO)
        
        Args:
            p: tree with [0,100] nodes
            q: tree with [0,100] nodes
            
        Returns:
            boolean of whether or not trees are equal    
        """
        pqueue = [p]
        qqueue = [q]

        # one or both trees are empty
        if (p is None) and (q is None):
            return True
        elif (p is None) or (q is None):
            return False

        while (len(pqueue) > 0) and (len(qqueue) > 0):
            # extract node from front (FIFO)
            u = pqueue.pop(0)
            v = qqueue.pop(0)
            
            # check if equal
            if u is None and v is None:
                continue
            elif u is None or v is None:
                return False
            if u.val != v.val:
                return False

            # add next nodes if they exist
            pqueue.append(u.left)
            pqueue.append(u.right)
            qqueue.append(v.left)
            qqueue.append(v.right)
        
        # all nodes verified
        return True

    def DFS(self, node) -> list:
        """Traverses tree from node using DFS method
        
        Args:
            node: tree with [0,100] nodes

        Returns:
            list of node vals in order of traversal
        """
        stack, seen = [], []
        seen.append(node)
        while len(stack) > 0:
            u = stack.pop()
            if u not in seen:
                seen.append(u)
                stack.append(u.left)
                stack.append(u.right)
        return seen

    def DFS_method(self, p, q) -> bool:
        """Verifies that trees are equal using DFS method (LIFO)
        
        Args:
            p: tree with [0,100] nodes
            q: tree with [0,100] nodes
            
        Returns:
            boolean of whether or not trees are equal    
        """
        pseen = self.DFS(p)
        qseen = self.DFS(q)
        
        # TODO: write an __eq__ method to compare objects
        return pseen == qseen

    def isSameTree(self, p, q) -> bool:
        return self.BFS_method(p, q)

def main():
    Solution()

if __name__=='__main__':
    main()