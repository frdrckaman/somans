from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def brand_counter(context, num):
    brand = context.get("count_brand")
    return brand[num-1]


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/buttons/new-workstation-app-button.html",
    takes_context=True,
)
def new_workstation_app(context):
    title = None
    wks_alert = 'bg-success'
    wks_value = context.get("new_workstation_software")
    if wks_value > 0:
        wks_alert = 'bg-danger'

    return dict(
        title=title,
        wks_alert=wks_alert,
        wks_value=wks_value,
    )


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/buttons/new-server-app-button.html",
    takes_context=True,
)
def new_server_app(context):
    title = None
    svr_alert = 'bg-success'
    svr_value = context.get("new_server_software")

    if svr_value > 0:
        svr_alert = 'bg-danger'
    return dict(
        title=title,
        svr_alert=svr_alert,
        svr_value=svr_value,
    )
