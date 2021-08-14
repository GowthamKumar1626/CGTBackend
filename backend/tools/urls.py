from django.urls import path

# from tools.views import tool_list, tool_details
from tools.views import ToolListAPIView, ToolDetailAPIView


## APIView based Routes

urlpatterns = [
    path('list/', ToolListAPIView.as_view(), name='tool-list'),
    path('<int:pk>/', ToolDetailAPIView.as_view(), name='tool-details')
]

## Funtional APIs Routes

# urlpatterns = [
#     path('list/', tool_list, name='tool-list'),
#     path('<int:pk>/', tool_details, name='tool-details')
# ]