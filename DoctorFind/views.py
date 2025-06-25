from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer

@api_view(['GET'])
def doctor_list(request):
    city = request.GET.get('city', None)
    if city:
        doctors = Doctor.objects.filter(city__icontains=city)
    else:
        doctors = Doctor.objects.all()
    
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_doctor(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Doctor added successfully!', 'data': serializer.data}, status=201)
    return Response(serializer.errors, status=400)
