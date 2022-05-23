from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reports
from .serializers import ReportsSerlializer
from django.http import Http404
from rest_framework import status


class ReportList(APIView):

    def get(self, request):
        reports = Reports.objects.all()
        serializer = ReportsSerlializer(reports, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
            )

    
    def post(self, request):
        serializer = ReportsSerlializer(data=request.data)
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

    def put(self, request, pk):
        reports = self.get_objects(pk)
        ReportList = request.data
        serializer = ReportsSerlializer(
            instance = project,
            data = data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReportDetail(APIView):

    def get_object(self, pk):
        try:
            return Reports.objects.get(pk=pk)
        except ReportsSerlializer.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        report = self.get_object(pk)
        serializer = ReportsSerlializer(report)
        return Response(serializer.data)

    def put(self, request):
        report = self.get_object(pk)
        data = request.data
        serializer = ReportsSerlializer(
            instance=report,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, pk):
        report = self.get_object(pk)
        serializer = ReportsSerlializer(data=request.data)
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

    def delete(self, request, pk):
        report = self.get_object(pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)