A, B = map(int, input().strip().split())
N = int(input())
print(min(abs(B - A), min(abs(B - int(input())) + 1 for _ in range(N))))
