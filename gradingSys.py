#GCSE GRADING SYSTEM

mark = int(input("Enter mark: "))

if mark >= 90:
    print("Grade 9")
elif mark >= 80:
    print("Grade 8, need", 90 - mark, "for next grade")
elif mark >= 70:
    print("Grade 7, need", 80 - mark, "for next grade")
elif mark >= 60:
    print("Grade 4, need", 70 - mark, "for next grade")
else:
    print("Fail, need", 60 - mark, "for next grade")
