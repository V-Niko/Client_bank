import json
import os
import re
from random import randint
from datetime import datetime

username = '1'


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def client():
    print("*************************************")
    print("=<< 1. Create new bank account    >>=")
    print("=<< 2. Check Account Details      >>=")
    print("=<< 3. Logout                     >>=")
    print("*************************************")
    choice = input(f'Select your choice number from the above menu: ')
    if choice == "1":
        create()
    elif choice == "2":
        account()
    elif choice == "3":
        file = open('user_session.txt', 'r+')
        file.truncate()
        file.close()
        welcome()
    else:
        print('Wrong input')
        client()


def create():
    name_correct = False
    while name_correct == False:
        name = str(input(f"Enter buyer's name"))
        if len(name) > 4:
            if not name.isalpha():
                print('Only alphabets are allowed')
                name_correct = False
            else:
                name_correct = True
        else:
            print('Name should be longer than four characters')
            name_correct = False
    balance_correct = False
    while balance_correct == False:
        try:
            balance = float(input('Enter opening balance'))
            balance_correct == True
            break
        except ValueError:
            print('Only numbers allowed')
            balance_correct == False
    acc_type_correct = False
    while acc_type_correct == False:
        acc_type = input(f"Enter account type(Savings or Current)")
        if acc_type.upper() == "SAVINGS":
            acc_type_correct = True
        elif acc_type.upper() == "CURRENT":
            acc_type_correct = True
        else:
            print('Enter account type(Savings or Current)')
            acc_type_correct = False
    email_correct = False
    while email_correct == False:
        email = input('Enter email')
        regex = '^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$'
        if re.search(regex, email):
            email_correct = True
        else:
            email_correct = False
    number = random_with_N_digits(10)
    buyer_file_data = []
    buyer_banking_data = {
        username: [
            {
                'Account name': name.title(),
                'Opening Balance': balance,
                'Account Type': acc_type.title(),
                'Account email': email,
                'Account Number': number,
            }
        ],
    }
    print(f"An account with account number {number} has been opened for {name}")
    if os.stat('buyer.txt').st_size == 0:
        buyer_file_data.append(buyer_banking_data)
        with open('buyer.txt', 'w') as obj:
            json.dump(buyer_file_data, obj)
    else:
        with open('buyer.txt') as obj:
            data = json.load(obj)
            data.append(buyer_banking_data)
            with open('buyer.txt', 'w') as obj:
                json.dump(data, obj)
    client()


def account():
    try:
        collect_number = int(input(f"\nEnter buyer's account number: "))
        with open('buyer.txt') as file_obj:
            data = json.load(file_obj)
            found_flag = False
        for user_data in data:
            for user_data_key in user_data.keys():
                for user_details in user_data[user_data_key]:
                    if collect_number in user_details.values():
                        found_flag = True
                        print('\nAccount Found ! See details below:')
                        print(user_details)
                        client()
        if found_flag == False:
            print('\nAccount Not Found! You can register a new one if you wish.')
            client()
    except ValueError:
        print('Only integers are allowed')
        client()


def exit():
    file = open('buyer.txt', 'r+')
    file.truncate()
    file.close()
    print("Thank you for using our banking system!")


def login():
    print(f"Enter Details")
    username = input("Please enter your username")
    password = input(f'Please enter your password')
    with open('client.txt') as json_file:
        data = json.load(json_file)
        while (username != (data['client 1']['Username']) or password != (data['client 1']['Password'])) and (
                username != (data['client 2']['Username']) or password != (data['client 2']['Password'])):
            print('Username or password not found')
            login()
        else:
            print(f'Welcome {username}')
            login = datetime.now()
            login = login.strftime("%d:%m:%Y %H:%M:%S")
            session_data = {
                'Present User': username,
                'Login Time': login,
            }
            with open('user_session.txt', 'w') as file_object:
                json.dump(session_data, file_object)
            client()


def welcome():
    #print("=====================================")
    print("     ----Welcome to SNBank----       ")
    #print("*************************************")
    print("=<< 1. Client Login                >>=")
    print("=<< 2. Close App                  >>=")
    #print("*************************************")
    choice = input(f'Select your choice number from the above menu :')
    if choice == "1":
        login()
    elif choice == "2":
        exit()
    else:
        print('Wrong input')
        welcome()

welcome()