def driving_license(age):
    if age >= 18:
        return "you are eligible for a driving license"
    elif age >= 17:
        return "needs special permit"
    else:
        return "you are not eligible for a driving license"

def main():
 age = int(input("Enter your age: "))
 result = driving_license(age)
 print(result)

main()
    
