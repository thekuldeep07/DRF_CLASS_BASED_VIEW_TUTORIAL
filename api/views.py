from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):

    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializedStu = StudentSerializer(stu)
            return JsonResponse(serializedStu.data,safe=False)
        stuList = Student.objects.all()
        serializedStu = StudentSerializer(stuList,many=True)
        return JsonResponse(serializedStu.data,safe=False)
    
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        ser = StudentSerializer(data = python_data)
        if(ser.is_valid()):
            ser.save()
            msg = {'msg':'created Successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type= 'application/json')
        json_data = JSONRenderer().render(ser.errors)
        return HttpResponse(json_data,content_type = 'application/json')
    
    def put(self,request,*args,**krwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id =id)
        serializer = StudentSerializer(stu , data = python_data , partial = True)
        if(serializer.is_valid()):
            serializer.save()
            msg={'msg':'updated successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type ='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')
    

    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        msg = {'msg':'deleted succesfully'}
        json_Data = JSONRenderer().render(msg)
        return HttpResponse(json_Data,content_type ="application/info")
    




