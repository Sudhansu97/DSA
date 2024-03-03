def findLevel(n,edges,x):
    adj_dict ={}
    for i in edges:
        if i[0] in adj_dict:
            adj_dict[i[0]].append(i[1])
        else:
            adj_dict[i[0]] = [i[1]]
    
    visited= [0 for _ in range(n)]
    q = []
    q.append(edges[0][0])
    lvl = 0
    while len(q)>0:
        # print(q,visited,lvl,adj_dict)
        sz = len(q)
        while sz>0:
            current_node = q.pop(0)
            if current_node == x:
                return lvl
            for node in adj_dict[current_node]:
                if not visited[node]:
                    # print("Node",current_node, node,q)
                    q.append(node)
                    visited[node] = 1
            sz -= 1
        lvl+=1
        
    return -1




# Driver Code
V=5
edges=[[0,1],[0,2],[1,3],[2,4]]
X=3
 
#Function call
level=findLevel(V,edges,X)
print(level)
 