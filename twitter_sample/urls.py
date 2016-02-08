from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', TemplateView.as_view(template_name='app/index.html')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
]
