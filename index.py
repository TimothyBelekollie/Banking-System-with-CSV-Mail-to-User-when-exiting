import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class BankSystem:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def save_to_csv(self):
        with open('transactions.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for transaction in self.transactions:
                writer.writerow([transaction])

    def send_email(self, to_email):
        subject = "Bank Transactions"
        body = "Please find attached the transaction details in CSV format."

        msg = MIMEMultipart()
        msg['From'] = "your_email@gmail.com"
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach CSV file
        with open('transactions.csv', 'r') as file:
            attachment = MIMEText(file.read())
            attachment.add_header('Content-Disposition', 'attachment', filename='transactions.csv')
            msg.attach(attachment)

        # Send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login("belekollietimothy2@gmail.com", "shsx nvkc lgnw yybz")
            server.sendmail("belekollietimothy2@gmail.com", to_email, msg.as_string())

if __name__ == "__main__":
    bank = BankSystem()

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Display Transactions\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter the deposit amount: $"))
            bank.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the withdrawal amount: $"))
            bank.withdraw(amount)
        elif choice == '3':
            bank.display_balance()
        elif choice == '4':
            bank.display_transactions()
        elif choice == '5':
            bank.save_to_csv()
            email_address = "belekollietimothy2@gmail.com"
            bank.send_email(email_address)
            print(f"Transaction details sent to {email_address}. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
