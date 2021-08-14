from django.db import models

class Tool(models.Model):
    class Meta:
        verbose_name_plural = "Tool"
        ordering = ('name',)
    name = models.CharField(max_length=100, null=True)
    image = models.FileField(upload_to="images")
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
    