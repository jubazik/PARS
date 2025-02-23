from django.db import models

class Document(models.Model):
    number = models.IntegerField()
    station = models.CharField(max_length=255)
    notification = models.IntegerField(unique=True)
    date = models.DateField()
    client_name = models.CharField(max_length=255)
    place_of_transfer = models.CharField(max_length=255)
    locomotive = models.CharField(max_length=255)
    route_belonging = models.CharField(max_length=255)
    client_representative = models.CharField(max_length=255)

    class Meta:
        db_table = 'documents'


class Cargo(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    wagon = models.IntegerField()
    container_and_size = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    control_mark = models.CharField(max_length=255)
    operation = models.CharField(max_length=255)
    cargo_names = models.TextField()
    note = models.TextField()

    class Meta:
        db_table = 'cargo'


# Create your models here.
