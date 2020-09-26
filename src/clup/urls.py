from django.contrib import admin
from django.urls import path

from posts.views import home_page_view, contact_page_view, about_us_page_view


urlpatterns = [
    path('', home_page_view),
    path('home/', home_page_view),
    path('admin/', admin.site.urls),
    path('contact/', contact_page_view),
    path('aboutus/', about_us_page_view)
]
