from django.db import models

class category(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    image=models.ImageField(upload_to='media/images',null=True,blank=True)

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='media/images', null=True, blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


