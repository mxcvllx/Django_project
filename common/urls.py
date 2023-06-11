from django.urls import path

from common.views import CategoryListCreateView, AboutUsListApiViews, AdvantagesListAPIView

urlpatterns = [
    path('category/', CategoryListCreateView.as_view(), name='category'),
    path('about-us/', AboutUsListApiViews.as_view(), name='about-us'),
    path('advantages/', AdvantagesListAPIView.as_view(), name='advantages')
]
