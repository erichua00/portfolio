
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import blog.views

urlpatterns = [
    path('erichua/secure/secure/secure/admin', admin.site.urls),
    path("",jobs.views.home,name='home'),
    #path("blog/", include('blog.urls')),
    path("win10optimize/", blog.views.win10optimize, name='win10optimize'),
    path("win10optimize/step_1", blog.views.step_1, name='step_1'),
    #path("win10optimize/step_2", blog.views.step_2, name='step_2'),
    #path("win10optimize/step_3", blog.views.step_3, name='step_3'),
    #path("win10optimize/step_4", blog.views.step_4, name='step_4'),
    #path("win10optimize/step_5", blog.views.step_5, name='step_5'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
