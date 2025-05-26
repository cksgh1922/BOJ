#fizzbuzz

first = input()
second = input()
third = input()

ans = 0

if first.isdigit():
    ans+=int(first)+3
elif second.isdigit():
    ans+=int(second)+2
elif third.isdigit():
    ans+=int(third)+1

if ans%3 == 0 and ans%5 == 0:
    print("FizzBuzz")
elif ans%3 == 0:
    print("Fizz")
elif ans%5 == 0:
    print("Buzz")
else:
    print(ans)