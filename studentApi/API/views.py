from rest_framework import generics
from API.models import *
from serializers import *

class CreateStudentView(generics.CreateAPIView):
    serializer_class = StudentMainSerializer
    
class ListAllStudentsView(generics.ListAPIView):
    queryset = StudentMainModel.objects.all()
    serializer_class = StudentMainSerializer
    
class AddMarksToStudentView(generics.CreateAPIView):
    serializer_class = StudentMarksSerializer
    
    def perform_create(self, serializer):
        student_id = self.request.data['student']
        sem = self.request.data['sem']
        marks = self.request.data['marks']
        student_marks_main = studentMarksMainModel.objects.get(student_id=student_id)
        if student_marks_main.marks.filter(sem=sem).exists():
            raise serializers.ValidationError("Marks for this semester already assigned.")
        else:
            student_marks = serializer.save()
            student_marks_main.marks.add(student_marks)
            
class ListStudentMarksHistoryView(generics.ListAPIView):
    serializer_class = StudentMarksSerializer
    
    def get_queryset(self):
        student_id = self.kwargs('pk')
        student_marks_main = studentMarksMainModel.objects.get(student_id=student_id)
        return student_marks_main.marks.all()

