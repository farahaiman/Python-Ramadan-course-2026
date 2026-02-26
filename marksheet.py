# Marksheet Program

print("----- Student Marksheet -----")

# Input marks
math = int(input("Enter marks of Math: "))
eng = int(input("Enter marks of English: "))
urdu = int(input("Enter marks of Urdu: "))
islamiyat = int(input("Enter marks of Islamiyat: "))
science = int(input("Enter marks of Science: "))

# Total marks
total = math + eng + urdu + islamiyat + science

# Percentage
percentage = (total / 500) * 100

# Grade system
if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# Output
print("\n----- Result -----")
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
