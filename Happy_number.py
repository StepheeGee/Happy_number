def check_happy(num: int) -> bool:
    def is_happy(num) -> int:
        num = list(str(num))
        sq_list = []
        for i in num:
            sq_list.append(int(i) ** 2)
        result = sum(sq_list)
        return result

    i = 0
    temporary = is_happy(num)
    while is_happy(temporary) != 1 and i < 100:
        i += 1
        temporary = is_happy(temporary)
    if is_happy(temporary) == 1:
        print("Number is happy")
        return True

    if i == 100:
        print("Number is unhappy =(")
        return False


while True:
    check_happy(num=int(input('Enter a number: ')))
