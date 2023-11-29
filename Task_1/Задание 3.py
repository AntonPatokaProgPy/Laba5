import validation

user_input = int(input("Введите число: "))

if validation.check_even(user_input):
    print("Число четное")
else:
    print("Число нечетное")
