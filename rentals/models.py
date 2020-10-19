from django.db import models


class Facility(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Estate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pax = models.IntegerField()
    amount = models.FloatField()
    commission = models.FloatField(default='0.08', editable=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True)
    # image = models.ImageField()

    def __str__(self):
        return self.title


class Reservation(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    since_date = models.DateField()
    to_date = models.DateField()
    code = models.CharField(max_length=100, editable=False)
    amount = models.FloatField(editable=False)
    guest_name = models.CharField(max_length=200, blank=True, null=False, editable=False)
    guest_last_name = models.CharField(max_length=200, blank=True, editable=False)
    guest_email = models.EmailField(blank=True, editable=False)

    def __str__(self):
        return "Reservation: " + self.estate.__str__()


class RentalDate(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.estate.__str__() + " " + self.date.__str__()
