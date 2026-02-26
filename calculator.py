print(".....Calculator.....")

# User se input lena
value1 = float(input("First number: "))
value2 = float(input("Second number: "))
count = input("Operator dijiye (+, -, *, /): ")

# Calculation logic
if count == "+":
    ans = value1 + value2
elif count == "*":
    ans = value1 * value2
elif count == "-":
    ans = value1 - value2
elif count == "/":
    if value2 != 0:   # divide by zero check
        ans = value1 / value2
    else:
        ans = "Error: Zero se divide nahi ho sakta"
else:
    ans = "Invalid operator"

# print karna
print("Answer:", ans)
