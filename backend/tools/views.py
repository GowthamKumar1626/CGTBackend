from rest_framework.response import Response
from rest_framework.decorators import api_view

from tools.models import Tool
from tools.serializers import ToolSerializer

@api_view(['GET'])
def tool_list(request):
    tools = Tool.objects.all()
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def tool_details(request, pk):
    tool = Tool.objects.get(pk=pk)
    serializer = ToolSerializer(tool)
    return Response(serializer.data)
    