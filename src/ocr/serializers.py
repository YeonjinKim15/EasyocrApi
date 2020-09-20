from rest_framework import serializers
from .models import Module

class GradeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Module # 모델 설정
		fields = ['module','score','grade'] # 필드 설정