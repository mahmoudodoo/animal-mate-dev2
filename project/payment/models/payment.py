from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import Account

PAYOUTREQUEST_STATUS = (
    ('1', 'Accepted'),
    ('2', 'Rejected'),
    ('3', 'Under Review'),
    ('4', 'Delayed')
)

class PayoutRequest(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Payout date')
    )
    status = models.CharField(
        choices=PAYOUTREQUEST_STATUS,
        max_length=255,
        default='3'
    )
    amount = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.get_status_display()
