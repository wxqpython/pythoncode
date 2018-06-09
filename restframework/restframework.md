# restframework

## 基础

```
pip3 install djangorestframework
```

version: settings/urls/views/

```
#settings.py
INSTALLED_APPS = [
    #...
    'rest_framework',  # 友好显示TemplateDoesNotExist报错
]
REST_FRAMEWORK = {
    'ALLOWED_VERSIONS':['v1','v2'],
    'DEFAULT_VERSION':'v1',
}
```

```
# urls.py
from django.conf.urls import url
from app01 import views
urlpatterns = [
    url(r'^(?P<version>\w+)/user/$', views.UserView.as_view()),
    # url(r'^user/$', views.UserView.as_view()),
]
```

```
# views.py
# pip3  install djangorestframework
from django.shortcuts import render,HttpResponse,redirect

from django.views import View
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning,QueryParameterVersioning

class UserView(APIView):
    versioning_class = URLPathVersioning
    # versioning_class = QueryParameterVersioning

    def get(self,request,*args,**kwargs):
        print(request.version)
        self.dispatch
        return HttpResponse("user.get")

    def post(self,request,*args,**kwargs):
        return HttpResponse("user.post")
```


