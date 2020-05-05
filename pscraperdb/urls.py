from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import include, path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('pscraper.urls')),
    path('api/v1/docs/', include_docs_urls(title='Pscraper API')),
    path('', lambda r: HttpResponseRedirect('api/v1/docs/')),
]
