from django.db import models

# Create your models here.

class MenuMaster(models.Model):
    TYPE_CHOICES  =  (('BREAKFAST','BREAKFAST'),('LUNCH','LUNCH'),
                       ('EVENING SNACKS & DINNER','EVENING SNACKS & DINNER'),('SPECIAL ITEMS','SPECIAL ITEMS'))

    item_name   =   models.CharField(max_length = 100,primary_key = True)
    image       =   models.ImageField(blank = True,upload_to = "item")
    type        =   models.CharField(max_length = 30,choices = TYPE_CHOICES)


class MenuSelection(models.Model):
    DAY_CHOICES   =   (('MONDAY','MONDAY'),('TUESDAY','TUESDAY'),('WEDNESDAY','WEDNESDAY'),('THURSDAY','THRUSDAY'),
                     ('FRIDAY','FRIDAY'),('SATURDAY','SATURDAY'),('SUNDAY','SUNDAY'))

    # TYPE_CHOICES  =  (('BREAKFAST','BREAKFAST'),('LUNCH','LUNCH'),
    #                    ('EVENING SNACKS & DINNER','EVENING SNACKS & DINNER'),('SPECIAL ITEMS','SPECIAL ITEMS'))

    # QUANTITY_CHOICES = (('Kg','Kg'),('Grams','Grams'),('Litre','Litre'))

    day           =    models.CharField(max_length = 10,choices = DAY_CHOICES)
    item_name     =    models.ForeignKey(MenuMaster,on_delete = models.CASCADE)
    # type          =    models.CharField(max_length = 30,choices = TYPE_CHOICES)
    quantity      =    models.FloatField()
    quantiy_of_measurement = models.CharField(max_length = 10)

class ReceipeMaster(models.Model):

    # QUANTITY_CHOICES =    (('Kg','Kg'),('Grams','Grams'),('Litre','Litre'))

    menu_item        =    models.ForeignKey(MenuMaster,on_delete = models.CASCADE)
    base_quantity    =    models.FloatField()
    base_uom         =    models.CharField(max_length = 10)
    item             =    models.CharField(max_length = 30)
    type             =    models.CharField(max_length = 30,blank = True)
    brand            =    models.CharField(max_length = 20,blank = True)
    measure          =    models.FloatField()
    unit_of_measure  =    models.CharField(max_length = 10,)
    factor           =    models.FloatField()
