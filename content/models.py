from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



class Device(models.Model):
    device_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="offline")
    last_connected = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Content(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50, choices=[("image", "Image"), ("video", "Video")])
    content = models.FileField(upload_to="content_files/")

    def __str__(self):
        return self.name


class Schedule(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField()

    def __str__(self):
        return f"Schedule for {self.program.name} at {self.scheduled_at}"


class Statistics(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    total_views = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stats for {self.device.name} - {self.program.name}"
