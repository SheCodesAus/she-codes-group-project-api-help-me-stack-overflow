from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Reports
from .serializers import ReportsSerializer

class ReportList(APIView):
    def get(self, request):
        Reports = Reports.objects.all()

