from django import forms 
from .models import Form 
#creating my own forms
class Regform(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'
        labels ={
            'first_ name':'FIRST NAME',
            'last_ name':'LAST NAME',
            'email':'EMAIL',
            'number':'PHONE NUMBER',
            'state':'STATE OF ORIGIN',
            'dob':'DATE OF BIRTH',
            'address':'HOUSE ADDRESS',
            'course':'COURSE DESIRED',
            'reg_date':'REGISTRATION DATE',
            'start_date':'RESUMPTION DATE',
        }
        
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter a valid email'}))
    # number = forms.IntegerField(widget=forms.IntegerField(attrs={'class':'form-control','placeholder':'Enter your Phone number'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your state of origin'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Your date of birth'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your house address'}))
    #course = forms.Select(widget=forms.Select(attrs={'class':'form-control'}))
    reg_date = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Registration date'}))
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Resumption date'}))