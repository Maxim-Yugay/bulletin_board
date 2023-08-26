from django.contrib.flatpages.admin import FlatPageAdmin
from django.utils.translation import gettext_lazy as _


class FlatPagesAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('enable_comments',
                        'registration_required',
                        'template_name'),
        }),
    )
