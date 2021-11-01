from django.contrib import admin
from django.urls import path
from api.views import (
    StudentList,
    StudentCreate,
    StudentRetrieve,
    StudentUpdate,
    StudentDestroy,
    StudentListCreate,
    StudentRetrieveUpdateDestroy
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student/', StudentList.as_view(), name='student-list'),
    # path('student/', StudentCreate.as_view(), name='student-create'),
    # path('student/<int:pk>/', StudentRetrieve.as_view(), name='student-retrieve'),
    # path('student/<int:pk>/', StudentUpdate.as_view(), name='student-update'),
    # path('student/<int:pk>/', StudentDestroy.as_view(), name='student-destroy'),
    path('student/', StudentListCreate.as_view(), name='student-list-create'),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroy.as_view(), name='student-retrieve-update-destroy'),
]

