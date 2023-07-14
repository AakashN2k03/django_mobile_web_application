from django.urls import path
from .import views

urlpatterns=[
    path("",views.home,name='home'),
    path("login_view",views.login_view,name='login_view'),
     path("content",views.content,name='content'),
     path("logindup",views.logindup,name='logindup'),
      path("logout",views.logout,name='logout'),
        path("collection1",views.collection1,name='collection1'),
       path("collection2",views.collection2,name='collection2'),
         path("collection3",views.collection3,name='collection3'),
          path("collection4",views.collection4,name='collection4'),
           path("collection5",views.collection5,name='collection5'),
           path("search",views.search,name='search'),
           path("payment",views.payment,name='payment'),
            path("tq",views.tq,name='tq'),

]