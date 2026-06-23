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
from Bank import  createAcc, update_df, print_users, deposit, withdraw, transfer, userSettings

if __name__ == "__main__":

    while True: 
        print("ATM Machine")
        print("1. Create an Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. User Settings")
        print("6. Views users")
        print("7. Exit")

        try: 
            option = int(input("\nChoose an option: "))

            if option == 1: 
                update_df()
            
            elif option == 2: 
                deposit()
            
            elif option == 3:
                withdraw()
            
            elif option == 4:
                transfer()
            
            elif option == 5:
                userSettings()
            
            elif option == 6:
                print_users()
            
            elif option == 7:
                print("Exiting...")
                break

            else:
                print("Invalid option. Select right option..")
        
        except ValueError as e: 
            print(f"Invalid input error as: {e}")