num = 6

def test_factorial_1():
    num = 5
    fact = 1
    while(num>0):
        fact = num * fact
        num = num-1
    print("factorial number is" , fact)

def test_factorial_2():
    num = 5
    fact = 1
    if (num<0):
        print("We cant find factorial number for negative values")
    elif(num==1):
        print("We cant find factorial number for negative values")
    else:
        for i in range(1,num+1):
            fact=fact*i
        print(fact)
def test_palindrome():
    num = 151
    num1 = num
    pal1 = 0
    while(num>0):
        x = num % 10
        pal1 = (pal1*10) + x
        num = int(num / 10)
    print(pal1)
    if(num1 == pal1):
        print("Given number is palindrome")
    else:
        print("given number is not palindrome")

def test_oddnumbercount():
    num = 100
    count = 0
    for i in range (1,num+1):
        if(i%2==1):
            count += 1
    print(count)

def test_evennumbercount():
    num = 100
    count = 0
    for i in range(1, num+1):
        if(i%2==0):
            count = count + 1
    print(count)

def test_evennumberprint():
    num = 100
    for i in range(1, num+1):
        if (i%2==0):
            print(i)


def test_oddnumberprint():
    num = 100
    for i in range (1, num+1):
        if(i%2==1):
            print(i)

def test_odd_even_number():
    num = 100
    for i in range (1, num+1):
        if(i%2==0):
            print(i, "is even number")
        else:
            print(i, "is odd number")








