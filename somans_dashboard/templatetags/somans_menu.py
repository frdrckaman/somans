from django import template

register = template.Library()


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/menu/main-menu.html",
    takes_context=True,
)
def main_menu(context):
    title = None
    return dict(
        title=title,
    )


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/menu/mobile-menu.html",
    takes_context=True,
)
def mobile_menu(context):
    title = None
    return dict(
        title=title,
    )


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/menu/top-bar-menu.html",
    takes_context=True,
)
def top_bar_menu(context):
    title = None
    return dict(
        title=title,
    )
