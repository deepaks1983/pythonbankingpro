import json


def dataLoad():
    with open('file.json') as f:
        data = json.loads("[" +
                          f.read().replace("}\n{", "},\n{") +
                          "]")
    data2 = {}
    for i in data:
        data2.update(i)
    return data2


class Bank:

    def __init__(self):
        option = int(input("Enter '1' for registration\nEnter '2' for login\n"))

        if option == 1:
            Registration()

        if option == 2:
            Login()

        else:

            Bank()


class Login:

    def __init__(self):
        dl = dataLoad()

        user_name = input('Enter the User Name: ')
        password = input('Enter the password: ')

        if user_name in dl.keys() and dl[user_name]['User_Password'] == password:
            print('User Logged in Successfully')
            print('Your Balance is ', dl[user_name]['Balance'])

            option = int(input("Enter '1' for Depositing\nEnter '2' for Withdrawal\n"))

            while True:
                if option == 1:
                    amount = int(input('Enter the amount to deposit: '))


                    dl[user_name]['Balance'] = dl[user_name]['Balance'] + amount

                    # Save the updated JSON object to the file
                    with open('file.json', 'w') as file:
                        file.write('{}\n'.format(json.dumps(dl)))

                    print(f"You Deposited Rs {amount}/- and Your balance is Rs {dl[user_name]['Balance']}/-")
                    break




                if option == 2:
                    amount = int(input('Enter the amount to withdraw: '))
                    if amount > dl[user_name]['Balance']:
                        print('Not enough balance to withdraw')
                        continue

                    else:
                        dl[user_name]['Balance'] = dl[user_name]['Balance'] - amount

                        with open('file.json', 'w') as file:
                            file.write('{}\n'.format(json.dumps(dl)))
                        print(f"You Withdraw Rs {amount}/- and Your balance is Rs {dl[user_name]['Balance']}/-")
                        break



        else:
            print('User Credentials does not Match or Invalid User')
            Login()


class Registration:

    def __init__(self):

        dl = dataLoad()

        Bank_DB = {}

        print('Please enter the details')
        login_name = input('Enter the login Name: ')

        if login_name in dl.keys():

            print('Already this user name taken')
            Registration()

        else:

            Bank_DB[login_name] = {}
            user_password = input('Enter the password: ')
            Beneficiary_name = input('Enter your Name: ')
            phone_no = input('Enter the Phone Number: ')

            Bank_DB[login_name]['LoginName'] = login_name
            Bank_DB[login_name]['User_Password'] = user_password
            Bank_DB[login_name]['Beneficiary_Name'] = Beneficiary_name
            Bank_DB[login_name]['Phone_No'] = phone_no
            Bank_DB[login_name]['Balance'] = 0

            while Bank_DB == {}:
                break

            else:
                with open('file.json', 'a') as sample:

                    for dict in [Bank_DB]:
                        sample.write('{}\n'.format(json.dumps(dict)))


b = Bank()
