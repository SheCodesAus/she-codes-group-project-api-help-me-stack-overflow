from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reports
from .serializers import ReportsSerlializer

class ReportList(APIView):

    def get(self, request):
        reports = Reports.objects.all()
        serializer = ReportsSerlializer(reports, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        reports = Reports(data=request.data)
        if ReportsSerlializer.is_valid():
            ReportsSerlializer.save()
            return Response(ReportsSerlializer.data)



