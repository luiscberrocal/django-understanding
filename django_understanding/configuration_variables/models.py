import json

from django.db import models


# Create your models here.

class ConfigurationVariable(models.Model):
    STRING_TYPE = "STRING"
    INTEGER_TYPE = "INTEGER"
    BOOL0EAN_TYPE = "BOOLEAN"
    FLOAT_TYPE = "FLOAT"
    LIST_TYPE = "LIST"
    OBJECT_TYPE = "OBJECT"

    VARIABLE_TYPES = (
        (STRING_TYPE, "String"),
        (INTEGER_TYPE, "Integer"),
        (BOOL0EAN_TYPE, "Boolean"),
        (FLOAT_TYPE, "Float"),
        (LIST_TYPE, "List"),
        (OBJECT_TYPE, "Object"),
    )

    name = models.CharField(max_length=128, unique=True)
    variable_type = models.CharField(max_length=12, choices=VARIABLE_TYPES, default=STRING_TYPE)
    value = models.TextField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_value(self):
        if self.variable_type == self.STRING_TYPE:
            return self.value
        elif self.variable_type == self.INTEGER_TYPE:
            return int(self.value)
        elif self.variable_type == self.BOOL0EAN_TYPE:
            return self.value.lower() in ("yes", "true", "t", "1")
        elif self.variable_type == self.FLOAT_TYPE:
            return float(self.value)
        elif self.variable_type == self.LIST_TYPE:
            return json.loads(self.value)
        elif self.variable_type == self.OBJECT_TYPE:
            return json.loads(self.value)
        else:
            return self.value
