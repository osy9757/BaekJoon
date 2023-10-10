from collections import defaultdict
import sys

def count_zero_sum(n, A, B, C, D):
    sum_dict = {}    
    for a in A:
        for b in B:
            sum_val = a + b
            sum_dict[sum_val] = sum_dict.get(sum_val, 0) + 1
    
    count = 0
    for c in C:
        for d in D:
            target = -(c + d)
            count += sum_dict.get(target, 0)
    
    return count

n = int(sys.stdin.readline())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
print(count_zero_sum(n, A, B, C, D))