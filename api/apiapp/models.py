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


class MiniCours(models.Model):
    start_date = models.DateField(verbose_name=_('start date'))
    end_date = models.DateField(verbose_name=_('end date'))
    start_time = models.TimeField(verbose_name=_('start time'))
    title = models.CharField(max_length=128, verbose_name=_('title'))
    backoffice_link = models.CharField(max_length=512, verbose_name=_('link'))

    def __str__(self) -> str:
        return f'{self.title} | {self.start_date} | {self.start_time}'
    
    class Meta:
        verbose_name = _('mini course')
        verbose_name_plural = _('mini courses')


class Student(models.Model):
    first_name = models.CharField(max_length=64, verbose_name=_('name'))
    last_name = models.CharField(max_length=64, verbose_name=_('surname'))
    parent_phone = models.CharField(max_length=32, verbose_name=_('parent pthone'))
    is_presence = models.BooleanField(default=False, verbose_name=_("presence"))
    course = models.ForeignKey(to=MiniCours, on_delete=models.PROTECT)

    def get_fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self) -> str:
        return self.get_fullname()
    
    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')
