# https://www.geeksforgeeks.org/minimize-maximum-adjacent-difference-in-a-path-from-top-left-to-bottom-right/

# Given a matrix arr[][] of size M * N, where arr[i][j] represents the height of the cell (row, col). The task is to find a path from top-left to bottom-right such that the value of the maximum difference in height between adjacent cells is minimum for that path.

# Note: A path energy is the maximum absolute difference in heights between two consecutive cells of the path.


def isValid(i,j,x,visited,arr,parent):
    if i<0 or j<0 or i>=m or j>=n or visited[i][j] or abs(arr[i][j]-parent)>x:
        return False
    if i==m-1 and j==n-1:
        return True
    visited[i][j] = True
    if isValid(i+1,j,x,visited,arr,arr[i][j]):
        return True
    if isValid(i-1,j,x,visited,arr,arr[i][j]):
        return True
    if isValid(i,j+1,x,visited,arr,arr[i][j]):
        return True
    if isValid(i,j-1,x,visited,arr,arr[i][j]):
        return True
    return False

def minimizeMaxAdjDiffPath(arr,m,n):
    start,end = 0,10000000
    result = arr[0][0]
    while start<=end:
        mid = (start+end)//2
        visited = [[False for _ in range(n)] for _ in range(m)]
        if isValid(0,0,mid,visited,arr,arr[0][0]):
            result = mid
            end -= 1
        else:
            start +=1
    return result





arr=[[1,2,1],[2,8,2],[2,4,2]]
m=len(arr)
n=len(arr[0])
 
# Function Call
print(minimizeMaxAdjDiffPath(arr,m,n))