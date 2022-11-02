#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        q=deque() # creating queue
        q.append(root) # appending root to queue
        
        while q:
            size = len(q)
            level = set() # creating new set
            for i in range(size):
                node = q.popleft() # popping the queue value and storing in node
                level.add(node.val) # adding the node value in level
                
                if node.left and node.right and ((node.left.val==x and node.right.val==y) or (node.left.val==y and node.right.val==x)): # if node left and node right and x,y assigned to node left and node right
                    return False
                if node.left:
                    q.append(node.left) # appending the node's left value to queue
                if node.right:
                    q.append(node.right) # appending the node's right value to queue
                     
            if x in level and y in level: # if x in level array and y in level array then return true
                return True 
        return False
