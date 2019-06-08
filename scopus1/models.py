from django.db import models


class Authors(models.Model):
    f_name = models.CharField(max_length=50, default='N/A')
    m_name = models.CharField(max_length=50, default='N/A')
    l_name = models.CharField(max_length=50, default='N/A')
    scopus_author_id = models.IntegerField(default=0)
    staff_member = models.BooleanField(default=False)

    def __str__(self):
        return self.f_name+" "+self.l_name


class P_type(models.Model):
    type_name = models.CharField(max_length=30, default='N/A')

    def __str__(self):
        return self.type_name


class Paper(models.Model):
    title = models.TextField(max_length=150, blank=False)
    p_type = models.ForeignKey(P_type, models.CASCADE, blank=False)
    description = models.TextField(null=True)
    num_pages = models.IntegerField(null=True)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Authored(models.Model):
    p_title = models.ForeignKey(Paper, on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, blank=False)