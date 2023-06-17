_ = input()
room_numbers = list(map(int, input().split()))
count = {}
for index, element in enumerate(room_numbers):
    if element in count:
        count[element] += 1
    else:
        count[element] = 1
captain_room = [key for key, value in count.items() if value == 1]
print(*captain_room)
