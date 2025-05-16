


lst = [input()]

result_n = 0
for i in range(3):
    if lst[i].isdigit():
        result_n = int(lst[i]) + 3-i
        break

if result_n%15 == 0:
    print("FizzBuzz")
elif result_n%3 == 0:
    print("Fizz")
elif result_n%5 == 0:
    print("Buzz")
else:
    print(result_n)


