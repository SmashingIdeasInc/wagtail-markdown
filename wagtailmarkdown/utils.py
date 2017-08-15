# vim:sw=4 ts=4 et:
# Copyright (c) 2015 Torchbox Ltd.
# felicity@torchbox.com 2015-09-14
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely. This software is provided 'as-is', without any express or implied
# warranty.
#

from django.utils.safestring import mark_safe
from markdown import markdown
from bleach import clean

from wagtailmarkdown.base_configurations import markdown_config, bleach_config


def render(text, markdown_custom={}, bleach_custom={}):
    mc = markdown_config()
    bc = bleach_config()

    mc.update(markdown_custom)
    bc.update(bleach_custom)

    return mark_safe(
        clean(
            markdown(text, **mc),
            **bc
        )
    )
