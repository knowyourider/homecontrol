from django import forms

class ControlForm(forms.Form):
    """
    docstring for ControlForm
    """
    ACTIONS = (
        ('1','1 - Open'),
        ('2','2 - Close'),
        ('3','3 - Stop'),
    )
    action = forms.ChoiceField(
        choices = ACTIONS,
        widget  = forms.RadioSelect,
        required=True,
    )
