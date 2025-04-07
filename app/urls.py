from django.urls import include, path

urlpatterns = [
    path("user/", include("app.user.urls")),
    path("photos/", include("app.photos.urls")),
]
