from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDoModel
from django.shortcuts import get_object_or_404
from datetime import datetime


# Create your views here.

class ListTaskView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = ToDoModel.objects.all()
        result = []
        for todo in queryset:
            result.append({'id': todo.pk,
                           'task_text': todo.task,
                           'status': todo.status,
                           'created_at': todo.created_at,
                           'updated_at': todo.updated_at, })
        return Response(result)


class DetailTaskView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = get_object_or_404(ToDoModel, pk=kwargs['id'])
        return Response({'id': queryset.pk,
                         'task_text': queryset.task,
                         'status': queryset.status,
                         'created_at': queryset.created_at,
                         'updated_at': queryset.updated_at, })


class CreateTaskView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            task = request.data['task_text']
        except KeyError:
            return Response({'message': 'Please send task_text'}, 400)
        q = ToDoModel()
        q.task = task
        q.save()

        return Response({'message': 'Object created successfully'})


class DeleteTaskView(APIView):
    def delete(self, request, *args, **kwargs):
        id = kwargs['id']
        q = get_object_or_404(ToDoModel, pk=id)
        q.delete()
        return Response({'message': "deleted"}, 204)


class UpdatePatchTaskView(APIView):
    def patch(self, request, *args, **kwargs):
        task1 = get_object_or_404(ToDoModel, pk=kwargs['id'])
        if 'task_text' in request.data:
            task1.task = request.data['task_text']
            task1.save()
        if 'created_at' in request.data:
            task1.created_at = request.data['created_at']
            task1.save()
        return Response({'message': 'success'})


class UpdatePutTaskView(APIView):
    def put(self, request, **kwargs):
        task = get_object_or_404(ToDoModel, pk=kwargs['id'])
        try:
            task.task = request.data('task_text')
            task.created_at = request.data('created_at')
            task.save()
            return Response({'message': 'success'})
        except:
            return Response({'message': 'fail,Please provide task_text and created_at'})


class StatusUpdateView(APIView):
    def get(self, request, *args, **kwargs):
        task1 = get_object_or_404(ToDoModel, pk=kwargs['id'])