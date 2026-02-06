num = input("enter a number: ")

digits = list(num)

if len(digits) < 3:
    print("Not a Hill number")
else:
    mode = "up"
    went_up = False
    went_down = False
    is_hill = True

    for i in range(len(digits) - 1):
        curr = digits[i]
        next_ = digits[i + 1]

        if curr == next_:
            is_hill = False
            break

        if next_ > curr:
            if mode == "down":
                is_hill = False
                break
            went_up = True
        else:
            mode = "down"
            went_down = True

    if is_hill and went_up and went_down:
        print("Hill number")
    else:
        print("Not a Hill number")