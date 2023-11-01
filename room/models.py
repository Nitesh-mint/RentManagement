from django.db import models
from Account.models import Account
from datetime import date, timedelta


room_size_choices = (
    ('small','small'),
    ('medium','medium'),
    ('large', 'large'),
)
class Room(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100)
    size = models.CharField(max_length=50,blank=True, choices=room_size_choices)
    Image = models.ImageField(upload_to="photos/rooms", blank=True)
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.room.name}"
    

def expiry():
    return date.today() + timedelta(days=1)


class IssuedRooms(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        today = date.today()
        if today > self.expiry_date:
            self.is_active = False
        super().save(*args, **kwargs)