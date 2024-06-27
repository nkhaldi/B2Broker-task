"""Serializers for Wallet and Transaction models."""

from rest_framework_json_api import serializers

from .models import Transaction, Wallet


class WalletSerializer(serializers.ModelSerializer):
    """Wallet serializer."""

    class Meta:
        """Meta class for Wallet serializer."""

        model = Wallet
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    """Transaction serializer."""

    class Meta:
        """Meta class for Transaction serializer."""

        model = Transaction
        fields = "__all__"
