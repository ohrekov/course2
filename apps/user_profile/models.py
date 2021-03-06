from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        primary_key=True,
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    patronymic = models.CharField('По батькові', max_length=150, blank=True)
    company = models.ForeignKey('blog.Company', models.CASCADE, null=True, blank=True, verbose_name='Компанія')

    def get_full_name(self):
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.patronymic)
        return full_name.strip()
