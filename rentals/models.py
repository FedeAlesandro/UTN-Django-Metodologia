from django.db import models


class Facility(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'

    def __str__(self):
        return self.name


class NameField(models.CharField):  # pasa la variable a lowercase
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class City(models.Model):
    name = NameField(max_length=50)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Estate(models.Model):
    title = models.CharField(max_length=30)
    zone = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    pax = models.IntegerField()
    amount = models.FloatField()
    commission = models.FloatField(default='0.08', editable=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    facility = models.ManyToManyField(Facility)
    image = models.ImageField(upload_to='estate_images')

    def __str__(self):
        return self.title


class Reservation(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    date = models.DateField()
    code = models.CharField(max_length=100, editable=False)
    amount = models.FloatField(editable=False, default=0)
    guest_name = models.CharField(max_length=50, blank=True, null=False, editable=False)
    guest_last_name = models.CharField(max_length=50, blank=True, editable=False)
    guest_email = models.EmailField(blank=True, editable=False)

    def __str__(self):
        return "Reservation: " + self.estate.__str__()


class RentalDate(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.estate.__str__() + " " + self.date.__str__()
