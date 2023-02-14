from empApi.viewsets import EmployeeViewset
from crudapi.viewsets import CrudViewSets
from rest_framework import routers

router= routers.DefaultRouter()
router.register('employee' , EmployeeViewset)
router.register('crud', CrudViewSets)   
