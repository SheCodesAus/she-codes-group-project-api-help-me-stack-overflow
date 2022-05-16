from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Programs
from .serializers import ProgramsSerializer

# Programs listing functions. View list of programs using get and create programs using post
class ProgramsList(APIView):

    def get(self, request):
        programs = Programs.objects.all()
        serializer = ProgramsSerializer(programs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProgramsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# Programs detail view. View details of a program on a single page ie. programs/1/
class ProgramsDetail(APIView):

    def get_object(self, pk):
        try:
            return Programs.objects.get(pk=pk)
        except Programs.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        programs = self.get_object(pk)
        serializer = ProgramsSerializer(programs)
        return Response(serializer.data)
