"""load_wallet.py
Defines the LoadWallet class used to manage a prepaid load balance.
"""


class LoadWallet:
    """A prepaid load wallet for one subscriber."""

    # Service charge for sending load to a different network (in pesos)
    SERVICE_FEE = 1.00

    def __init__(self, owner_name, mobile_number, starting_balance=0.0):
        self.owner_name = owner_name
        self.mobile_number = mobile_number
        # Leading underscore: the balance is "private" (encapsulation).
        # It should only be changed through the methods below. 
        self._balance = float(starting_balance)

    # ---------- helper methods ----------
    def get_balance(self):
        """Return the current balance (read-only access)."""
        return self._balance

    @staticmethod
    def is_valid_number(number):
        """A valid mobile number has 11 digits and starts with 09."""
        return number.isdigit() and len(number) == 11 and number.startswith("09")

    # ---------- main features ----------
    def top_up(self, amount):
        """Add load to the wallet."""
        if amount <= 0:
            print("Invalid amount. Top up must be greater than 0.")
            return False
        self._balance += amount
        print(f"Top up successful! Added P{amount:.2f}.")
        return True

    def send_load(self, recipient_number, amount):
        """Send load to another number on the SAME network (no fee)."""
        if not self.is_valid_number(recipient_number):
            print("Invalid mobile number. Use 11 digits starting with 09.")
            return False
        if recipient_number == self.mobile_number:
            print("You cannot send load to your own number.")
            return False
        if amount <= 0:
            print("Invalid amount. Amount must be greater than 0.")
            return False
        if amount > self._balance:
            print("Insufficient balance.")
            return False

        self._balance -= amount
        print(f"Sent P{amount:.2f} to {recipient_number} (same network).")
        return True

    def send_with_fee(self, recipient_number, amount):
        """Send load to a DIFFERENT network. A service charge is added."""
        if not self.is_valid_number(recipient_number):
            print("Invalid mobile number. Use 11 digits starting with 09.")
            return False
        if recipient_number == self.mobile_number:
            print("You cannot send load to your own number.")
            return False
        if amount <= 0:
            print("Invalid amount. Amount must be greater than 0.")
            return False

        total = amount + self.SERVICE_FEE
        if total > self._balance:
            print(f"Insufficient balance. You need P{total:.2f} "
                  f"(amount + P{self.SERVICE_FEE:.2f} fee).")
            return False

        self._balance -= total
        print(f"Sent P{amount:.2f} to {recipient_number} (different network).")
        print(f"Service charge: P{self.SERVICE_FEE:.2f} | Total deducted: P{total:.2f}")
        return True

    def show_balance(self):
        """Display the wallet details and current balance."""
        print("\n----- Wallet Info -----")
        print(f"Owner         : {self.owner_name}")
        print(f"Mobile Number : {self.mobile_number}")
        print(f"Balance       : P{self._balance:.2f}")
        print("-----------------------")
