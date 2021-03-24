from rest_framework import serializers
from api_app.models import BedAvailability
from datetime import datetime

class BedSerializer(serializers.ModelSerializer):

	class Meta:
		model = BedAvailability
		fields = ['id', 'alloted_on', 'status', 'patient_name', 'type']

	def __init__(self, *args, **kwargs):
		request = kwargs['context']['request']
		if request.method == 'PUT':
			self.fields.pop('type')
		super(BedSerializer, self).__init__(*args, **kwargs)

	def validate(self, validated_data):
		request = self.context['request']
		if request.method == 'POST' and not BedAvailability.objects.filter(status='FREE', type=validated_data['type']).exists():
			raise serializers.ValidationError("Not available as of now")

		return validated_data

	def create(self, validated_data):
		obj = BedAvailability.objects.filter(type=validated_data['type'], status='FREE').first()
		obj.status = 'NOT FREE'
		obj.patient_name = validated_data['patient_name']
		obj.alloted_on = datetime.now()
		obj.save()
		return obj

	def update(self, instance, validated_data):
		instance.status = 'FREE'
		instance.patient_name = ''
		instance.alloted_on = datetime.now()
		instance.save()
		return instance

