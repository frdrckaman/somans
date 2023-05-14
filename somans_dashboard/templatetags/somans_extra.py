from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def brand_counter(context, num):
    brand = context.get("count_brand")
    return brand[num-1]
