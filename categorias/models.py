from django.db import models


class Categorie(models.Model):
    category_name = models.CharField(max_length=48)

    def __str__(self) -> str:
        return self.category_name