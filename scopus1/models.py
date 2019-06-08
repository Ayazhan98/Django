from django.db import models


class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    scopus_author_id = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name


class P_type(models.Model):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name


class Paper(models.Model):
    title = models.TextField(max_length=150, unique=True)
    p_type = models.ForeignKey(P_type,models.SET_NULL,blank=True,null=True,)
    description = models.TextField(blank=True , unique=True)
    num_pages = models.IntegerField(null=True)
    co_authors  = models.TextField(max_length=150,default=None)
    author_id = models.ForeignKey(Staff, models.SET_NULL,blank=True,null=True,)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.title


