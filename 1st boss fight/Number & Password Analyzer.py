password = "56751746a" 
attempt = 3

while attempt > 0: 
    attempt -= 1
    entred_password = input("Please enter the password: ")
    password_length = len(entred_password)
    digit_only = entred_password.isdigit()
    if entred_password == password:
        if password_length >= 8 and digit_only == False:
            print("Correct Password!")
            print("\nNow let's see if the number is Positive/Negative/Zero and Even/Odd.")
            number = int(input("Please enter the number: "))
            even = number % 2
            if number > 0 and even == 0:
                print("The number is Positive and Even")
            elif number > 0 and even != 0:
                print("The number is Positive and Odd")
            elif number < 0 and even == 0:
                print("The number is Negative and Even")
            elif number < 0 and even != 0:
                print("The number is Negative and Odd")
            elif number == 0 and even == 0:
                print("The number is Zero and Even")       
            break
        else:
            print("Verify the lengh of password typed , or is it only digits.")
    else:
        print("Wrong, Type the password agin please.")