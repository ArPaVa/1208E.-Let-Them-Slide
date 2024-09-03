from collections import deque

def MaxSlidingWindow(nums:list[int],k:int):
    output = []
    q = deque()
    l = r = 0
    while r < len(nums):
        
        while q and nums[q[-1]] < nums[r]:
            
            q.pop()
        q.append(r)
        
        if l > q[0]:
            q.popleft()
            
        if (r+1) >= k:
            output.append(nums[q[0]])
            l += 1
        r+= 1
    return output


fl = input()
n, w = fl.split(" ")
n = int(n)
w = int(w)
results = [0] * (w + 2)
resultstr = "" 

for i in range(n):
    line = input()
    line = line.split(" ")
    line = [int(i) for i in line]
    length = line[0]
    row = line.copy()
    row[0] = 0
    
    row.append(0)
    q = deque()
    l = r = 1
    q.append(0)
    blank = w - length
    k = length - blank
    
    while r <= w:
        if r <= length + 1:
            while q and row[q[-1]] <= row[r]:
                q.pop()
            q.append(r)
        if r - blank > q[0]:
            q.popleft()
        
        max = row[q[0]]
        results[r] += max 
        
        if w > length*2 and r == length+1:
            results[blank + 1] -= max
            r = blank
        else:
            results[r+1] -= max
            
        r+=1
return_list = ""            
for i  in range(1,w+1):
    results[i] += results[i-1]
    return_list = return_list + f"{results[i]} "
print(return_list)

# inputCopy
# 3 3
# 3 2 4 8
# 2 2 5
# 2 6 3
# outputCopy
# 10 15 16 

# inputCopy
# 2 2
# 2 7 8
# 1 -8
# outputCopy
# 7 8 



