from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class MaqomlarTuri(models.Model):
    tur_nomi = models.CharField(max_length=255, verbose_name="Maqom turi")

    class Meta:
        db_table = 'MaqomlarTuri'

    def __str__(self):
        return self.tur_nomi  # Admin panelda tur_nomi ko‘rinadi


class MaqomlarModel(models.Model):
    maqom_nomi = models.CharField(max_length=355, verbose_name="Maqom nomi", null=False)
    ijrochi_surati = models.ImageField(upload_to="media/", verbose_name="Ijrochi surati")
    maqom_sozlari = RichTextField(verbose_name="Maqom so'zlari", null=False)

    maqom_ijrochisi = models.CharField(max_length=355, verbose_name="Maqom ijrochisi", null=False)
    maqom_turi = models.ForeignKey(
        MaqomlarTuri, 
        on_delete=models.CASCADE, 
        related_name="maqomlar", 
        verbose_name="Maqom turi", 
        null=False
    )

    class Meta:
        db_table = 'MaqomlarModel'

    def __str__(self):
        return self.maqom_nomi  # Admin panelda maqom_nomi ko‘rinadi
