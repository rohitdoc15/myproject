from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField( auto_now_add=True)
    tags = models.ManyToManyField('tag')
    

    def __str__(self):
        return self.name
    
class Channel(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created = models.DateField( auto_now_add=True)
    #assign all titles to channel of specific channel



    def __str__(self):
        return self.name
    
class Title(models.Model):
    channel = models.ForeignKey('channel', on_delete=models.CASCADE ,null=True, blank=True, related_name='titles')
    name = models.CharField(max_length=100,null=False,blank=False,unique=False)
    date = models.DateField( auto_now_add=True)
    tags = models.ManyToManyField('tag',default='others')
    id = models.AutoField(primary_key=True)
    v_id = models.CharField(max_length=100,null=False,blank=False,unique=True)
    tit = models.CharField(max_length=100,null=False,blank=False,unique=False)
    # color = models.CharField(max_length=100,null=True,blank=True)

    
    

    def __str__(self):
        return self.tit    
    
class tag(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name    
    

class dummy(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name        