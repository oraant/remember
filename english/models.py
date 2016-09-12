from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    words = models.IntegerField()

    def __unicode__(self):
        return self.name

class Group(models.Model):
    book = models.ForeignKey(Book)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    words = models.IntegerField()

    def __unicode__(self):
        return self.name

class Word(models.Model):
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name

class User(models.Model):
    # todo : use django auth
    pass

class Record(models.Model):
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    wrong = models.IntegerField()
    date = models.DateField()

class Today(models.Model):

    STATUS = (
        ('passed', 'PASSED'),
        ('failed', 'FAILED'),
        ('hanging', 'HANGING'),
        ('waiting', 'WAITING'),
    )

    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    wrong = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS)


