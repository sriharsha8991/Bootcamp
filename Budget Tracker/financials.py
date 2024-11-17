class FinancialManager:
    def __init__(self, transactions):
        self.transactions = transactions

    def calculate_balance(self):
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expense = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        return income - expense

    def generate_summary(self):
        summary = []
        for transaction in self.transactions:
            summary.append(f"{transaction['type'].capitalize()}: {transaction['amount']} - {transaction['description']}")
        return summary
