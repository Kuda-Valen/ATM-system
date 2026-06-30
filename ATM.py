# ATM Machine system
"""
Features: 
PIN Authentication
Check Balance
Deposit Money
Withdraw Money
Change PIN
Mini Statement
"""

import datetime
from Bank import  update_df, log_in, forgot_pin

if __name__ == "__main__":

    while True: 
        print("\nATM Machine")
        print("1. Create an Account")
        print("2. Log In")
        print("3. Forgot Pin")
        print("5. Exit")

        try: 
            option = int(input("\nChoose an option: "))

            if option == 1: 
                update_df()
            
            elif option == 2: 
                log_in()

            elif option == 3:
                forgot_pin()
            
            #elif option == 4:
                #print_users()
            
            elif option == 5:
                print("Exiting...")
                break

            else:
                print("Invalid option. Select right option..")
        
        except ValueError as e: 
            print(f"Invalid input error as: {e}")