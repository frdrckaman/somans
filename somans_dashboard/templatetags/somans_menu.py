from django import template

register = template.Library()


# @register.inclusion_tag(
#     f"somans_dashboard/bootstrap/menu/main-menu.html",
#     takes_context=True,
# )
# def main_menu(context):
#     title = None
#     return dict(
#         title=title,
#     )


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


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/menu/main-menu.html",
    takes_context=True,
)
def main_menu(context):
    software_active = None
    servers_active = None
    workstations_active = None
    menu_category = context.get('menu_category')
    if menu_category == 'software':
        software_active = "top-menu--active"
    elif menu_category == 'servers':
        servers_active = "top-menu--active"
    elif menu_category == 'workstations':
        workstations_active = "top-menu--active"

    return dict(
        software_active=software_active,
        servers_active=servers_active,
        workstations_active=workstations_active,
    )
