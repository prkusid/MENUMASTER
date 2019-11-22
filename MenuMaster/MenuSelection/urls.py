from django.urls import path
from MenuSelection import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('measurement_items/<menu_item>', views.measurement_items),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
