class atm (object):
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    def cash_withdrawal(self):
        print("withdrawal limit is 200")
    def check_balance(self):
        print("there is £4000 left")
    def sending_cash(self):
        print("how much would you like to send")
bank = atm("5738596", "8796", )
print(bank.pin)