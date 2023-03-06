from django.db import models
from django.utils.translation import gettext_lazy as _


class TgUser(models.Model):
    first_name = models.CharField(max_length=128, verbose_name=_('Name'), blank=True, null=True)
    last_name = models.CharField(max_length=128, verbose_name=_('Surname'), blank=True, null=True)
    tg_username = models.CharField(max_length=256, verbose_name=_('username'), blank=True, null=True)
    tg_id = models.BigIntegerField(verbose_name=_('telegraam id'), unique=True)
    
    def __str__(self) -> str:
        return 'tg_id: {} | name: {}'.format(self.tg_id, self.first_name)
    
    class Meta:
        verbose_name = _('telegram user')
        verbose_name_plural = _('telegram users')
