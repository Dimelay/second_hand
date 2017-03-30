from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

from django.contrib import admin
urlpatterns = [
url(r'^login/$', views.user_login, name='login'),
url(r'^logout/$', views.user_logout, name='logout'),
#url(r'^product/(?P<pid>\w+)/$', views.get_product, name='get_product'),
url(r'^product/(?P<pid>\w+\.0)/(?P<rev>[0-1])/$', views.get_product, name='get_product'),
url(r'^sale/$', views.sale_product, name='sale_product'),
url(r'^history/$', views.history, name='history'),
#url(r'^cart/', views.cart, name='cart'),
url(r'^$', views.index, name='index'),
url(r'^admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
