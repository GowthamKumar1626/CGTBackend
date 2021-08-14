from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from tools.models import Tool
from tools.serializers import ToolSerializer

## Class based Views - APIView

class ToolListAPIView(APIView):
    
    def get(self, request):
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ToolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class ToolDetailAPIView(APIView):
    
    def get(self, request, pk):
        try:
            tool = Tool.objects.get(pk=pk)
            serializer = ToolSerializer(tool)
            return Response(serializer.data)
        except Tool.DoesNotExist:
            return Response({"details": "Tool doesnot exit"}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
        try:
            tool = Tool.objects.get(pk=pk)
            serializer = ToolSerializer(tool, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Tool.DoesNotExist:
            return Response({"details": "Tool doesnot exit"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk):
        try:
            tool = Tool.objects.get(pk=pk)
            tool.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tool.DoesNotExist:
            return Response({"details": "Tool doesnot exit"}, status=status.HTTP_404_NOT_FOUND)


## Functional APIs

# @api_view(['GET', 'POST'])
# def tool_list(request):
#     if request.method == 'GET':
#         tools = Tool.objects.all()
#         serializer = ToolSerializer(tools, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ToolSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def tool_details(request, pk):
#     if request.method == 'GET':
#         try:
#             tool = Tool.objects.get(pk=pk)
#             serializer = ToolSerializer(tool)
#             return Response(serializer.data)
#         except Tool.DoesNotExist:
#             return Response({"details": "Tool doesnot exit"}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#         tool = Tool.objects.get(pk=pk)
#         serializer = ToolSerializer(tool, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         tool = Tool.objects.get(pk=pk)
#         tool.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)