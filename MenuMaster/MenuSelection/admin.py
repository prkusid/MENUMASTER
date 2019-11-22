from django.contrib import admin
from MenuSelection.models import MenuMaster,MenuSelection,ReceipeMaster

# Register your models here.

class MenuMasterAdmin(admin.ModelAdmin):
    list_display    =   ['item_name','image','type']
    search_fields   =   ('item_name','type')

class MenuSelectionAdmin(admin.ModelAdmin):
    list_display    =   ['item_name','day','quantity','quantiy_of_measurement']
    # search_fields   =   ('item_name',)
    raw_id_fields   =   ('item_name',)

class ReceipeMasterAdmin(admin.ModelAdmin):
    list_display    =  ['menu_item','base_quantity','base_uom','item','type','brand','measure','unit_of_measure','factor']
    # search_fields   =   ('menu_item',)
    raw_id_fields   =   ('menu_item',)

admin.site.register(MenuMaster,MenuMasterAdmin)
admin.site.register(MenuSelection,MenuSelectionAdmin)
admin.site.register(ReceipeMaster,ReceipeMasterAdmin)
