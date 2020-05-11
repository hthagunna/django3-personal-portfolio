#from django.contrib import admin
from django.urls import path
#from django.conf.urls.static import static
#from django.conf import settings
from . import views
app_name ='blog'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.all_blogs, name='all_blogs'),
    #path('blog/', include('blog.urls')),
    path('<int:blog_id>/', views.detail, name='detail'),

]
