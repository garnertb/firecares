import autocomplete_light.shortcuts as al
from .models import Address
from firecares.firestation.models import FireDepartment

al.register(Address,
    # Just like in ModelAdmin.search_fields
    search_fields=['^address_line1', 'city', 'state_province', 'postal_code'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Address',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 100,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)

al.register(FireDepartment,
    # Just like in ModelAdmin.search_fields
    search_fields=['name'],
    attrs={
        # This will set the input placeholder attribute:
        'placeholder': 'Fire Department',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    },
    # This will set the data-widget-maximum-values attribute on the
    # widget container element, and will be set to
    # yourlabs.Widget.maximumValues (jQuery handles the naming
    # conversion).
    widget_attrs={
        'data-widget-maximum-values': 100,
        # Enable modern-style widget !
        'class': 'modern-style',
    },
)
