from pathlib import Path
current_dir = Path(__file__).resolve().parent


class Account:
    
    def __init__(self, account_number, name, balance = 0):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(account_number, int):
            raise TypeError("account_number must be an integer")
        if not isinstance(balance, (int, float)):
            raise TypeError("balance should be of (float,int)")
        
        self.account_number = account_number
        self.name = name 
        self.balance = balance
    
    def __repr__(self):
        return f"{self.account_number}, {self.name}, {self.balance}"
    

class Bank:

    def __init__(self, file_name):
        self.file_name = current_dir/file_name 
        self.load_from_file()

    
    def load_from_file(self):
        self.accounts = dict()
        self.__counter = 0
        try:
            with open(self.file_name, 'r') as f:
                for line in f:
                    acc_nu, name, bal = line.strip().split(', ')
                    acc_num = int(acc_nu)
                    self.accounts[acc_num] = Account(acc_num, name, float(bal))
                    self.__counter = max(self.__counter, acc_num)
            
            self.__counter += 1

        except:
            pass 
    
    def save_to_file(self):
        with open(self.file_name, 'w') as f:
            for acc in self.accounts.values():
                f.write(str(acc) + '\n')
    
    def create_account(self, name, initial_deposit = 0):
        self.accounts[self.__counter] = Account(self.__counter, name, initial_deposit)
        self.__counter += 1 
        self.save_to_file()
    
    def view_account_details(self, acc_num):
        if acc_num not in self.accounts.keys():
            print("No account found.")
        
        return self.accounts[acc_num]
    
    def deposit_money(self, acc_num, value):
        if not isinstance(value, (int,float)):
            raise TypeError("Value must be of (int,float)")
        
        if acc_num not in self.accounts.keys():
            print("No account found.")
        
        self.accounts[acc_num].balance += value 
        self.save_to_file()

    def withdraw_money(self, acc_num, value):
        if not isinstance(value, (int,float)):
            raise TypeError("Value must be of (int,float)")
        
        if acc_num not in self.accounts.keys():
            print("No account found.")
            return 
        if value > self.accounts[acc_num].balance:
            print("Not enough money!")
            return 
        
        self.accounts[acc_num].balance -= value 
        self.save_to_file()





# b = Bank("Accounts.txt")

# b.create_account("Husanboy", 100)
# b.withdraw_money(0, 20)
# print(b.view_account_details(0))