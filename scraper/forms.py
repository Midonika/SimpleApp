from django import forms
from django.core.validators import RegexValidator

url_validator = RegexValidator("^http[s]?://?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",
                               "The url format is incorrect. Correct and try again!")


class UrlForm(forms.Form):
    url = forms.CharField(required=True, validators=[url_validator], label="Url address")
