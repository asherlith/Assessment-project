from api.views import companylist,riccodeCompany
from django.urls import path


urlpatterns=[
    path('corps/', companylist),
    path('esgscore/<str:ricCode>/',riccodeCompany)

]