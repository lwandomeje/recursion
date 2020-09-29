def addition(num1,num2):
    answer= num1+num2
    return answer
first_number=int(input("please enter first number"))
second_number=int(input("please enter second number"))
result= addition(first_number,second_number)
print(result)


number=6
factorial=1
while number >1:
    factorial=factorial*number
    number=number-1
    print(factorial)


def fact(number):
    if number<2:
        return 1
    else:
        answer=number* fact(number-1)
        return answer

number= int(input("please enter a number"))
print(fact(number))


def ispalindrome (string):
    if len(string)<=1 :
        return True
    else:
        return string [0]==string[-1] and ispalindrome(string[1:-1])
string= input("please enter string")
print(ispalindrome(string))

