from django.urls import path

from .views import GetPostSensorsView, GetPatchSensorView, PostMeasurementView

urlpatterns = [
    path('sensors/', GetPostSensorsView.as_view()),
    path('sensors/<id>/', GetPatchSensorView.as_view()),
    path('measurements/', PostMeasurementView.as_view()),
]
