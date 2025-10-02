from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Base(models.Model):
   # unique hash code random
    # this uuid4 base work on time 
    
    uuid=models.UUIDField(unique=True,default=uuid.uuid4)
    
    # carefull if another place up app on sql perhapse does not support
    create_date=models.DateTimeField(auto_now_add=True)
    
    # if field is null can be not save to database
    
    # blank is means user can blank field
    
    modified_date=models.DateTimeField(auto_now=True)
    
    deleted_date=models.DateTimeField(default=None, null=True,blank=True)
    
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    
    # this class do not create on the database 
    # use only abstract another class 
    # conflict beacuse category two realtion on one table
    class Meta:
        abstract=True
    
    
    def __str__(self):
        return f"{self.name}"
    
        
# 1-1-2

# priority first class in the args on the define parent

class Category(Base):
    # static attributes
    name=models.CharField(max_length=225)
    
    # beacuse every table relation 1 to 1 with itself
    parent=models.ForeignKey('Category',null=True
                             ,default=None
                             ,on_delete=models.PROTECT
                             ,related_name='children')
    
    def __str__(self):
        return f"{self.name}"

# 1-1-1

# Camelcase class tell pep and can detect with func
 
class Product(Base): # create table
    
    # static attributes
    name=models.CharField(max_length=225)
    
    slug=models.SlugField()
    price=models.IntegerField()
    discount=models.FloatField(default=0)
    enabled=models.BooleanField()
    deleted=models.BooleanField(default=False)
    description=models.TextField()
    
    # if delete both delete them
    category=models.ForeignKey(Category,on_delete=models.PROTECT
                              ,related_name='products')
    
    # if realted_name is set better 
    # old_category=models.ForeignKey(Category,on_delete=models.PROTECT
    #                               ,related_name='old_product')
    # ---------------------------------------------------------
    
    # in python do not have enum (when we are limit data or resource use enum)
    # we use choices tuple
    # first item save to database, seconde show to user
    #STATUS_ENABLED=0
    #STATUS_DISABLED=1
    #STATUS_DELETED=2
    
    #STATUS_CHOISES=(
    #(STATUS_ENABLED,"Enabled"),
    # (STATUS_DISABLED,'Disabled'),
    #  (STATUS_DELETED,'Deleted')
    #   )
    
    #status=models.IntegerField(max_length=10,choices=STATUS_CHOISES)
    
    def __str__(self):
        return f"{self.name}"
    
class Tag(Base):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"
    
class Comment(Base):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"
    
class Like(Base):
    ...
