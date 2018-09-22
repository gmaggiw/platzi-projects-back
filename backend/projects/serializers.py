from rest_framework import serializers

from projects.models import Project, Stack

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = (
            'pk',
            'name',
            'description',
            'logo',
            'members',
            'github',
            'stacks',
            'stars',
            'created_at',
            'updated_at',
            )


class StackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stack
        fields = (
            'pk',
            'name',
            'description',
            'created_at',
            'updated_at',
            )