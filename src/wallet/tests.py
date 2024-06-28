"""Tests for the wallet app."""

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Transaction, Wallet


class WalletTestCase(TestCase):
    """Test cases for the Wallet model."""

    def setUp(self):
        """Create a wallet for testing."""
        self.wallet = Wallet.objects.create(label="Test Wallet")

    def test_wallet_creation(self):
        """Test wallet creation."""
        self.assertEqual(self.wallet.label, "Test Wallet")
        self.assertEqual(self.wallet.balance, 0)

    def test_transaction_creation(self):
        """Test transaction creation."""
        Transaction.objects.create(wallet=self.wallet, txid="tx1", amount=100)
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, 100)

    def test_negative_balance(self):
        """Test that a transaction with a negative amount raises a ValidationError."""
        with self.assertRaises(ValidationError):
            Transaction.objects.create(wallet=self.wallet, txid="tx2", amount=-200)
