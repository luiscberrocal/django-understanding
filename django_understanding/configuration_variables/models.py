from django.db import models


# Create your models here.

class ConfigurationVariable(models.Model):
    STRING_TYPE = "STRING"
    INTEGER_TYPE = "INTEGER"
    BOOL0EAN_TYPE = "BOOLEAN"
    FLOAT_TYPE = "FLOAT"
    LIST_TYPE = "LIST"
    OBJECT_TYPE = "OBJECT"

    name = models.CharField(max_length=128, unique=True)
    value = models.TextField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
