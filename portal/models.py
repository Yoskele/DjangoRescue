from django.db import models




class Event(models.Model):
    CATEGORY = (
        ('fire', 'Fire'),
        ('earth', 'Earth'),
        ('water', 'Water'),
        ('storm', 'Storm'),
        ('disease', 'Disease'),
        ('industrial', 'Industrial')
    )

    SEVERITY = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    )

    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, default=None, blank=True)
    location = models.CharField(max_length=200)
    severity = models.CharField(max_length=10, choices=SEVERITY,
                                default='medium')
    category = models.CharField(max_length=10, choices=CATEGORY,
                                default='fire')

    def __str__(self):
        return "{} [{}] at {}".format(
            self.name, self.severity, self.location)


class PersonStatus(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.id_number, self.mobile

# to do: add Person model---  DONE