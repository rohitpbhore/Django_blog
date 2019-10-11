from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'content',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Row(
        Column('title', css_class='form-group col-md-6 mb-0'),
        css_class='form-row'
      ),
      Row(
        Column('content', css_class='form-group col-md-6 mb-0'),
        css_class='form-row'
      ),
      Submit('submit', 'Save')
    )
