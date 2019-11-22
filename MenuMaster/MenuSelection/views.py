from django.shortcuts import render
from MenuSelection.models import MenuSelection,ReceipeMaster,MenuMaster

# Create your views here.
def home(request):
    menu_item  = MenuMaster.objects.all()
    breakfast_list = []
    lunch_list = []
    snacks_dinner_list = []
    special_item_list = []
    for i in menu_item:
        if i.type == 'BREAKFAST':
            breakfast_list.append(i)
        elif i.type == 'LUNCH':
            lunch_list.append(i)
        elif i.type == 'EVENING SNACKS & DINNER':
            snacks_dinner_list.append(i)
        else:
            special_item_list.append(i)

    return render(request,'MenuSelection/base.html',{'breakfast_list':breakfast_list,'lunch_list':lunch_list,
                                                    'snacks_dinner_list':snacks_dinner_list,'special_item_list':special_item_list})

def measurement_items(request,menu_item):
    menu_item1  = MenuSelection.objects.get(item_name = menu_item)
    menu_item2  = ReceipeMaster.objects.filter(menu_item__exact = menu_item)

    menu_item   = menu_item1.item_name.item_name
    quantity    = menu_item1.quantity
    string = ''
    # uom         = menu_item1.quantiy_of_measurement
    for item in menu_item2:
        item.measure  = item.factor * quantity
        if item.measure < 0.89:
            if item.unit_of_measure.lower() == 'grams':
                item.measure = item.measure * 1000
        string = str(item.measure)
        find = string.find('.')
        string = string[:find + 3]
        item.measure = float(string)


    return render(request,'MenuSelection/measurement_items.html',{'menu_item':menu_item,'menu_item1':menu_item1,'menu_item2':menu_item2})
