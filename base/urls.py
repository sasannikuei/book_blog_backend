from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('products/', views.ProductListView.as_view(), name="products"),
    path('products/<int:pk>', views.getProduct, name="product"),
    path('form/', views.product_form_view, name='product_form'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)