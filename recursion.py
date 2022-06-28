def factorial(n):
    if n == 1:
        return 1
    else:
        answer = n * factorial(n - 1)
        print(answer)
        return answer

input = input("Enter a number: ")
factorial(int(input))
