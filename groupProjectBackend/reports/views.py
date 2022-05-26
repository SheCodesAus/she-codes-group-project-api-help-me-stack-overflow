from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reports
from .serializers import ReportsSerlializer
from django.http import Http404
from rest_framework import status


class ReportList(APIView):


    def get_object(self, pk):
        try:
            return Reports.object.get(pk=pk)
        except Reports.DoesNotExist:
            raise Http404

    def get(self, request):
        reports = Reports.objects.all()
        serializer = ReportsSerlializer(reports, many=True)
        return Response(
            serializer.data)

    
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

class ReportDetail(APIView):

    def get_object(self, pk):
        try:
            return Reports.objects.get(pk=pk)
        except Reports.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        report = self.get_object(pk)
        serializer = ReportsSerlializer(report)
        return Response(serializer.data)

    def put(self, request, pk):
        report = self.get_object(pk)
        data = request.data
        serializer = ReportsSerializer(
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()


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