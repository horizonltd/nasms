from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


#Method is django define

class UserCreateForm(UserCreationForm):

    class Meta:
        fields  = ('username', 'email','password1','password2')
        model = get_user_model()
        # widgets={
        #     'subject': UserCreationForm.TextInput(attrs={'style': 'width:20px'}),
        #     'business': UserCreationForm.Select(attrs={'style': 'width:20px'})
        #     }          

#Setting up user label for Clark Name and Email
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Clark User Name'
        self.fields['email'].label = 'Email Address'
  
