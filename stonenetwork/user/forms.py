from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User


class MOD_UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['nick', 'first_name', 'last_name', 'email']



class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("nick", "password")