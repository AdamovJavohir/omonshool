#path ni import qilamiz
from django.urls import path

#biz yozgan vievlarni import qilamiz
from .views import HomeView, SuccessView

#viewlarni nom ostida urlga ulaymiz
urlpatterns = [
    path("", HomeView, name="home"),
    path("success/", SuccessView, name="success")
]