from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer

class GetPostSensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        data = SensorDetailSerializer(sensors, many=True)
        return Response(data.data)
    
    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        Sensor.objects.create(name=name, description=description)
        return Response({'status': f"Sensor {name} with description - '{description}' create"})

class GetPatchSensorView(APIView):
    def get(self, request, id):
        sensor = Sensor.objects.get(id=id)
        data = SensorDetailSerializer(sensor)
        return Response(data.data)
    
    def patch(self, request, id):
        name = request.data.get('name')
        description = request.data.get('description')
        before = Sensor.objects.get(id=id)
        if name:
            Sensor.objects.filter(id=id).update(name=name)
        if description:
            Sensor.objects.filter(id=id).update(description=description)
        after = Sensor.objects.get(id=id)
        return Response({'status': f"Data '{before}' replaced by '{after}'"})
    
class PostMeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer()

    def post(self, request):
        sensor = request.data.get('sensor')
        temperature = request.data.get('temperature')
        Measurement.objects.create(sensor=Sensor.objects.get(id=sensor), temperature=temperature)
        return Response({'status': f"Measurement for sensor {sensor} with temperature - '{temperature}' create"})