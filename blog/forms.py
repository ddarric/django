from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        #Lenght same as Comment model max length
        max_length=60,
        #Text input widget
        widget=forms.TextInput(
            attrs={
            #css class
            "class": "form-control",
            #placeholder text
            "placeholder": "Your Name"
            }
        )
    )
    #Text area widget
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
            }
        )
    )