from django import forms


class StudentForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class TeacherForm(forms.Form):
    Tusername = forms.CharField(label="用户名", max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Tpassword = forms.CharField(label="密码", max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

