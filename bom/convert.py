from .models import PartClass


def full_part_number_to_broken_part(part_number):
    part_class = PartClass.objects.filter(code=part_number[:3])[0]
    part_item = part_number[4:8]
    part_variation = part_number[9:]

    civ = {
        'class': part_class,
        'item': part_item,
        'variation': part_variation
    }

    return civ

def full_part_number_to_broken_cmpart(part_number):
    mainpart_number, revision = part_number.split("_") 
    mainPart, item = mainpart_number.split("-")

    part_class = PartClass.objects.filter(code=mainPart[:-1])[0]
    part_variation = int(mainPart[-1])
    part_item = int(item)


    civ = {
        'class': part_class,
        'item': part_item,
        'variation': part_variation,
        'revision': revision
    }

    return civ
