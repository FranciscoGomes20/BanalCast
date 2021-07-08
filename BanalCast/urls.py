from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('post/<int:poste_id>', views.post, name='post'),
    path('page-error', views.page_error, name='page-error'),
]