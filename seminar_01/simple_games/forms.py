from django import forms


class ChooseGameForm(forms.Form):
    a_game = forms.ChoiceField(choices=[('0', 'Coin play'), ('1', 'Dice'), ('2', 'Random Number')])
    attempts = forms.IntegerField(min_value=1, max_value=64)
