from rest_framework.routers import DefaultRouter

from employees.api.views.employee import EmployeeView
app_name = 'employees'

router = DefaultRouter()

router.register(r'employee', EmployeeView, basename='employ_view')

urlpatterns = router.urls
