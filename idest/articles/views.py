from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.timezone import now

from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from articles.models import ArticlePost,Comment
from articles.forms import ArticlePostForm,CommentForm

from rest_framework import filters

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class MusicIndexView(ListView):
    model = ArticlePost
    template_name = 'articles/music_index.html'
    context_object_name='posts'

    filter_backends = [filters.SearchFilter]
    search_fields = ['title','tags','text','publish_date']

    def get_queryset(self):
        return ArticlePost.objects.filter(publish_date__lte=now()).order_by('-publish_date')[0:5]


class AboutUsView(TemplateView):
    template_name = 'about.html'

class ComingSoonView(TemplateView):
    template_name = 'comingsoon.html'

class PostListView(ListView):
    model = ArticlePost
    template_name='articles/articlepost_list.html'
    context_object_name='posts'

    filter_backends = [filters.SearchFilter]
    search_fields = ['title','tags','text','publish_date']
    
    def get_queryset(self):
        return ArticlePost.objects.filter(publish_date__lte=now()).order_by('-publish_date')

class ArticlePostDetailView(DetailView):
    model = ArticlePost

class CreateArticleView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'article/articlepost_detail.html'

    form_class = ArticlePostForm

    model = ArticlePost

class UpdateArticleView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'article/articlepost_detail.html'

    form_class = ArticlePostForm
    model = ArticlePost
    #fields = ('title','text','featured_image')

class DeletePostView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    redirect_field_name = 'article/articlepost_detail.html'

    model = ArticlePost
    fields = '__all__'
    success_url = reverse_lazy('articles:articlelist')

class DraftArticleView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'article/articlepost_detail.html'
    context_object_name = 'drafts'
    
    template_name='articles/articlepost_draft_list.html'
    model = ArticlePost
    fields = '__all__'

    def get_queryset(self):
        return ArticlePost.objects.filter(publish_date__isnull=True).order_by('create_date')


#############################
#############################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(ArticlePost,pk=pk)

    post.publish()
    return redirect('articles:post_detail',pk=pk)


def add_comment_to_post(request,pk):
    post = get_object_or_404(ArticlePost,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('articles:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'articles/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('articles:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('articles:post_detail',pk=post_pk)


