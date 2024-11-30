def draw(numb):
    if numb <= 0:
        return

    print("*" * numb)
    draw(numb - 1)
    print("#" * numb)


num = int(input())
draw(num)

