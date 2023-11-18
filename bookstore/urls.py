from django.contrib import admin
from django.urls import path, include

import books

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", include('books.urls'))
]
