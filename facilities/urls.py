from django.urls import path
from . import views 


urlpatterns = [
    path('facilities/', views.FacilityListView.as_view(), name='facility-list'),
    path('facilities/<int:pk>', views.FacilityDetailView.as_view(), name='facility-detail'),
    path('consumption/', views.ConsumptionListView.as_view(), name='consumption-list'), 
    path('coefficients/', views.CoefficientRecordView.as_view(), name='coefficients-list')
]