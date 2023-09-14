from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import School
from .serializers import SchoolSerializer

@api_view(['GET'])
def school_list(request):
    schools = School.objects.all()
    name = request.GET.get('name')
    district = request.GET.get('district')
    region = request.GET.get('region')
    location = request.GET.get('location')

    if name:
        schools = schools.filter(name__icontains=name)
    if district:
        schools = schools.filter(district__icontains=district)
    if region:
        schools = schools.filter(region__icontains=region)
    if location:
        schools = schools.filter(location__icontains=location)
    serializer = SchoolSerializer(schools, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def school_detail(request, pk):
    school = School.objects.get(pk=pk)
    serializer = SchoolSerializer(school)
    return Response(serializer.data)
