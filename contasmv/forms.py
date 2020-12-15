from django import forms
from contasfin.models import ContasFin


class CtFinForm(forms.Form):
    ctfin = forms.ModelChoiceField(
        queryset=ContasFin.objects.all(),
        empty_label=None,
        label='Conta Financeira'
    )

    class Meta:
        fields = ('ctfin')