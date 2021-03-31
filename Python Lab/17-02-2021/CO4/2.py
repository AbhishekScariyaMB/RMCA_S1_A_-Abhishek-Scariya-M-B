class BankAccount:
    def __init__(self,a,n,t,b):
        self.acno=a
        self.name=n
        self.type=t
        self.bal=b
    def deposit(self,a):
        self.bal+=a
        print('Rs.',a,'deposited! Current balance is: Rs.',self.bal)
    def withdraw(self,a):
        if self.bal >= a:
            self.bal-=a
            print('Rs.',a,'withdrawn! Current balance is: Rs.', self.bal)
        else:
            print('Insufficient balance to make this transaction!')
a=int(input('Enter account number:'))
n=input('Enter name of the account holder: ')
t=input('Enter account type: ')
b=float(input('Enter your balance:'))
ac1=BankAccount(a,n,t,b)
ac1.deposit(float(input('Enter amount to deposit: ')))
ac1.withdraw(float(input('Enter amount to withdraw: ')))