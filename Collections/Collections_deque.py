from collections import deque
queue = deque()

# 1st Method
for i in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'append':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'appendleft':
        queue.appendleft(int(cmd[1]))
    elif cmd[0] == 'pop':
        queue.pop()
    elif cmd[0] == 'popleft':
        queue.popleft()
print(*queue)


# 2nd Method
for i in range(int(input())):
    cmd = input().split()
    try:
        exec(f'queue.{cmd[0]}({cmd[1]})')
    except IndexError as i:
        exec(f'queue.{cmd[0]}()')
print(*queue)