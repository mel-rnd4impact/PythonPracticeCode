# 2 blank lines after function definition
def sum_two():
    print(2+2)


sum_two()
sum_two()


def func_name(param):
    print(param+3)


func_name(4)


def default_ex(num1=5, num2=4):
    print(num1 * num2)


default_ex()
default_ex(4)
default_ex(9,8)
# make sure regular code outside functions are non-indented

def default_ex2(num1=5, num2=4):
    return num1 * num2


prod = default_ex2() + 30
print(prod)
