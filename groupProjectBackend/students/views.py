from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Students
from .serializers import StudentsSerializer, StudentsDetailSerializer

#Students listing function. Get a list of students and post to create new students
class StudentsList(APIView):

    def get(self, request):
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentsSerializer(data=request.data)
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

# Students detail view. View details of a program on a single page ie. students/1/
# put function to edit student detail
# del function to delete a single student
class StudentsDetail(APIView):

    def get_object(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        students = self.get_object(pk)
        serializer = StudentsSerializer(students)
        return Response(serializer.data)

    def put(self, request, pk):
        students = self.get_object(pk)
        data = request.data
        serializer = StudentsDetailSerializer(
            instance = students,
            data = data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.errors,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        students = self.get_object(pk)
        students.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

        



