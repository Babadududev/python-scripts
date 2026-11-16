class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    withdrawals = []
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        withdrawals.append(spent)
    
    total_spent = sum(withdrawals)
    percentages = [int((spent / total_spent) * 100) // 10 * 10 if total_spent > 0 else 0 for spent in withdrawals]
    
    chart = "Percentage spent by category\n"
    for line in range(100, -1, -10):
        chart += f"{line:>3}| "
        for pct in percentages:
            chart += "o  " if pct >= line else "   "
        chart += "\n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)
    
    for i in range(max_len):
        chart += "     "
        for name in names:
            char = name[i] if i < len(name) else " "
            chart += f"{char}  "
        if i < max_len - 1:
            chart += "\n"
            
    return chart
