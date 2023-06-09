from django.urls import path
from  .views import PostListView,PostDetailView,PostEditView,PostDeleteView,CommentDeleteView,ProfileView,ProfileEditView,AddFollower,\
    RemoveFollower,AddLike,AddDislike,UserSearch,ListFollowers
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post_edit/<int:pk>',PostEditView.as_view(),name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('test/<int:id>/',views.test,name="test"),
    path('post/<int:post_pk>/comment/delete/<int:pk>/',CommentDeleteView.as_view(),name="comment-delete"),
    path('profile/<int:pk>/',ProfileView.as_view(),name="profile"),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add',AddFollower.as_view(),name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='list-followers'),


]