# github repository- Lavanya-B

def heapsort(l): 

    def heap(l, node, maxlen=len(l)-1):
        left_child = node * 2 + 1
        right_child = node * 2 + 2
        larger = node 
        if left_child <= maxlen:
            if l[left_child] > l[node]:
                larger = left_child
        if right_child <= maxlen:
            if l[right_child] > l[larger]:
                larger = right_child 
        if larger != node:
            l[larger], l[node] = l[node], l[larger]
            heap(l, larger, maxlen)
        return l[0]
        
    def buildheap(l):
        for i in range((len(l))//2-1,-1,-1):
            heap(l, i)
                 
    buildheap(l)
    
    for j in range(len(l)-1, 0, -1):
        l[0], l[j] = l[j], l[0]
        heap(l, 0, j-1)
             
    return l
 
a = [6,1,7,8,9,3,5,4,2]

print(heapsort(a))            