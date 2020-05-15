from django.urls import path
from django.contrib import admin

from photos.views import PhotoView
from feedback.views import FeedbackView

urlpatterns = [
    path('', PhotoView.as_view(), name="home"),
    path('feedback/', FeedbackView.as_view(), name="feedback"),
    path('admin/', admin.site.urls),
]
