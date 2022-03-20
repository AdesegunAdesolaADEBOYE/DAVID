from django.urls import path
from django.views.generic import TemplateView


app_name = 'event'


urlpatterns = [
    path('', TemplateView.as_view(template_name="event/index.html")),
    path('cv/', TemplateView.as_view(template_name="event/event.html")),
]

