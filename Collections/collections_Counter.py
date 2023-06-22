from collections import Counter
X = int(input())
available_sizes = map(int, input().split())
N = int(input())
asl = Counter(available_sizes)
money_earned = 0
for i in range(N):
    desired_size, price = map(int, input().split())
    if desired_size in asl.keys() and asl[desired_size] > 0:
        asl[desired_size] -= 1
        money_earned += price
print(money_earned)

