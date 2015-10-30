# -*- coding: utf-8 -*-

from brandcaptcha.resources import BrandcaptchaValidator

from django.template import Library
register = Library()


@register.inclusion_tag('brandcaptcha_tag.html')
def brandcaptcha_tag():
    return {
        'url': BrandcaptchaValidator().get_url(),
    }
