from typing import Protocol
 
 
class Cart:
    def __init__(self, total: float):
        self.total = total
 
 
class PaymentMethod(Protocol):
    def pay(self, amount: float) -> str:
        ...
 
 
class CardPayment:
    def pay(self, amount: float) -> str:
        print("Simulating card validation...")
        fee = amount * 0.02
        total = amount + fee
        print(f"Processing fee: Rs. {fee:.2f}")
        return f"Card payment successful: Rs. {total:.2f}"
 
 
class UPIPayment:
    def pay(self, amount: float) -> str:
        print("Simulating UPI verification...")
        discount = min(amount * 0.05, 100)
        total = amount - discount
        print(f"UPI discount: Rs. {discount:.2f}")
        return f"UPI payment successful: Rs. {total:.2f}"
 
 
class WalletPayment:
    def __init__(self, balance: float):
        self.balance = balance
 
    def pay(self, amount: float) -> str:
        print("Checking wallet balance...")
        if self.balance < amount:
            return "Payment failed: Insufficient balance"
        self.balance -= amount
        print(f"Remaining balance: Rs. {self.balance:.2f}")
        return f"Wallet payment successful: Rs. {amount:.2f}"
 
 
def checkout(cart: Cart, method: PaymentMethod) -> str:
    print(f"\nCart total: Rs. {cart.total}")
    return method.pay(cart.total)


class ExternalPaymentGateway:
    def pay(self, amount: float) -> str:
        fee = amount * 0.03
        total = amount + fee
        print(f"Service charge: Rs. {fee:.2f}")
        return f"External payment successful: Rs. {total:.2f}"

class NetBankingPayment:
    def pay(self, amount: float) -> str:
        fee = 10
        total = amount + fee
        return f"Net Banking successful: Rs. {total:.2f}"


 
 
cart = Cart(1500)
print(checkout(cart, CardPayment()))
print(checkout(cart, UPIPayment()))
print(checkout(cart, WalletPayment(2000)))

print(checkout(cart, ExternalPaymentGateway()))
print(checkout(cart, NetBankingPayment()))

