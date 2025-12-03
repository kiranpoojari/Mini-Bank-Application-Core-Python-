from dataclasses import dataclass, field
from datetime import datetime
import hashlib

@dataclass
class Transaction:
    type: str
    amount: float
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")

@dataclass
class Account:
    acc_no: str
    holder: str
    _balance: float = 0.0
    transactions: list = field(default_factory=list)
    _pin_hash: str = field(default="")

    @property
    def balance(self):
        return self._balance

    def add_transaction(self, ttype, amount):
        self.transactions.append(Transaction(ttype, amount))

    def set_pin(self, pin):
        self._pin_hash = hashlib.sha256(pin.encode()).hexdigest()

    def verify_pin(self, pin):
        if not self._pin_hash:
            return False
        return hashlib.sha256(pin.encode()).hexdigest() == self._pin_hash
