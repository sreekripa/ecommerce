from django.urls import path
from . import views
app_name='ecommerce'

urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='Products_by_Category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodcatdetail,name='prodcatdetail'),
]