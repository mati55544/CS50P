score = int(input("score:"))

if score >= 90 and score >= 100:
    print("grade:A")
elif score >= 80 and score <= 90:
    print("grade:B")
elif score >= 80 and score <= 70:
    print("grade c")
elif score >= 70 and score <= 60:
    print("grade d")
else:
    print("your grade is f")
