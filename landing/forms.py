from bootstrap.forms import BootstrapForm, Fieldset
from django import forms


class FeedbackForm(BootstrapForm):
    class Meta:
        layout = (
            Fieldset("Send your feedback", "name", "message", ),
        )

    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea())