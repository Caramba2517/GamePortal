from django.forms import ModelForm, BooleanField, CharField, ChoiceField
from ads.models import Reply, Ads


class ReplyForm(ModelForm):
    ad = ChoiceField()

    class Meta:
        model = Reply
        fields = ['ad']