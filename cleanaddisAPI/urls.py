from django.urls import include, path

from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet, GCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('devices', FCMDeviceAuthorizedViewSet)
urlpatterns = [
    
    path('api/users/', user_signup_view),
    path('api/users/web/', user_web_signup),
    path('api/users/all', all_user_view),
    path('api/user/<int:id>',UserDetail.as_view()),
    path('api/user/<int:pk>/update/password/', user_password_update),
    path('api/user/<int:pk>/update/', user_profile_update),
    path('api/user/delete/<int:pk>' , user_delete_view),
    path('api/companies/',CompanyAPIView.as_view()),
    path('api/waste/<int:pk>', waste_detail_view),
    path('api/waste/<int:pk>/update', waste_update_view),
    path('api/waste/delete/<int:pk>', waste_delete_view),
    path('api/waste/seller/<int:seller>', seller_list_view),
    path('api/waste/seller/<int:seller>/<str:for_waste>/<str:waste_type>', seller_list_view_by_type),
    path('api/waste/buyer/<int:buyer>', buyer_list_view),
    path('api/waste/donations', waste_donation_list),
    path('api/waste/', waste_create_view),
    path('api/waste/all/', all_waste_list_view),
    path('api/waste/<str:waste_type>/',waste_list_for_sell),
    path('api/report/', report_create_view),
    path('api/report/all/', all_report_list_view),
    path('api/report/<int:pk>', report_detail_view),
    path('api/report/<int:pk>/update', report_update_view),
    path('api/report/delete/<int:pk>', report_delete_view),
    path('api/report/reportlist/<int:reportedBy>',report_list_view),
    path('api/publicplace/', publicplace_create_view),
    path('api/publicplace/list/', publicplace_list_view),
    path('api/publicplace/all', all_publicplace_view),
    path('api/publicplace/<int:pk>', publicplace_detail_view),
    path('api/publicplace/<int:pk>/update', publicplace_update_view),
    path('api/publicplace/delete/<int:pk>', publicplace_delete_view),
    path('api/seminar/', seminar_create_view),
    path('api/seminar/all', seminar_list_view),
    path('api/seminar/<int:pk>', seminar_detail_view),
    path('api/seminar/<int:pk>/update', seminar_update_view),
    path('api/seminar/delete/<int:pk>', seminar_delete_view),
    path('api/workschedule/', workschedule_create_view),
    path('api/workschedule/all', all_workschedule_view),
    path('api/workschedule/<int:pk>', workschedule_detail_view),
    path('api/workschedule/<int:pk>/update', workschedule_update_view),
    path('api/workschedule/delete/<int:pk>', workschedule_delete_view),
    path('api/announcement/', announcement_create_view),
    path('api/announcement/all', all_announcement_view),
     path('api/announcement/individual/', announcement_view),
    path('api/announcement/<int:pk>', announcement_detail_view),
    path('api/announcement/<int:pk>/update', announcement_update_view),
    path('api/announcement/delete/<int:pk>', announcement_delete_view),
    path('api/auth/', custom_token_obtain),
    path('api/auth/refresh', jwt_views.token_refresh), 
    path('register_device',
         FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'), 
   
    path('device/register/',
         GCMDeviceAuthorizedViewSet.as_view({'post': 'create'}),)
]
