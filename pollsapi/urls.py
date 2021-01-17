from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
	path('admin/', admin.site.urls),
	path(r'swagger-docs/', schema_view),
	path(r'docs/', include_docs_urls(title='Polls API')),

	re_path(r'^', include('polls.urls')),
]
