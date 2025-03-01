from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):  
    COURSE_CHOICES = [
        ('Frontend', 'Fronted'),
        ('Backend', 'Backend'),
        ('FullStack', 'FullStack'),
        ('Kompyuter Savodxonligi', 'Kompyuter Savodxonligi'),
    ]

    first_name = models.CharField(_("Ismi"), max_length=30)  
    last_name = models.CharField(_("Familyasi"), max_length=30)   
    father_name = models.CharField(_("Otasini Ismi"), max_length=30)
    phone_number = models.CharField(_("Telefon Nomeri"), max_length=100) 
    family_phone_number = models.CharField(_("Oilasini Nomeri"), max_length=100)
    date_joined = models.DateField(_("Qo'shilgan Sanasi"),auto_now_add=True)
    payment_date = models.DateField(_("To'lov Kuni"))
    birth = models.DateField(_("Tug'ilgan yili"))
    paid = models.BooleanField(_("To'landi Yoki To'lanmadi"), default=False) 
    payment_amount = models.DecimalField(_("To'lov Narxi"),max_digits=10, decimal_places=0)
    course = models.CharField(_("O'quv Kursi"), max_length=100, choices=COURSE_CHOICES)

    class Meta:
        db_table = "User"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.first_name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(_("To'lov Narxi"), max_digits=10, decimal_places=0)
    payment_date = models.DateField(_("To'lov Kuni"), auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.amount} so'm"

