import pandas as pd

users = []
account_numbers = []
default_acc = 100000
account_numbers.append(default_acc)
columns = ["Name", "Surname", "Email", "Number", "Balance", "Account Number"]
#df = pd.DataFrame(columns=columns)                            # This is done already, i dont need it now
df = pd.read_csv("All_Users.csv")
 
def userSettings():
    print("\nUser Setttings\n")
    print("1. Change pin")
    print("")

    
def createAcc(existing_df):
    name = input("Enter user name: ")
    surname = input("Enter your surname: ")
    email  = input("Enter email: ")
    number = input("Enter phone number: ")
    balance = 0.0

        # Getting account Number
    last_account = df.iloc[-1]["Account Number"]
    account_number = (last_account + 1)
    account_numbers.append(account_number)

    user_info = {"Name": name, "Surname": surname, "Email": email, "Number": number, "Balance": balance, "Account Number": account_number}
    user_info_df = pd.DataFrame([user_info])
    updated_df = pd.concat([existing_df, user_info_df], ignore_index=True)
    return updated_df

def update_df():
    global df
    df = createAcc(df)
    df.to_csv("All_Users.csv", index=False)
    print("Account created successfully!")
    
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
        
