from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import Account
from animal.models import Animal

# Define your lists and variables here

CONNECT_STATUS = (
    ('accepted', 'accepted'),
    ('denied', 'denied'),
    ('on-hold', 'on-hold'),
    ('paid', 'paid'),
    ('finished', 'finished'),
)

VERY_BAD = 1
BAD = 2
GOOD = 3
EXCELLENT = 4
VERY_EXCELLENT = 5

RATE_CHOICES = (
    (VERY_BAD, _('Very Bad')),
    (BAD, _('Bad')),
    (GOOD, _('Good')),
    (EXCELLENT, _('Excellent')),
    (VERY_EXCELLENT, _('Very Excellent')),
)


class Connect(models.Model):
    sender_user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='sender_user',
        verbose_name=_('connect sender user')
    )
    receiver_user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='receiver_user',
        verbose_name=_('connect receiver user')
    )
    sender_animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='sender_animal',
        verbose_name=_('connect sender animal')
    )
    receiver_animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        related_name='receiver_animal',
        verbose_name=_('connect receiver animal'),
        null=True,
        blank=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('connect date created')
    )
    desc = models.TextField(
        max_length=255,
        verbose_name=_('connect description')
    )
    status = models.CharField(
        choices=CONNECT_STATUS,
        max_length=255,
        verbose_name=_('connect status')
    )
    first_confirm = models.BooleanField(
        default=False,
        verbose_name=_('first confirm')
    )
    second_confirm = models.BooleanField(
        default=False,
        verbose_name=_('second confirm')
    )
    is_chat = models.BooleanField(
        default=False,
        verbose_name=_('connect is chat')
    )
    paid = models.BooleanField(default=False)
    closed_by = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True, related_name='closed_chat_rooms')

    def __str__(self):
        return self.sender_animal.name

class ConnectRate(models.Model): 
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATE_CHOICES, default=2)
    connect = models.ForeignKey(Connect, on_delete=models.CASCADE) 
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('rate date created')
    )
    preview_in_page = models.BooleanField(_("preview_in_page"), default=False)

    def __str__(self):
        return f'Rate for {self.connect} Connect by {self.user}'
