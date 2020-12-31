#from django import forms
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import XxnfTasks
from django.contrib.auth.models import User

#from bootstrap_datepicker_plus import DatePickerInput

class TasksForm(forms.ModelForm):
         
    class Meta:
        model = XxnfTasks
        fields = ['task_id', 'set_num', 'round_num', 'question_num', 'topic', 'description', 'owner', 'status', 'remarks']
        topics =    (
                        ('', 'Select Topic'),
                        ('Math', 'Math'),
                        ('Energy', 'Energy'),
                        ('Earth and Space Science', 'Earth and Space Science'),
                        ('Life Science', 'Life Science'),
                        ('Physical Science', 'Physical Science'),
                    )
        statuses = (
                        ('Entered', 'Entered'),
                        ('InProgress', 'InProgress'),
                        ('Completed', 'Completed'),
                        ('Cancelled', 'Cancelled'),
                        ('OnHold', 'OnHold'),
                    )
        widgets = {
             'set_num' : forms.TextInput(attrs={'style':'max-width:5em'}),
             'round_num' : forms.TextInput(attrs={'style':'max-width:5em'}),
             'question_num' : forms.TextInput(attrs={'style':'max-width:5em'}),
             'topic': forms.Select(choices=topics, attrs={'class': 'form-control', 'style':'max-width:15em'}),
             'description' : forms.TextInput(attrs={'style':'max-width:50em'}),            
             'status': forms.Select(choices=statuses, attrs={'class': 'form-control', 'style':'max-width:12em'}),
             'remarks' : forms.TextInput(attrs={'style':'max-width:30em'}),
             
        }

        labels = {
            "set_num": "Set",
            "round_num": "Round",
            "question_num": "Q#"
        }
 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('set_num', css_class='form-group col-md-0 mb-0'),
                Column('round_num', css_class='form-group col-md-0 mb-0'),
                Column('question_num', css_class='form-group col-md-0 mb-0'),
                Column('topic', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('description', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('owner', css_class='form-group col-md-1 mb-0'),
                Column('status', css_class='form-group col-md-1 mb-0'),
                Column('remarks', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit'),
        )
