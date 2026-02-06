s = input()
n = int(input())

if len(s) % n != 0:
    print("Division not possible")
else:
    part = s[:n]
    valid = True

    for i in range(0, len(s), n):
        if s[i:i+n] != part:
            valid = False
            break

    if valid:
        for i in range(0, len(s), n):
            print(part)
    else:
        print("Sequence cannot be same")