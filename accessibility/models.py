"""
accessibility/models.py
"""

from django.db import models

from accessibility.accessibility import ACCESSBILITY_FEATURE
from moared.models import moaredModel


class DefaultAccessibility(moaredModel):
    """
    DefaultAccessibilityModel
    """

    feature = models.CharField(max_length=100, choices=ACCESSBILITY_FEATURE)
    filter = models.JSONField()
    exclude_all = models.BooleanField(default=False)
