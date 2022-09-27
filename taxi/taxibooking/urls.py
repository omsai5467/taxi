from django.contrib import admin
from django.urls import path
from taxibooking import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",views.home),
    path("get",views.get),
    path("getcarDetails",views.getcar_details),
    path("bookcar",views.bookcar)
]