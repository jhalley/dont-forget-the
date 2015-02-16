from django.db import models
import datetime

# Create your models here.
class List(models.Model):
    # todo: grocerylist should be attached to a user
    OPEN = 'OPEN'
    CLOSE = 'CLOSE'
    PENDING = 'PENDING'
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length = 100, default='Grocery List %s'%datetime.datetime.now().date())
    status = models.CharField(max_length = 100, default=OPEN)
    
    def __unicode__(self):
        return '%s - %s'%(self.title, self.status)
    
class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #grocery_list = models.ManyToManyField(GroceryList)
    desc = models.CharField(max_length = 100)
    
    # todo: brand should be a separate table
    # todo: comment should be attached to a user or grocery list
    #brand = models.CharField(max_length = 100, default = '')
    #comment = models.TextField(default = '')
    
    def __unicode__(self):
        return self.desc
        
class List_Item(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    list = models.ForeignKey(List)
    item = models.ForeignKey(Item)
    bought = models.BooleanField(default = False)
    
    def __unicode__(self):
        return '%s - %s'%(self.list, self.item)