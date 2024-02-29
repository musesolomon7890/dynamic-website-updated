from django.contrib import admin
from django.urls import path
from myapp.views  import index, contact, store, about
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact.html', contact, name='contact'),
    path('store.html', store, name='store'),
    path('about.html', about, name='about'),
    path('', index, name = 'index'),
    path('index.html', index, name = 'index'),
  
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
