from django import forms
from .models import Article, Comment
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["author","title", "content"]
        
        widgets = {
            # 'status':forms.Select(attrs={'class': 'form-control'}),
            # 'category':forms.Select(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Username'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add A Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add Your Article'}),
        }
        
   
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ["article","comment_author", "comment_content"]
        
#         widgets = {
#             'article': forms.Select(attrs={'class': 'form-control'}),
#             'comment_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
#             'comment_content': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Comment'}),
#         }
