from django import forms

from mainapp.models import ProductCategory
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'image')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control py-4'


class UserAdminProfileForm(UserProfileForm):

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


class CategoryUpdateFormAdmin(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    # description = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}), required=False)
    # is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-control py-4"}))
    discount = forms.IntegerField(widget=forms.NumberInput(),label='скидка',required=False,min_value=0,max_value=90,
                                  initial=0)

    class Meta:
        model = ProductCategory
        # exclude =()
        fields = ("name", "description",'discount')

    def __init__(self, *args, **kwargs):
        super(CategoryUpdateFormAdmin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'