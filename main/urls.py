from django.urls import path

from main import views
app_name = 'main'

urlpatterns = [
        path("", views.UserListView.as_view(), name="user-list"),
        path("create/", views.UserCreateView.as_view(), name="user-create"),
        path("<int:pk>/", views.UserUdateView.as_view(), name="user-update"),
        path("delete/<int:pk>/", views.UserDeleteView.as_view(), name="user-delete"),
        path('update-payment/<int:user_id>/', views.update_payment, name='update_payment'),

        path('user/<int:user_id>/orders/', views.UserOrderListView.as_view(), name='user-orders'),
        path('orders/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),
        path('orders/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order-delete'),
        ]
