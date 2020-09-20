from django.db import models
from .ocr_result import result as ocr_result

# Create your models here.
class Module(models.Model):
	result = ocr_result() #ocr 결과 전체
	module = result[0] # 과목
	score = result[1] # 점수
	grade = result[2] # 등급
