from django import template

register = template.Library()

@register.filter
def currency_format(value):
    """Format numbers as currency (e.g., $12,450)."""
    try:
        value = int(value)  # Ensure it's an integer
        return f"${value:,}"  # Format with commas
    except (ValueError, TypeError):
        return value  # Return as is if not a number
