from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
''' using as _ means we can now call
    gettext_lazy() using _().
    It's effectively an alias
'''


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = ('Remove')
    initial_text = ('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'