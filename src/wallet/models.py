"""Models for wallet app."""

from django.core.exceptions import ValidationError
from django.db import models


class Wallet(models.Model):
    """Wallet model."""

    label = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=36, decimal_places=18, default=0)

    def __str__(self):
        """Return str representation of the model."""
        return self.label


class Transaction(models.Model):
    """Transaction model."""

    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=36, decimal_places=18)
    wallet = models.ForeignKey(Wallet, related_name="transactions", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Override the save method to update the wallet balance."""
        if self.pk is None:
            new_balance = self.wallet.balance + self.amount
            if new_balance < 0:
                raise ValidationError("Wallet balance cannot be negative")
            self.wallet.balance = new_balance
            self.wallet.save()

        super().save(*args, **kwargs)

    def __str__(self):
        """Return str representation of the model."""
        return self.txid
