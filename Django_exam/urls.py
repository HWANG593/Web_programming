from django.urls import path
from . import views

urlpatterns = [
    path('exercise1/', views.exercise1, name='exercise1'),
    path('exercise2/',views.exercise2, name='exercise2'),
    path('product1/', views.product1, name='product1'),
    path('basket1/', views.basket1, name='basket1'),

]

# exercise1/으로 끝나면 views.exercise1을 실행한다.
# exercise2/로 끝나면 views.exercise2를 실행한다.