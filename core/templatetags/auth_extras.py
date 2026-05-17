from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    """
    Vérifie si un utilisateur appartient à un groupe spécifique.
    Usage: {% if user|has_group:"Opérateurs" %}
    """
    if user.is_superuser:
        return True
    return user.groups.filter(name=group_name).exists()
