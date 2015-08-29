from django import forms
from django.utils import six
from djangular.forms import NgDeclarativeFieldsMetaclass, NgModelFormMixin


class PostForm(six.with_metaclass(NgDeclarativeFieldsMetaclass, NgModelFormMixin, forms.Form)):
    title = forms.CharField(max_length=200)
