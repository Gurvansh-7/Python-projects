# It is for learning, otherwise it is not polished

import msvcrt   # it is window specific tool, so code will not work in linux or mac
import sys
import string

password = ""   # as in the starting there will be nothing
print("Password should be of total '8' digit, including atleast one 'capital letter', 'lower letter', 'number' and 'symbol'")   # line 1
sys.stdout.write("Enter Password => ")      # line 2
sys.stdout.flush()

while True:
    ch = msvcrt.getch()     # input ie read the each keystore and return byte not string
    
    if ch == b"\x08":       # for backspace
        password = password[:-1]
        continue
    
    try:
        char = ch.decode("utf-8")       # convert the byte into string
    except UnicodeDecodeError:          # some character cannot be decoded by utf-8
        continue
    password += char

    capital = string.ascii_uppercase
    small = string.ascii_lowercase
    digit = string.digits
    symbol = string.punctuation
     
    capital_check = any(i in password for i in capital)   # any return True if any element satifies the condition
    small_check = any(i in password for i in small)
    digit_check = any(i in password for i in digit)
    symbol_check = any(i in password for i in symbol)
    
    # to display password and update every character user write
    sys.stdout.write("\rEnter Password => " + password)    # display password and \r to rewrite line 2 as we still at line 2
    sys.stdout.flush()             
    sys.stdout.write("\033[s")              # line 2: save cursor position
    sys.stdout.write("\n")                  # line 3: 
    sys.stdout.write("\r Capital letter [{} ]  Small letter [{} ]  Digit [{} ]  Symbol [{} ]".format(  # written on line 3
        "✔" if capital_check else "❌",
        "✔" if small_check else "❌",
        "✔" if digit_check else "❌",
        "✔" if symbol_check else "❌"))
    sys.stdout.write("\033[u")              # line 2: restore cursor position to saved one ie at line 2
    sys.stdout.flush()                      # at last we are reaching line 2 before input
    
    if ch == b"\r":         # read until press enter
        if capital_check and small_check and digit_check and symbol_check:   # if all requirement meet it break
            password = password[:-1]        # remove the hidden enter \r ch
            break
        else:
            print(f"\nPrevious Password is => {password}")     # if entered: line 3 by \n than its own \n, it is at starting of line 4
            print("Weak password, try again")                  # line 4 => line 5 starting
            sys.stdout.write("\033[3A")                        # line 2 : move cursor 4 lines up
            sys.stdout.write("\rEnter Password => \033[K")     # \033[K : clear anything on right side of the cursor
            sys.stdout.write("\r")                             # line 2: coulum 0
            del password
            password = ""       # make the password empty again

print("")         
print(f"\n\nPassword is => {password}")
    