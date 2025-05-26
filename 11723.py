S = set()

for _ in range(int(input())):
    # command, x = input().split()
    al_command = input().strip()
    if al_command == "all":
        S = set(list(range(1, 21)))
    elif al_command == "empty":
        S = set()
    else:
        command, x = al_command.split()
        x = int(x)
        
        if command == "add":
            S.add(x)
        elif command == "remove":
            S.discard(x) # remove대신 사용 가능 | 요소가 없으면 그냥 무시함
        elif command == "check":
            print(1 if x in S else 0)
        elif command == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)

