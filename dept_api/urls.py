from django.urls import path
from dept_api.views import Live_view


urlpatterns = [
    path('', Live_view.as_view()),
]