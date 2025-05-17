"""
moared_automations/filters.py
"""

from moared.filters import moaredFilterSet, django_filters
from moared_automations.models import MailAutomation


class AutomationFilter(moaredFilterSet):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"
