from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from api_app.serializer import BedSerializer
from api_app.models import BedAvailability

# Create your views here.

class BedViewAPI(viewsets.ModelViewSet):
	serializer_class = BedSerializer
	lookup_field = "id"
	lookup_url_kwarg = "id"

	def list(self, request):
		queryset = BedAvailability.objects.all().order_by('type', 'id')
		status = request.GET.get('status', None)
		_type = request.GET.get('type', None)

		if status:
			queryset = queryset.filter(status=status)
		if _type:
			queryset = queryset.filter(type=_type)

		serializer = self.get_serializer(queryset, many=True)
		data = serializer.data
		return Response(data)

	def get_queryset(self):
		queryset = BedAvailability.objects.all()
		return queryset
