from django import forms
from articles.models import ArticlePost, Comment

class ArticlePostForm(forms.ModelForm):

    class Meta():
        model = ArticlePost
        fields = ('author','title','text','featured_image','tags')
    
        widgets = {
            "title":forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

