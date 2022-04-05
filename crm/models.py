from django.utils import timezone
from django.conf import settings
from django.db import models


class Customer(models.Model):
    """
    Class Object Customer
    """
    id = models.CharField(primary_key=True, unique=True, max_length=8)
    first_name = models.CharField(max_length=25, verbose_name="First Name")
    last_name = models.CharField(max_length=25, verbose_name="Last Name")
    email = models.EmailField(
        max_length=100, verbose_name="email")
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    mobile = models.CharField(max_length=20, verbose_name="Mobile Number")
    company_name = models.CharField(max_length=250,
                                    verbose_name="Compagny Name")
    date_created = models.DateTimeField(
        verbose_name="Date Created", auto_now_add=True)
    date_updated = models.DateTimeField(
        verbose_name="Date Updated", auto_now_add=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        limit_choices_to={'profile_staff': 2},
        on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Save Method surcharged to update ID Customer CMXXXXX
        """
        last_customer = Customer.objects.all().order_by('id').last()
        if not last_customer:
            self.id = "CM00001"
        else:
            self.id = "CM" + str(int(last_customer.id[2:])+1)
        super().save(*args, **kwargs)


class Contract(models.Model):
    """
    Class Object Contract for Customer
    """
    id = models.CharField(primary_key=True, unique=True, max_length=8)
    title = models.CharField(max_length=125,
                             verbose_name="Title Contract",
                             default="Title Contract")
    date_start_contract = models.DateTimeField(
        verbose_name="Date Start Contract", auto_now_add=True)
    date_end_contract = models.DateTimeField(
        verbose_name="Date End Contract")
    signed = models.BooleanField(verbose_name='signed', default=False)
    customer_assigned = models.ForeignKey(
        to=Customer, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Save Method surcharged to update ID Contract CTXXXXX
        """
        last_contract = Contract.objects.all().order_by('id').last()
        if not last_contract:
            self.id = "CT00001"
        else:
            self.id = "CT" + str(int(last_contract.id[2:])+1)
        super().save(*args, **kwargs)


class Event(models.Model):
    """
    Class Object Event
    """
    id = models.CharField(primary_key=True, unique=True, max_length=8)
    title = models.CharField(max_length=125, verbose_name="Title Event")
    date_started = models.DateTimeField(
        verbose_name="Date Start", auto_now_add=True)
    date_updated = models.DateTimeField(
        verbose_name="Date Updated", auto_now_add=True)
    date_finished = models.DateTimeField(verbose_name="Date End")
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        limit_choices_to={'profile_staff': 3},
        on_delete=models.CASCADE)
    contract_assigned = models.ForeignKey(
        to=Contract, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Save Method surcharged to update ID Event EXXXXX
        """
        last_event = Event.objects.all().order_by('id').last()
        if not last_event:
            self.id = "E00001"
        else:
            self.id = "E" + str(int(last_event.id[1:])+1)
        super().save(*args, **kwargs)


class Need(models.Model):
    """
    Class Object Need For Event
    """
    id = models.CharField(primary_key=True, unique=True, max_length=8)
    title = models.CharField(max_length=125, verbose_name="title Need")
    success = models.BooleanField(verbose_name='success', default=False)
    date_updated = models.DateTimeField(
        verbose_name="Date Updated", auto_now_add=True)
    event_assigned = models.ForeignKey(
        to=Event, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """Save Method surcharged to update ID Need NXXXXX
        """
        last_need = Need.objects.all().order_by('id').last()
        if not last_need:
            self.id = "N00001"
        else:
            self.id = "N" + str(int(last_need.id[1:])+1)
        super().save(*args, **kwargs)
