class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        m=len(wordList[0]) # assigning length of wordlist to m
        wordList = set(wordList) # converting wordlist to set
        
        wordList.add(beginWord) # adding in set with beginword
        
        adj = defaultdict(list) # creating the defaultdict
        for word in wordList: # for every word in wordlist producing the string and appending it to adjacency matrix
            for i in range(m):
                s = word[:i]+"_"+word[i+1:]
                adj[s].append(word)
                
        q=deque() # creating queue
        q.append(beginWord) # appending beginword to queue
        visited = set() # creating visited set
        dist = 0 # assigning dist to 0
        visited.add(beginWord) # adding beginword in visited
        while q:
            dist+=1 # incrementing dist by 1 
            size = len(q)
            for _ in range(size):
                currword = q.popleft() # popping from queue and storing it to currword
                for i in range(m):
                    s = currword[:i]+"_"+currword[i+1:] # creating the string with the currword
                    for nextword in adj[s]: # for every word in adjacency matrix
                        visited.add(nextword) # adding the word in visited array
                        q.append(nextword) # appending the word in visited
                        if nextword == endWord: # if nextword is equal to endword
                            return dist+1 # returning the dist+1
                        
        return 0 # returning 0