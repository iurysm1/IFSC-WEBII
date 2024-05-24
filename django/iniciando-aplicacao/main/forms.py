from django import forms


class CreateNewList(forms.Form):
    name=forms.CharField(label="Name", max_length=200)


class CreateNewItemList(forms.Form):
    text=forms.CharField(label="Text", max_length=300)
    complete=forms.BooleanField(label="Complete", required=False)