from django.contrib import admin
from api_app import views
from django.urls import path, include
from api_app.views import BedViewAPI


bed_get_detail = BedViewAPI.as_view({
    'get': 'retrieve',
    "put": "update"
})

bed_post_list_detail = BedViewAPI.as_view({
    'post': 'create',
    'get': 'list',
})

urlpatterns = [
				path('bed/', bed_post_list_detail, name='bed_get_detail'),
				path('bed/', bed_post_list_detail, name='bed_post_detail'),
				path('bed/<str:id>/', bed_get_detail, name='bed_get_detail'),
			]