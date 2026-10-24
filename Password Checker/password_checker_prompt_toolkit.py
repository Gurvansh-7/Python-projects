# it is finilized version

from prompt_toolkit import PromptSession
from prompt_toolkit.validation import Validator
import string

session = PromptSession()       # session is the object of the class promptSession()

def check(password):            # check the conditions
    checks = {"Atleast 8 characters" : len(password) >= 8,
              "Capital letter" : any(i.isupper() for i in password),
              "Small letter" : any(i.islower() for i in password),
              "Digit" : any(i.isdigit() for i in password),
              "Symbol" : any(i in string.punctuation for i in password)}
    return checks

password_validator = Validator.from_callable(           # tell lib whether to accept or reject input
    lambda password : all(check(password).values()),    # to check the conditon
    error_message= "Password requirement not met!",     # print if requirements are not meet
    move_cursor_to_end= True                            # input will not same until condition met
)

def get_password():             # to get the password and pass our function to the lib function
    def toolbar():              
        password = session.default_buffer.text          # read the input
        checks = check(password)
        passed = sum(checks.values())
        total = len(checks)

        return "\n".join(f"{name} {"✓" if valid else "✗"}"        # display
                         for name, valid in checks.items()
        ) + f"\n{passed} / {total}"         

    password = session.prompt(              # password is variable where input will store, prompt ask the input
        "Password: ",                       # it is what will show to user
        is_password= True,                  # for masking the password only on the screen
        bottom_toolbar= toolbar,            # pass toolbar to the lib function bottom_toolbar
        validator= password_validator       # pass password_validator ot lib function validator
        )
    return password

if __name__ == "__main__":
    password = get_password()
    print("Password entered")