from django import template

register = template.Library()


@register.inclusion_tag(
    f"idap_finservices/bootstrap/buttons/status_icon.html",
    takes_context=True,
)
def FinStatusIcon1(context, counter):
    ls1 = []
    s_status1 = context.get('s_status_node1'),
    for status1 in s_status1:
        ls1.append(status1)
    ls_status1 = ls1[0]

    if counter in [9, 11, 20]:
        theme1 = 'bg-dark'
        icon1 = 'chevron-down'
        icon_text1 = 'text-primary'
        sv_status1 = 'Down'
    else:
        if ls_status1[counter] == 'UP':
            theme1 = 'bg-success'
            icon1 = 'chevron-up'
            icon_text1 = 'text-primary'
            sv_status1 = 'Up'
        else:
            theme1 = 'bg-danger'
            icon1 = 'chevron-down'
            sv_status1 = 'Down'
            icon_text1 = 'text-danger'

    return dict(
        theme=theme1,
        icon=icon1,
        icon_text=icon_text1,
        sv_status=sv_status1,
    )


@register.inclusion_tag(
    f"idap_finservices/bootstrap/buttons/status_icon.html",
    takes_context=True,
)
def FinStatusIcon2(context, counter):
    ls2 = []
    s_status2 = context.get('s_status_node2'),
    for status2 in s_status2:
        ls2.append(status2)
    ls_status2 = ls2[0]

    if ls_status2[counter] == 'UP':
        theme2 = 'bg-success'
        icon2 = 'chevron-up'
        icon_text2 = 'text-primary'
        sv_status2 = 'Up'
    else:
        theme2 = 'bg-danger'
        icon2 = 'chevron-down'
        icon_text2 = 'text-danger'
        sv_status2 = 'Down'

    return dict(
        theme=theme2,
        icon=icon2,
        icon_text=icon_text2,
        sv_status=sv_status2
    )


@register.inclusion_tag(
    f"idap_finservices/bootstrap/buttons/time_stamp.html",
    takes_context=True,
)
def FinStatusTime1(context):
    return {"time_stamps": context.get('s_status_node1')[len(context.get('s_status_node1')) - 2]}


@register.inclusion_tag(
    f"idap_finservices/bootstrap/buttons/time_stamp.html",
    takes_context=True,
)
def FinStatusTime2(context):
    return {"time_stamps": context.get('s_status_node2')[len(context.get('s_status_node2')) - 2]}
