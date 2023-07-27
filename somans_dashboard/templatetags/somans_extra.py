from django import template
from django.urls import reverse

from somans_dashboard.constants import DARK, DARK_THEME, LIGHT_THEME, LIGHT
from somans_dashboard.models import AppTheme

register = template.Library()


@register.simple_tag(takes_context=True)
def brand_counter(context, num):
    brand = context.get("count_brand")
    return brand[num - 1]


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/buttons/new-workstation-app-button.html",
    takes_context=True,
)
def new_vs_old_workstation_app(context):
    title = None
    wks_value = context.get("new_workstation_software")
    wks_alert = 'bg-danger' if wks_value > 0 else 'bg-success'

    return dict(
        title=title,
        wks_alert=wks_alert,
        wks_value=wks_value,
    )


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/buttons/new-workstation-app-button.html",
    takes_context=True,
)
def new_workstation_app(context):
    title = None
    wks_value = context.get("no_nw_sft_wks")
    wks_alert = 'bg-danger' if wks_value > 0 else 'bg-success'

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
    svr_value = context.get("no_nw_sft_svr")
    svr_alert = 'bg-danger' if svr_value > 0 else 'bg-success'
    return dict(
        title=title,
        svr_alert=svr_alert,
        svr_value=svr_value,
    )


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/buttons/new-server-app-button.html",
    takes_context=True,
)
def new_vs_old_server_app(context):
    title = None
    svr_value = context.get("new_server_software")
    svr_alert = 'bg-danger' if svr_value > 0 else 'bg-success'
    return dict(
        title=title,
        svr_alert=svr_alert,
        svr_value=svr_value,
    )


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/buttons/new-server-app-button.html",
    takes_context=True,
)
def svr_inc_dtls_tag(context):
    title = None
    svr_value = context.get("no_svr_inc_dtls")
    svr_alert = 'bg-danger' if svr_value > 0 else 'bg-success'
    return dict(
        title=title,
        svr_alert=svr_alert,
        svr_value=svr_value,
    )


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/buttons/new-server-app-button.html",
    takes_context=True,
)
def wks_inc_dtls_tag(context):
    title = None
    svr_value = context.get("no_wks_inc_dtls")
    svr_alert = 'bg-danger' if svr_value > 0 else 'bg-success'
    return dict(
        title=title,
        svr_alert=svr_alert,
        svr_value=svr_value,
    )


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/scripts.html",
    takes_context=True,
)
def js_scripts(context):
    title = None
    return dict(
        title=title,
    )


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/buttons/theme_button.html",
    takes_context=True,
)
def theme_mode(context, url=None):
    title = None
    theme_mode = DARK
    theme_name = DARK_THEME
    current_usr = context.get('user')
    current_theme = AppTheme.objects.filter(theme_user=current_usr)
    if current_theme is None:
        theme_name = DARK_THEME
        theme_mode = theme_mode
    elif current_theme:
        thm = list(current_theme.values())[0]
        if thm['theme_mode'] == LIGHT:
            theme_name = DARK_THEME
            theme_mode = DARK
        else:
            theme_name = LIGHT_THEME
            theme_mode = LIGHT
    next = url_name(url)
    uri = f'?name={theme_name}&mode={theme_mode}&next={next}'
    return dict(
        title=title,
        theme_name=theme_name,
        theme_url=uri,
    )


def url_name(url):
    url_name = url.split('/')
    return url_name[-2]


@register.simple_tag(takes_context=True)
def get_theme(context, theme='light'):
    current_usr = context.get('user')
    if current_usr.is_authenticated:
        current_theme = AppTheme.objects.filter(theme_user=current_usr)
        theme = list(current_theme.values())[0]['theme_mode'] if current_theme else LIGHT
    return theme


@register.inclusion_tag(
    f"somans_dashboard/bootstrap/header/user_theme.html",
    takes_context=True,
)
def theme_user_mode(context):
    current_usr = context.get('user')
    current_theme = AppTheme.objects.filter(theme_user=current_usr)
    if current_theme:
        theme = list(current_theme.values())[0]['theme_mode']
        usr_theme = theme
    else:
        usr_theme = LIGHT

    return dict(
        usr_theme=usr_theme,
    )
