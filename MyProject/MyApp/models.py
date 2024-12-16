from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class IntermediateModel(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True


class FinalModel(IntermediateModel):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
