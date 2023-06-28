from django.db import models

class School(models.Model):
    id1 = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    create_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    id2 = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    enrollment = models.CharField(max_length=20, unique=True)
    school = models.ForeignKey(School, default=1, verbose_name="Category", on_delete=models.CASCADE)
    create_at = models.DateField()
    update_at = models.DateField()

    def __str__(self):
        return self
