from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('hello-viewset',views.helloviewset,base_name='hello-viewset')
router.register('profile',views.userprofileviewset)
router.register('login',views.loginviewset,base_name='login')
router.register('feed',views.userprofilefeedviewset)

urlpatterns=[
    url(r'^hello-view/',views.helloapiview.as_view()),
    url(r'',include(router.urls)),
]