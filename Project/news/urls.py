from django.urls import path
from .views import PostList, PostDetail, NewsSearch, PostCreate, PostUpdate, PostDelete, CategoryListView, subscribe, \
   unsubscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', cache_page(60)(PostDetail.as_view()), name='post_detail'),
   path('search/', NewsSearch.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscriptions', subscribe, name='subscriptions'),
   path('categories/<int:pk>/unsubscriptions', unsubscribe, name='unsubscriptions')
]
