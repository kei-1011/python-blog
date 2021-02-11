from django import forms

class PostForm(forms.Form):
  title = models.CharField(max_length=30, label='タイトル')
  content = models.CharField(label='内容',widget=forms.Textarea())
