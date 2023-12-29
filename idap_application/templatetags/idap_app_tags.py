from django import template
from idap_application.models import ApplicationLinks

register = template.Library()


@register.inclusion_tag(
    f"idap_application/bootstrap/menus/prod.html",
    takes_context=True,
)
def AppLinkProd(context):
    env_name = 'PROD'
    prod_links = ApplicationLinks.objects.filter(app_env='prod')
    return dict(
        prod_links=prod_links,
        env_name=env_name,
    )


@register.inclusion_tag(
    f"idap_application/bootstrap/menus/dr.html",
    takes_context=True,
)
def AppLinkDr(context):
    env_name = 'DR'
    dr_links = ApplicationLinks.objects.filter(app_env='dr')
    return dict(
        dr_links=dr_links,
        env_name=env_name,
    )


@register.inclusion_tag(
    f"idap_application/bootstrap/menus/uat.html",
    takes_context=True,
)
def AppLinkUat(context):
    env_name = 'UAT'
    uat_links = ApplicationLinks.objects.filter(app_env='uat')
    return dict(
        uat_links=uat_links,
        env_name=env_name,
    )
