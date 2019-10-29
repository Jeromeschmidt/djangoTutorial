from django.db import models

# class Topping(models.Model):
#     # ...
#     topping_text = models.CharField(max_length=200)
#     def __str__(self):
#         return self.size_text
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Pizza(models.Model):
    # ...
    size_text = models.CharField(max_length=200)
    # toppings = models.ManyToManyField(Topping)
    # pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
