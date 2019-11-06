from django import forms
from .models import Commnet

import mistune


class CommentForm(forms.ModelForm):
    email = forms.CharField(
        label='邮箱',
        max_length=30,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )
    nickname = forms.CharField(
        label='昵称',
        max_length=10,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width: 60%;'},
        )
    )
    content = forms.CharField(
        label='内容',
        max_length=200,
        widget=forms.widgets.Textarea(
            attrs={'row': 3, 'cols': 40, 'class': 'form-control'}
        )
    )

    # website = forms.CharField(
    #     label='网站',
    #     max_length=100,
    #     widget=forms.widgets.URLInput(
    #         attrs={'class': 'form-control', 'style': 'width: 60%;'}
    #     )
    # )


    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('内容长度怎么能这么短呢！')
        content = mistune.markdown(content)
        return content

    class Meta:
        model = Commnet
        # fields = {'nickname', 'email', 'website', 'content'}
        fields = {'nickname', 'email', 'content'}