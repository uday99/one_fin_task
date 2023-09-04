"""movie_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.Register_user.as_view(),name='reg_user'),
    path('collection/',views.Create_collection_movie.as_view(),name='coll_movie'),
    path('collection/<collection_uuid>/',views.List_collections.as_view(),name='colls'),
    path('movies/',views.Movies_list.as_view(),name='mov_lst'),
    path('request-count/',views.Count_value_request.as_view(),name='rqst-cnt'),
    path('request-count/reset/',views.Count_request_reset.as_view(),name='cnt_reset')
]
