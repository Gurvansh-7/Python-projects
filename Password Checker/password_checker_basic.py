import string

print("Password should be of min '8' digit, including atleast one 'capital letter', 'lower letter', 'number' and 'symbol'")
pasw = input("Enter you password - ")

capital = string.ascii_uppercase
small = string.ascii_lowercase
digit = string.digits
symbol = string.punctuation

capital_check = False
small_check = False
digit_check = False
symbol_check = False

if len(pasw) >= 8:
    for i in capital:
        if i in pasw:
            capital_check = True
            print("Captial letter - check")
            break
    else:
        print("Add atleast 1 'capital letter'")

    for i in small:
        if i in pasw:
            small_check = True
            print("Small letter - check")
            break
    else:
        print("Add atleast 1 'Small letter'")
    
    for i in digit:
        if i in pasw:
            digit_check = True
            print("Digit - check")
            break
    else:
        print("Add atleast 1 num from '0 to 9'")
       
    for i in symbol:
        if i in pasw:
            symbol_check = True
            print("Symbol - check")
            break
    else:
        print("Add atleast 1 symbol")       
else:
    print("Enter min 8 digits")

if (capital_check and small_check and digit_check and symbol_check):
    print("Strong Password")
else:
    print("Weak Password")