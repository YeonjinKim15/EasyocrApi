from django.shortcuts import render

# Create your views here.
class GradeViewSet(viewsets.ModelViewSet):
	#QuerySet that contains all grade objects in the database.
	queryset = Module.objects.all()
	serializer_class = GradeSerializer