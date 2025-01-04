#Logic question 1 - IF ELIF Statement

num = int(input("Enter any number: "))
if num >=0 and num <=9:
    print(num, "is a single digit number")
elif num >=10 and num <=99:
    print(num, "is a double digit number")
elif num >=100 and num <=999:
    print(num, "is triple digit number")
elif num >=1000 and num <=9999:
    print(num, "is a four digit number")
elif num >=10000 and num <=99999:
    print(num, "is a five digit number")
else:
    print(num,"is a more than five digit number")
