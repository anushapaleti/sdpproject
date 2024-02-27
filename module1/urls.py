from django.contrib import admin
from django.urls import path
from .views import*

'''urlpatterns = [
    path('admin/', admin.site.urls),
]'''
urlpatterns=[
    path("hello2/",hello1),
    path('hello/',hello,name='hello'),#here name is optional
    path('',homepage,name='homepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',printtoconsole,name="printtoconsole"),
    path('p/',print1,name="print1"),
    path('h/',ran,name="ran"),
    path('context/',random123,name='random123'),
    path('d/',getdate1,name='getdate1'),
    path('date/',get_date,name='get_date'),
    path('tz/',tzfunctionlogic,name='tzfunctionlogic'),
    path('r/',reg,name='reg'),
    path('reg/',registerloginfunction,name='registerloginfunction'),#(/admin) type in urls to see the database
    path('pie/',pie_chart,name='pie_chart'),
    path('fam/',fam,name='fam'),
    path('w/',weatherpagecall,name='weatherpagecall'),
    path('weather/',weatherlogic,name='weatherlogic'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
]
