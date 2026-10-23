class Account:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def add_money(self, amount):
        if amount > 0:
            self.money = self.money + amount
            print("Money added successfully")
        else:
            print("Enter a valid amount")

    def show_details(self):
        print("Name:", self.name)
        print("Balance:", self.money)

A1 = Account("Amit", 2000)
A1.add_money(300)
A1.show_details()
