
from django.db import models
from GroupsApp.models import Group
from AuthenticationApp.models import MyUser

class Comment(models.Model):
    time = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=500)
    group = models.ForeignKey(Group, default=None, null=True)
    createdBy = models.ForeignKey(MyUser, default=None, null=True)

    def __str__(self):
        return self.comment