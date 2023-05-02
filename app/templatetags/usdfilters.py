from django import template

register=template.Library()

@register.filter(name='swapping')
def Swap(value):
    return value.swapcase()

#register.filter('swapping',Swap)

@register.filter()
def remove(value,arg):
    return value.replace(arg,'')
#register.filter('remove',remove)


@register.filter()
def count(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:
            c+=1
    return value.count(arg)
#register.filter('count',count)