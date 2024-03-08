def is_happy(num: int) -> int:
    """Check if a number is happy."""
    num = list(str(num))
    sq_list = [int(i) ** 2 for i in num]
    result = sum(sq_list)
    return result

def check_happy(num: int) -> bool:
    """Check if a number is happy within a certain limit of iterations."""
    i = 0
    temporary = is_happy(num)
    while is_happy(temporary) != 1 and i < 100:
        i += 1
        temporary = is_happy(temporary)
    
    return is_happy(temporary) == 1

while True:
    try:
        user_input = int(input('Enter a number: '))
        result = check_happy(num=user_input)
        if result:
            print("Number is happy")
        else:
            print("Number is unhappy =(")
    except ValueError:
        print("Please enter a valid integer.")
