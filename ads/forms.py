from django import forms
from django.contrib.sites import requests
from django.forms import ModelForm, BooleanField, CharField, TextInput
from ads.models import Ads, Reply
from ckeditor_uploader.fields import RichTextUploadingFormField


class AdsForm(ModelForm):
    check_box = BooleanField(label='Accept')
    content = RichTextUploadingFormField()

    class Meta:
        model = Ads
        fields = ['category', 'tittle', 'content', 'check_box']


class ReplyForm(ModelForm):
    comment = CharField(max_length=144,
                        label='Comment',
                        label_suffix='Maximal leght 144 symbols')
    check_box = BooleanField(label='Accept')

    class Meta:
        model = Reply
        fields = ['comment', 'check_box']
