from django.conf.urls import url
from app1 import views

app_name = 'app1'

urlpatterns = [
    url(r'^$',views.EmployeeListView.as_view(),name= 'list'),
    #url(r'^(?P<pk>[-\W]+)/$',views.EmployeeDetailView.as_view(),name= 'detail')
    url(r'^(?P<pk>\d+)/$',views.EmployeeDetailView.as_view(),name='detail'),
    url(r'^update/(?P<pk>\d+)/$',views.EmployeeListView.as_view(),name='update'),
]
