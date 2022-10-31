class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj = defaultdict(list) # creating adjacency of defaultdict
        q = deque() # creating queue
        q.append(root) # appending root to queue
        visited = set() # setting visited to set
        while q:
            curr = q.popleft() # popping the q and storing it to curr
            
            if curr.left: # if curr.left then append curr to adjacency of left, then append left value to adjacency of curr
                adj[curr.left].append(curr) 
                adj[curr].append(curr.left)
                q.append(curr.left)
                
            if curr.right: # if curr.right then append curr to adjacency of right, then append right value to adjacency of curr
                adj[curr.right].append(curr)
                adj[curr].append(curr.right)
                q.append(curr.right)
                
        q.append(target) # appending target to queue
        
        while q and k>0: # run until k is greater than 0
            size = len(q)
            for i in range(size):
                curr = q.popleft() # popping the queue and storing it to curr
                visited.add(curr) # adding curr to visited
                for neigh in adj[curr]: # for neighbour in adjacency of curr
                    if neigh not in visited:
                        q.append(neigh) # appending neighbour to queue
            
            k-=1 # decrement k by 1
        result = [] # creating empty result
        for node in q:
            result.append(node.val) # for every node in queue appending the node value in result
        
        return result # returning the result