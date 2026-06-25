import pandas as pd
import os
import hashlib

users = []
account_numbers = []
default_acc = 100000
account_numbers.append(default_acc)
columns = ["Name", "Surname", "Email", "Number", "Balance", "Account Number", "Pin"]
#df = pd.DataFrame(columns=columns)                            # This is done already, i dont need it now
df = pd.read_csv("All_Users.csv")
 
def userSettings():
    user_index = authenticate()
    if user_index is None:
        return
    
    global df
    print(f"Welcome back {df.iloc[user_index]["Name"]}")

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

def deposit():
    print("\nDeposit Money")
    
def withdraw():
    print("\nWithdraw Money")
    
def transfer():
    print("\nTransfer Money")

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
    print(f"\nBalance: {df.iloc[user_index]["Balance"]}")
    
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. User Settings")
        print("5. Main Menu")

        try:
            option = int(input("Choose an option: ")) 

            if option == 1:
                deposit()

            elif option == 2:
                withdraw()

            elif option == 3:
                transfer()

            elif option == 4:
                userSettings()

            elif option == 5:
                print("Back to Main menu!")
                return

            else:
                print("Invalid option. Select a Valid Option.")

        except ValueError as e:
            print(f"Invalid option! Error: {e}")