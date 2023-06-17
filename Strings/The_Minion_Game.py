def minion_game(string):
    string = string.upper()
    stuartScore = 0
    kevinScore = 0
    s = len(string)
    for i in range(s):
        if string[i] in 'AEIOU':
            kevinScore += (s-i)
        else:
            stuartScore += (s-i)
    if kevinScore > stuartScore:
        print(f"Kevin {kevinScore}")
    elif kevinScore < stuartScore:
        print(f"Stuart {stuartScore}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)