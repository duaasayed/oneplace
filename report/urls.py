from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('', views.show, name='show'),
    path('report-data', views.report_data, name='report_data'),
    path('add-application', views.add_application, name='add_application'),
    path('applications/<int:pk>/change-status', views.change_status, name='change_status'),
    path('report/export', views.export, name='export')
]