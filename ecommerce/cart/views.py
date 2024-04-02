
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop. models import product
from .models import cart,account,order
from django.http import HttpResponse

# Create your views here.

@login_required
def cartview(request):
    u=request.user
    c=cart.objects.filter(user=u)
    total=0
    for i in c:
        total=total+i.quantity*i.product.price
    return render(request,'addtocart.html',{'c':c,'total':total})
@login_required
def add_cart(request,p):
    p=product.objects.get(id=p)
    u=request.user
    try:
        Cart_obj=cart.objects.get(user=u,product=p)
        if(p.stock>0):
            Cart_obj.quantity+=1
            Cart_obj.save()
            p.stock-=1
            p.save()

    except:
        if(p.stock>0):
            Cart_obj=cart.objects.create(product=p,user=u,quantity=1)
            Cart_obj.save()
            p.stock-=1
            p.save()
    return cartview(request)

def cart_remove(request,p):
    p=product.objects.get(id=p)
    u=request.user
    try:
        Cart= cart.objects.get(user=u, product=p)
        if (Cart.quantity > 1):
            Cart.quantity -= 1
            Cart.save()
            p.stock += 1
            p.save()

        else:
            Cart.delete()
            p.stock +=1
    except:
        pass
    return cartview(request)


def full_remove(request,p):
    p=product.objects.get(id=p)
    u=request.user
    try:
        Cart=cart.objects.get(user=u,product=p)
        Cart.delete()
        p.stock += Cart.quantity
        p.save()
    except:
        pass
    return cartview(request)
def orderform(request):
    if(request.method=='POST'):
        a=request.POST['a']
        p=request.POST['p']
        ac=request.POST['ac']
        u=request.user
        c=cart.objects.filter(user=u)
        total=0
        for i in c:
            total=total+i.quantity*i.product.price
        try:
            an=account.objects.get(acctnum=ac)
            if(an.amount >= total):
                an.amount=an.amount-total
                an.save()
                for i in c:
                    b=order.objects.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status='paid')
                    b.save()
                c.delete()
                msg="Order Placed Successfully"
                return render(request,'orderdetail.html',{'message':msg})
            else:
                msg="Insufficient amount .You can't place order"
                return render(request,'orderdetail.html',{'message':msg})
        except:
            pass

    return render(request,'orderform.html',)

def Myorder(request):
    u=request.user
    b=order.objects.filter(user=u)
    return render(request,'orderview.html',{'c':b,'u':u.username})

