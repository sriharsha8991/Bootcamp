class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, description, transaction_type):
        self.transactions.append({
            'amount': amount,
            'description': description,
            'type': transaction_type
        })
        return f"Added {transaction_type}: {amount} - {description}"

    def get_transactions(self):
        return self.transactions
