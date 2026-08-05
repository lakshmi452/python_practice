from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Credit Card payment of", amount, "completed")
class UPIPayment(Payment):
    def pay(self, amount):
        print("UPI payment of", amount, "completed")
class CashPayment(Payment):
    def pay(self, amount):
        print("Cash payment of", amount, "completed")
p1 = CreditCardPayment()
p2 = UPIPayment()
p3 = CashPayment()
p1.pay(1500)
p2.pay(750)
p3.pay(300)