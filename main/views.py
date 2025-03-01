from django.views.generic import ListView, CreateView, UpdateView
from helpers.views import DeleteView
from main.models import User, Order
from .forms import UserForm, OrderForm
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404


class UserListView(ListView):
    model = User
    template_name = "index.html"
    context_object_name = "users"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 9

    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(course__icontains=search) |
                Q(phone_number__icontains=search) |
                Q(family_phone_number__icontains=search)
            )

        return object_list

class UserCreateView(CreateView):
    model = User
    template_name = "add-student.html"
    form_class = UserForm
    context_object_name = "object"
    success_url = reverse_lazy("main:user-list") 


class UserUdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "edit-student.html"
    context_object_name = "object"
    success_url = reverse_lazy("main:user-list") 

    def get_initial(self):
        # Eski ma'lumotlarni formga yuklash
        initial = super().get_initial()
        initial['first_name'] = self.object.first_name
        initial['last_name'] = self.object.last_name
        initial['payment_date'] = self.object.payment_date
        # Qo'shimcha maydonlarni shu tarzda qo'shishingiz mumkin
        return initial


class UserDeleteView(DeleteView):
    model = User
    success_url = "main:user-list"


# Orders Crud
class UserOrderListView(ListView):
    model = Order
    context_object_name = "orders"
    template_name = "order_list.html"
    paginate_by = 100

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)

        queryset = Order.objects.filter(user=user).order_by("-id")  

        # Qidiruv so'zini olish, bo'sh string sifatida
        search_query = self.request.GET.get('search', '').strip()  # Bo'sh string sifatida olish

        # Qidiruv so'zi bo'lsa, buyurtmalarni filtrlash
        if search_query:  
            queryset = queryset.filter(
                Q(user__first_name__icontains=search_query) |
                Q(amount__icontains=search_query) |
                Q(payment_date__icontains=search_query)
            )

        return queryset
    

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "edit-order.html"
    context_object_name = "user"
    
    def get_success_url(self):
        return reverse('main:user-orders', args=[self.object.user.id])
    
class OrderDeleteView(DeleteView):
    model = Order
    success_url = 'main:user-list'


def update_payment(request, user_id):
    if request.method == "POST":
        try:
            user = User.objects.get(id=user_id)
            user.paid = not user.paid
            if user.paid:
                amount = user.payment_amount
                order = Order.objects.create(user=user, amount=amount)

            user.save()  # Foydalanuvchini saqlash
            return JsonResponse({'success': True, 'new_status': user.paid, 'order_id': order.id if user.paid else None})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User not found.'})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})