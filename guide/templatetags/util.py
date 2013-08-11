from django import template
register = template.Library()

@register.filter()
def menu_active(path, item):
    """Add class="active" to a menu item if we're on that page
    This will work as long as APPEND_SLASH is True"""
    if len(path.split('/')) < 2:
        return ''
    last_piece = path.split('/')[-2]
    return 'class="active"' if last_piece == item else ''
