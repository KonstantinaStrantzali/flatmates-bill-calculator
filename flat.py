class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmates:

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pay(self, bill, flatmate):
        weight = self.days_in_house / (self.days_in_house + flatmate.days_in_house)
        rent = bill.amount * weight
        return rent
