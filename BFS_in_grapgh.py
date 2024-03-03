# How does BFS work?
# Starting from the root, all the nodes at a particular level are visited first and then the nodes of the next level are traversed till all the nodes are visited.

# To do this a queue is used. All the adjacent unvisited nodes of the current level are pushed into the queue and the nodes of the current level are marked visited and popped from the queue.

# Illustration:

# Let us understand the working of the algorithm with the help of the following example.

# Step1: Initially queue and visited arrays are empty.


# Queue and visited arrays are empty initially.

# Step2: Push node 0 into queue and mark it visited.

# Push node 0 into queue and mark it visited.
# Push node 0 into queue and mark it visited.

# Step 3: Remove node 0 from the front of queue and visit the unvisited neighbours and push them into queue.

# Remove node 0 from the front of queue and visited the unvisited neighbours and push into queue.
# Remove node 0 from the front of queue and visited the unvisited neighbours and push into queue.

# Step 4: Remove node 1 from the front of queue and visit the unvisited neighbours and push them into queue.

# Remove node 1 from the front of queue and visited the unvisited neighbours and push
# Remove node 1 from the front of queue and visited the unvisited neighbours and push

# Step 5: Remove node 2 from the front of queue and visit the unvisited neighbours and push them into queue.

# Remove node 2 from the front of queue and visit the unvisited neighbours and push them into queue.
# Remove node 2 from the front of queue and visit the unvisited neighbours and push them into queue.

# Step 6: Remove node 3 from the front of queue and visit the unvisited neighbours and push them into queue. 
# As we can see that every neighbours of node 3 is visited, so move to the next node that are in the front of the queue.

# Remove node 3 from the front of queue and visit the unvisited neighbours and push them into queue. 
# Remove node 3 from the front of queue and visit the unvisited neighbours and push them into queue. 

# Steps 7: Remove node 4 from the front of queue and visit the unvisited neighbours and push them into queue. 
# As we can see that every neighbours of node 4 are visited, so move to the next node that is in the front of the queue.

# Remove node 4 from the front of queue and and visit the unvisited neighbours and push ithem into queue. 
# Remove node 4 from the front of queue and visit the unvisited neighbours and push them into queue.

# Now, Queue becomes empty, So, terminate these process of iteration.

#check https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print(s, end=" ")

			# Get all adjacent vertices of the
			# dequeued vertex s.
			# If an adjacent has not been visited,
			# then mark it visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


# Driver code
if __name__ == '__main__':

	# Create a graph given in
	# the above diagram
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Breadth First Traversal"
		" (starting from vertex 2)")
	g.BFS(2)

# This code is contributed by Neelam Yadav
