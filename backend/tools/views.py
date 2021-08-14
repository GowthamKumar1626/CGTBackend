from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from tools.models import Tool
from tools.serializers import ToolSerializer

@api_view(['GET', 'POST'])
def tool_list(request):
    if request.method == 'GET':
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ToolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET', 'PUT', 'DELETE'])
def tool_details(request, pk):
    if request.method == 'GET':
        tool = Tool.objects.get(pk=pk)
        serializer = ToolSerializer(tool)
        return Response(serializer.data)
    if request.method == 'PUT':
        tool = Tool.objects.get(pk=pk)
        serializer = ToolSerializer(tool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        tool = Tool.objects.get(pk=pk)
        tool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)