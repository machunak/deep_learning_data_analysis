with open('data/poem.txt', 'r', encoding='utf-8') as f:
    num = 0

    for line in f:
        print(line.split())
        num += len(line.split())
    print(num)