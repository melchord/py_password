passwordFile = open("SecretPasswordFile.txt")
secretPassword = passwordFile.read()
print("Enter your password.")
typedPassword = input()
if typedPassword == secretPassword:
    print("Access granted")
    if typedPassword == "12345":
        print("That password is most likely not the best choice...")
else:
    print("Access denied")
