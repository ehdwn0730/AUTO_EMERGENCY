from django.contrib import admin
from django.urls import path
from board.views import blog, rescuer, finish, video, control, detail, call
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    path('blog/rescuer/', rescuer, name='rescuer'),
    path('finish/', finish, name='finish'),
    path('blog/rescuer/', video, name='video'),
    path('control/', control, name='control'),
    path('control/detail', detail, name='detail'),
    path('call/', call, name="call"),
    path('control/detail/', video, name='video'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)