from rest_framework import serializers
from task.models import Assigned_person, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class Assigned_personSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only = True)
    
    task_id = serializers.PrimaryKeyRelatedField(
        queryset = Task.objects.all(),
        source = 'task',
        write_only = True
    )

    class Meta:
        model = Assigned_person
        fields = "__all__"