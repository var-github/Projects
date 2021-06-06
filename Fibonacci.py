n = int(input("Till which number do you want to find the fibonacci series"))
x = 1
fibonacci = [0, 1]
while x < (n - 1):
    fibonacci.append((fibonacci[x]) + (fibonacci[x-1]))
    x += 1
print(fibonacci)
