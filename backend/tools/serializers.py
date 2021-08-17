from tools.models import Tool
from rest_framework import serializers

## Model Serializer

class ToolSerializer(serializers.ModelSerializer):
    # Custom Field
    href = serializers.SerializerMethodField()
    # Defining model serializer
    class Meta:
        model = Tool
        fields = "__all__"
        # fields = ['id', 'name', 'image', 'description'] If custom fields are there include those in here also if you use list inter of "__all__"
        # exclude = ['description']
        
    def get_href(self, object):
        name = object.name.replace(" ", "-").lower()
        return name
    
    ## Object level validation
    def validate(self, data):
        if data["name"] == None or data["name"] == "":
            raise serializers.ValidationError("Name of tool should not be empty or null")
        return data
    
    ## Filed level Validation
    def validate_name(self, value):
        if len(value) == 0 or value == None:
            raise serializers.ValidationError("Name is not set or NULL")
        else:
            return value



## BASIC Serializer

# class ToolSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     image = serializers.FileField()
#     description = serializers.CharField()
    
#     def create(self, validated_data):
#         return Tool.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.image = validated_data.get('image', instance.image)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance
    
#     def validate_name(self, value):
#         if len(value) == 0 or value == None:
#             raise serializers.ValidationError("Name is not set or NULL")
#         else:
#             return value