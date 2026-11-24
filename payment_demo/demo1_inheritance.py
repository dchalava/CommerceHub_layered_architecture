class Cart:
    def __init__(self, total):
        self.total = total
 
 
class PaymentMethod:
    def pay(self, amount):
        ...
 
 
class CardPayment(PaymentMethod):
    def pay(self, amount):
        print("Simulating card validation...")
        fee = amount * 0.02
        total = amount + fee
        print(f"Processing fee: Rs. {fee:.2f}")
        return f"Card payment successful: Rs. {total:.2f}"
 
 
class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print("Simulating UPI verification...")
        discount = min(amount * 0.05, 100)
        total = amount - discount
        print(f"UPI discount: Rs. {discount:.2f}")
        return f"UPI payment successful: Rs. {total:.2f}"
 
 
class WalletPayment(PaymentMethod):
    def __init__(self, balance):
        self.balance = balance
 
    def pay(self, amount):
        print("Checking wallet balance...")
        if self.balance < amount:
            return "Payment failed: Insufficient balance"
        self.balance -= amount
        print(f"Remaining balance: Rs. {self.balance:.2f}")
        return f"Wallet payment successful: Rs. {amount:.2f}"
 
 
def checkout(cart, method: PaymentMethod):
    print(f"\nCart total: Rs. {cart.total}")
    return method.pay(cart.total)
 
class NetBankingPayment(PaymentMethod):
    pass
 


 
cart = Cart(1500)
print(checkout(cart, CardPayment()))
print(checkout(cart, UPIPayment()))
print(checkout(cart, WalletPayment(1000)))
print(checkout(cart, NetBankingPayment()))
