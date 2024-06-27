"""Views for the wallet app."""

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework_json_api.filters import OrderingFilter
from rest_framework_json_api.pagination import JsonApiPageNumberPagination

from wallet.models import Transaction, Wallet
from wallet.serializers import TransactionSerializer, WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    """Wallet viewset."""

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    pagination_class = JsonApiPageNumberPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = "__all__"
    ordering_fields = "__all__"


class TransactionViewSet(viewsets.ModelViewSet):
    """Transaction viewset."""

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = JsonApiPageNumberPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = "__all__"
    ordering_fields = "__all__"
