a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
ans = a*b
if ans > 0 :
     print(f"{a} x {b} = {ans}")
     print ("The result is positive.")
elif ans < 0 :
    print(f"{a} x {b} = {ans}")
    print ("The result is negative.")
elif ans == 0 :
    print(f"{a} x {b} = {ans}")
    print ("The result is positive and negative.")

