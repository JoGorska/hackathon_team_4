from django.db import models
from django.core.exceptions import ValidationError


# def validate_current_century(value):
#     if value < 2000 or value > 2100:
#         raise ValidationError(u'%s is not a valid year!' % value)

# class Completion(models.Model):
#     start_date = models.DateField(validators=[validate_current_century])
#     end_date = models.DateField(validators=[validate_current_century])

# class ReportPeriod(models.Model):
#     start_date = models.DateField()
#     end_date = models.DateField()

# class ReportPeriod(models.Model):
#     start_date = models.DateField()
#     end_date = models.DateField(default=datetime.date.today())
    
#     date = models.DateField(default=datetime.date.today())
#     duration = models.TextField(default='0', blank='true')
#     created_at = models.DateTimeField(default=datetime.datetime.now(), blank='true')
#     def save(self, *args, **kwargs):
#         if self.date < datetime.date.today():
#             raise ValidationError("The date cannot be in the past!")
#         super(Event, self).save(*args, **kwargs)