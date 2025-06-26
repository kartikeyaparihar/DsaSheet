def palin():
    if s==reversed_s:
        print("Palindrome")
    else:
        print("Not Palindrome")
s=input("Enter the string you want to check \n")
reversed_s=s[::-1]
palin()
    