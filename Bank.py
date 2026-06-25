import pandas as pd
import os
import hashlib
import json 

users = []
account_numbers = []
default_acc = 100000
ATM_CONFIG_FILE = "atm_config.json"
DEFAULT_ATM_CASH = 5000.0
account_numbers.append(default_acc)
columns = ["Name", "Surname", "Email", "Number", "Balance", "Account Number", "Pin"]
#df = pd.DataFrame(columns=columns)                            # This is done already, i dont need it now
df = pd.read_csv("All_Users.csv")

# Initializing the ATM cash Vault
if not os.path.exists(ATM_CONFIG_FILE):
    atm_data = {"vault_cash": DEFAULT_ATM_CASH}
    with open(ATM_CONFIG_FILE, "w") as f:
        json.dump(atm_data, f, indent=4)
else:
    with open(ATM_CONFIG_FILE, "r") as f:
        atm_data = json.load(f)

# Helper functions for the ATM cash Vault
def get_atm_vault_cash():
    with open(ATM_CONFIG_FILE, "r") as f:
        data = json.load(f)
    return data["vault_cash"]

def update_atm_vault_cash(new_amount):
    data = {"vault_cash": new_amount}
    with open(ATM_CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def userSettings():
    while True:
        print("\n1. Change Pin")
        print("2. Change email")
        print("3. Change Number")
        print("4. Back to previous Menu")

        try:
            option = int(input("\nChoose an Option: "))

            if option == 1:
                print("Change Pin")
            
            elif option == 2:
                print("Change Email")
            
            elif option == 3:
                print("Change Number")
            
            elif option == 4:
                return
            
            else:
                print("\nInvalid option. Choose a valid option")
        
        except ValueError as e:
            print(f"Invalid input! Error: {e}")

def hash_pin(pin_string):
    return hashlib.sha256(pin_string.encode()).hexdigest()
    
def createAcc(existing_df):
    name = input("Enter user name: ")
    surname = input("Enter your surname: ")
    email  = input("Enter email: ")
    number = input("Enter phone number: ")
    balance = 0.0

        # Getting account Number
    last_account = df.iloc[-1]["Account Number"]
    #last_account = account_numbers[-1]
    account_number = (last_account + 1)
    account_numbers.append(account_number)
    print(f"Your account number is: {account_number}")
    pin = input("Create a 4-digit security PIN: ")
    hashed_pin = hash_pin(pin)

    user_info = {"Name": name, "Surname": surname, "Email": email, "Number": number, "Balance": balance, "Account Number": account_number, "Pin": hashed_pin}
    user_info_df = pd.DataFrame([user_info])
    updated_df = pd.concat([existing_df, user_info_df], ignore_index=True)
    return updated_df

def update_df():
    global df
    df = createAcc(df)
    df.to_csv("All_Users.csv", index=False)
    print("Account created successfully!")

def search(target_acc):
    global df

    if df.empty:
        return None
    
    left = 0
    right = len(df) - 1

    while left <= right:
        mid_index = (left + right)//2
        current_acc = df.iloc[mid_index]["Account Number"]

        if df.iloc[mid_index]["Account Number"] == target_acc:
            return mid_index
        
        elif df.iloc[mid_index]["Account Number"] < target_acc:
            left = mid_index + 1
        
        else:
            right = mid_index - 1
    
    return None 

def authenticate():
    global df
    try: 
        acc_num = int(input("Enter Account number: "))
    except ValueError:
        print("Invalid account number format.")
        return None
    
    user_index = search(acc_num)

    if user_index is None:
        print("Account Number not found")
        return None
    
    user_row = df.iloc[user_index]

    pin_attempt = input("Enter your pin: ")
    hashed_attempt = hash_pin(pin_attempt)

    if hashed_attempt == user_row["Pin"]:
        #print(f"Access Granted. Welcome back, {user_row['Name']}")
        return user_index
    
    else:
        print("Incorrect Pin! Access Denied.")

def deposit(user_index):
    global df

    balance = df.iloc[user_index]["Balance"]

    try:
        amount = float(input("How much would you like to deposit: "))
    except ValueError as e:
        print(f"Invalid input! Error: {e}")
    new_balance = balance + amount
    print(f"Successfully deposited R{amount} to your account!")

    current_vault = get_atm_vault_cash()
    new_vault = (current_vault + amount)
    update_atm_vault_cash(new_vault)

    df.at[user_index, "Balance"] = new_balance
    df.to_csv("All_Users.csv", index=False)
    
    
def withdraw():
    print("\nWithdraw Money")
    
def transfer():
    print("\nTransfer Money")

def getStatement():
    print("\nGet Statement")

def print_users():
    global df
    print("===== Registered ====")
    print(df)

def log_in():
    user_index = authenticate()

    if user_index is None:
        return
    
    global df
    print(f"\nWelcome back {df.iloc[user_index]["Name"]}")
    print(f"\nBalance: {df.iloc[user_index]["Balance"]:.2f}")
    
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Get Statement")
        print("5. User Settings")
        print("6. Main Menu")

        try:
            option = int(input("Choose an option: ")) 
            
            # All these functions only run when user is authenticated...
            if option == 1:
                deposit(user_index)

            elif option == 2:
                withdraw(user_index)

            elif option == 3:
                transfer(user_index)

            elif option == 4:
                getStatement(user_index)
                
            elif option == 5:
                userSettings()

            elif option == 6:
                print("Back to Main menu!")
                return

            else:
                print("Invalid option. Select a Valid Option.")

        except ValueError as e:
            print(f"Invalid option! Error: {e}")