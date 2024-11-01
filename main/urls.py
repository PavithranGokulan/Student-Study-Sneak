from django.urls import path,reverse
from . import views
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete

urlpatterns=[
    path("",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("logout",views.logoutpage,name="logout"),
    path("source",views.source,name="source"),
    path("notes",views.notes,name="notes"),
    path("noteapp",views.noteapp,name="noteapp"),
    path("delete_document/<int:docid>",views.delete_document, name="delete_document"),
    path("timer",views.timer,name="timer"),
    path("create_remainder",views.create_remainder,name="create"),
    path('remainders',views.remainder_list,name='list'),
    #path("add_note",views.add_note,name="add_note"),
    path("calender",views.calender,name="calender"),
    path('tasks',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>',TaskDetail.as_view(),name='task'),
    path('task-create',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name='task-delete'),
]   