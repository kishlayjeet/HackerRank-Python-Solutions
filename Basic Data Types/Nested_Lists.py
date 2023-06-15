if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    scores = [i[1] for i in records]
    runner_score = sorted(set(scores))[1]
    names = sorted([i[0] for i in records if i[1] == runner_score])
    print(*names, sep='\n')