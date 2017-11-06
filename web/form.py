from django import forms


class Sign_up(forms.Form):
    username = forms.CharField(error_messages={"required":'用户名不能为空'})
    password = forms.CharField(
        max_length=20,
        min_length=8,
        error_messages={"required":'密码不能为空',
                        "min_length":"密码长度不能小于8",
                        'max_length':'密码长度不能大于20'},
        show_hidden_initial=True,

    )
    email = forms.EmailField(error_messages={"required":'邮箱不能为空','invalid':'邮箱格式错误'})

