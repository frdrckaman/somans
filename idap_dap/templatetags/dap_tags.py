import getpass
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag(
    f"idap_dap/bootstrap/button/dc_access_approve_btn.html",
    takes_context=True,
)
def dca_approve_btn(context, count):
    title = None
    admin_usr = str(settings.IDAP_ADMIN).split(",")
    usr = str(context.get('user'))
    admin = True if usr in admin_usr else False
    return dict(
        title=title,
        admin=admin,
        count=count,
        username=context.get('user'),
    )
