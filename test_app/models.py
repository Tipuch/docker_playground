from django.db import models
from django.utils.translation import ugettext_lazy as _


class TestModel(models.Model):
    test_field = models.CharField(_("Test Field"), max_length=100)
