from django import forms

class NewTaskForm(forms.Form):
    title = forms.CharField(
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Task Title"
            }
        )
    )
    
    description = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                "class": "form-control",
                "placeholder": "Task Description"
            }
        )
    )

    end_date = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats = (
                '%Y-%d-%m', '%d/%m/%Y', '%d/%m/%y', # '2006-25-10', '25/10/2006', '25/10/06' 
                '%d-%m-%Y','%d-%m-%y',              # '25-10-2006', '25-10-06'
                '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'               
                '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
        )
    )