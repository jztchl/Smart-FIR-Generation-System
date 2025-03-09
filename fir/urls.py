from django.urls import path
from .views import FIRView

urlpatterns = [
    path("generate-fir/", FIRView.as_view(), name="generate_fir"),
]
