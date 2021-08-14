from rest_framework import serializers

class ToolSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    image = serializers.FileField(read_only=True)
    description = serializers.CharField(read_only=True)