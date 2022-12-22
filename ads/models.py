from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.TextChoices):
    TANK = "TA", "Tanks"
    HEAL = "HE", "Heals"
    DD = "DD", "DD"
    GUILDMASTER = "GM", "GuildMaster"
    QUESTGIVER = "QG", "QuestGiver"
    BLACKSMITH = "BS", "Blacksmith"
    SKINNER = "SK", "Skinner"
    POTIONMASTER = "PM", "PotionMaster"
    SPELLMASTER = "SM", "SpellMaster"


class PrUser(models.Model):
    pr_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Ads(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=2, choices=Category.choices, null=False)
    tittle = models.CharField(max_length=40)
    content = RichTextUploadingField()


    def __str__(self):
        return f'{self.tittle}'

    def get_absolute_url(self):
        return f'{self.id}'


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ads, on_delete=models.CASCADE)
    comment = models.TextField(max_length=144)

    def __str__(self):
        return f'{self.comment}'

    def get_absolute_url(self):
        return f'{self.id}'
