import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MenuMaster.settings')
from django.db.utils import IntegrityError
from django.db import models

import django
django.setup()

from MenuSelection.models import MenuMaster,ReceipeMaster

import xlrd
workbook  =  xlrd.open_workbook("data.xlsx")

worksheet = workbook.sheet_by_name("Receipe Master")
for i in range(54,115):
    try:
        object = MenuMaster.objects.get(item_name = worksheet.cell(i,0).value)
        book   = ReceipeMaster.objects.get_or_create(menu_item = object,
                                                    base_quantity = worksheet.cell(i,1).value,base_uom = worksheet.cell(i,2).value,
                                                    item = worksheet.cell(i,3).value,type = worksheet.cell(i,4).value,brand = worksheet.cell(i,5).value,
                                                    measure = worksheet.cell(i,6).value,unit_of_measure = worksheet.cell(i,7).value,
                                                    factor = worksheet.cell(i,8).value)
    except IntegrityError:
        continue
    except MenuMaster.DoesNotExist:
        continue
    except ReceipeMaster.DoesNotExist:
        continue

    # try:
    #     book = MenuMaster.objects.get_or_create(item_name = item,type='SPECIAL ITEMS')
    # except IntegrityError:
    #     continue
