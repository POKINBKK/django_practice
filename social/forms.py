from django.forms import ModelForm
from django import forms
from .models import Status, Comment
from django.utils.translation import gettext_lazy as _

class StatusForm(ModelForm):
    class Meta:
        model = Status
        # fields = '__all__'
        exclude = ['writer']
        labels = {
            'topic': _('Statusname'),
        }
        help_texts = {
            'topic': _('Put your Post here'),
        }
        error_messages = {
            'topic': {
                'max_length': _("This post's name is too long."),
            },
        }
        widgets = {
            'date': forms.SelectDateWidget,
        }
    # def clean(self):
    #     cleaned_data = super().clean()
    #     topic = cleaned_data.get('topic')
    #
    #     if 'hello' not in topic:
    #         self.add_error('topic', 'please add \"hello\" to Topic')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

