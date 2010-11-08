from django import template
import famfam


register = template.Library()

@register.inclusion_tag('famfam/icon.html')
def famfam_silk(icon):
    url = "%s%s.png" % (famfam.FAMFAM_SILK_ROOT, icon)
    return {
        "url":url,
        "icon":icon,
        "width":16,
        "height":16,
    }

@register.inclusion_tag('famfam/icon.html')
def famfam_mini(icon):
    url = "%s%s.gif" % (famfam.FAMFAM_MINI_ROOT, icon)
    return {
        "url":url,
        "icon":icon,
        "width":16,
        "height":16,
    }

@register.inclusion_tag('famfam/icon.html')
def famfam_flags(icon):
    url = "%s%s.png" % (famfam.FAMFAM_FLAGS_ROOT, icon)
    return {
        "url":url,
        "icon":icon,
        "width":16,
        "height":11,
    }

@register.inclusion_tag('famfam/icon.html')
def famfam_mint(icon):
    url = "%s%s.png" % (famfam.FAMFAM_MINT_ROOT, icon)
    return {
        "url":url,
        "icon":icon,
        "width":11,
        "height":11,
    }
