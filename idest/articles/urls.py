from django.urls import path,re_path
from articles import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'articles'

urlpatterns = [
    ###path("",views.IndexView.as_view(),name='index'),
    path("musicindex",views.MusicIndexView.as_view(),name='musicindex'),
    path("",views.MusicIndexView.as_view(),name='index'),
    path('articlelist',views.PostListView.as_view(),name='articlelist'),
    path('post/<int:pk>/',views.ArticlePostDetailView.as_view(),name='post_detail'),
    path('post/create/',views.CreateArticleView.as_view(),name='post_new'),
    path('post/<int:pk>/update/',views.UpdateArticleView.as_view(),name="post_update"),
    path('post/<int:pk>/delete/',views.DeletePostView.as_view(),name='post_delete'),
    path('post/drafts/', views.DraftArticleView.as_view(),name='draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),
    path('aboutus',views.AboutUsView.as_view(),name='about'),
    path('comingsoon',views.ComingSoonView.as_view(),name='comingsoon'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)