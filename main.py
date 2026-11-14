"""main.py
Menu program for the Cellphone Load Wallet.
Run this file:  python main.py
"""

from load_wallet import LoadWallet


def ask_amount(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def create_wallet():
    """Ask the user for details and return a new LoadWallet."""
    print("=== Create Your Load Wallet ===")
    name = input("Owner name: ").strip()

    number = input("Mobile number (e.g. 09171234567): ").strip()
    while not LoadWallet.is_valid_number(number):
        print("Invalid number. Use 11 digits starting with 09.")
        number = input("Mobile number: ").strip()

    balance = ask_amount("Starting balance: P")
    while balance < 0:
        print("Starting balance cannot be negative.")
        balance = ask_amount("Starting balance: P")

    print("\nWallet created successfully!")
    return LoadWallet(name, number, balance)


def show_menu():
    print("\n===== CELLPHONE LOAD WALLET =====")
    print("1. Top up load")
    print("2. Send load (same network)")
    print("3. Send load with fee (different network)")
    print("4. Check balance")
    print("5. Exit")


def main():
    wallet = create_wallet()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            amount = ask_amount("Amount to top up: P")
            wallet.top_up(amount)

        elif choice == "2":
            number = input("Recipient number: ").strip()
            amount = ask_amount("Amount to send: P")
            wallet.send_load(number, amount)

        elif choice == "3":
            number = input("Recipient number: ").strip()
            amount = ask_amount("Amount to send: P")
            wallet.send_with_fee(number, amount)

        elif choice == "4":
            wallet.show_balance()

        elif choice == "5":
            print(f"Thank you, {wallet.owner_name}! Goodbye.")
            break

        else:
            print("Invalid choice. Please pick 1-5.")


if __name__ == "__main__":
    main()
