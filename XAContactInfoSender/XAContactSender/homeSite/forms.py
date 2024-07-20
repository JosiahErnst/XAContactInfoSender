from django import forms

class Student(forms.Form):
    
    # All of the inputs for the student to submit to be sent
    first_name = forms.CharField(required = True, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(required = True, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "Last Name"})) 
    email = forms.CharField(required = True, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "Email"}))
    phone = forms.CharField(required = True, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "Mobile Number"})) 
    church = forms.CharField(required = True, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "Home Church"}))
    churchLocation = forms.CharField(required = True, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "Church City"}))
    pastor = forms.CharField(required = True, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "Youth Pastor"}))
    gradYear = forms.IntegerField(required = True, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "High School Graduation Year"}))
    major = forms.CharField(required = True, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "Possible Major"}))   
    
    # The list of collge choices for students to pick from
    CHOICES = [
        ('1', 'Northern Michigan University'),
        ('2', 'Michigan Tech University'),
        ('3', 'UW Eau Claire'),
        ('4', 'UW Green Bay'),
        ('5', 'UW La Crosse'),
        ('6', 'UW Madison'),
        ('7', 'UW Milwaukee'),
        ('8', 'UW Oshkosh'),
        ('9', 'UW River Falls'),
        ('10', 'UW Stevens Point'),
        ('11', 'UW Superior'),
        ('12', 'Undecided'),
        ('13', 'Not Listed'),
    ]
    
    # The next three variables are the three sections where a student can choose their top three
    # colleges in order from first to third
    First_Choice_College = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    Second_Choice_College = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    Third_Choice_College = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES, 
    )
    
    # An optional input if a student chooses that their desired college is not listed
    ifNotListed = forms.CharField(required = False, label = "", 
                    widget = forms.widgets.TextInput(attrs = {"class": "form-control", "placeholder": "If you selected 'Not Listed', please enter your desired colleges here"}))