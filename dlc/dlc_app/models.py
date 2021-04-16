from django.db import models


class Sort(models.Model):
    category = models.SmallIntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.category}"


class Recept(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to="news_image", null=True)
    image3 = models.ImageField(upload_to="news_image", null=True)
    image2 = models.ImageField(upload_to="news_image", null=True)
    steps = models.JSONField(null=False, default={"steps": []})
    ings = models.JSONField(null=False, default={})
    Prep = models.SmallIntegerField(null=False, blank=False, default=2362)
    Cook = models.SmallIntegerField(null=False, blank=False, default=23)
    Yields = models.CharField(max_length=100, null=False, blank=False, default="hhjgjh")
    stars = models.SmallIntegerField(
        choices=[(1, "bir yulduz"), (2, "ikki yulduz"), (3, "uch yulduz"), (4, "tort yulduz"), (5, "besh yulduz")], default=3)
    category = models.SmallIntegerField(null=False, blank=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    recept = models.ForeignKey(Recept, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False, default='kkuh')
    email = models.EmailField(null=False, blank=False, default='sayfififid@gmail.com')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
