T = int(input())

answers =[]
for _ in range(T):
  a, b, c = map(int,input().split())
  p_ab,p_bc,p_ca = map(int,input().split())
  max_price = 0


  for ab in range(min(a, b) + 1):
    if p_bc >= p_ca:
      bc = min(b-ab,c)
      ca = min(a-ab,c-bc)
      max_price = max(max_price, ab*p_ab + bc*p_bc + ca*p_ca)
    else :
      ca = min(a-ab,c)
      bc = min(b-ab, c-ca)
      max_price = max(max_price, ab*p_ab + bc*p_bc + ca*p_ca)
  answers.append(max_price)
for answer in answers:
    print(answer)


