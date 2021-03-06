from django import template

from meeting_guide.settings import get_display_flags

register = template.Library()


@register.inclusion_tag("meeting_guide/tags/meeting_guide.html", takes_context=True)
def meeting_guide(context):
    """
    Display the ReactJS drive Meeting Guide list.
    """
    settings = {
        "mapbox_key": context["mapbox_key"],
        "display_flags": ", ".join(
            [f"'{x}'" for x in get_display_flags()]
        ),
    }

    return settings
