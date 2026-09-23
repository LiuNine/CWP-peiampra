num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
ans = num1 * num2
print(f"{num1} x {num2} = {ans}")
if ans == 0:
    print("The result is positive and negative.")
elif ans > 0:
    print("The result is positive.")
else:
    print("The result is negative.")