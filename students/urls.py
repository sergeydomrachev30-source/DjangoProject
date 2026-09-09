from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('example/', views.example_view, name='example'),
    path('index/', views.index, name='index'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/', views.student_list, name='student_list'),
    path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('student_detail/<int:student_id>/<int:year>/', views.student_detail, name='student_detail'),
    path('mymodel/list/', views.MyModelListView.as_view(), name='mymodel_list'),
    path('mymodel/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/detail/<int:pk>/', views.MyModelDetailView.as_view(), name='mymodel_detail'),
    path('mymodel/update/<int:pk>/', views.MyModelUpdateView.as_view(), name='mymodel_update'),
    path('mymodel/delete/<int:pk>/', views.MyModelDeleteView.as_view(), name='mymodel_delete'),

]
