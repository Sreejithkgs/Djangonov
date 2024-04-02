from .models import cart
def total(request):
    # c=request.cart.objects.filter()
    # b=c.quantity.count()
    # return {'count':b}


    count=0
    if request.user.is_authenticated:
       u=request.user
    try:
       c = cart.objects.filter(user=u)
       for i in c:
           count=count+i.quantity

    except:
        count=0
    return {'count':count}

