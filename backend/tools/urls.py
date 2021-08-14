from django.urls import path

from tools.views import tool_list, tool_details


urlpatterns = [
    path('list/', tool_list, name='tool-list'),
    path('<int:pk>/', tool_details, name='tool-details')
]