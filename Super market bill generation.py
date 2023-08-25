from datetime import datetime
name=input('Enter your name:')
#list of items
lists= '''
Rice    Rs 50/kg
sugar   Rs 30/kg
salt    Rs 20/kg
Oil     Rs 200/liter
Paneer  Rs 150/kg
Boost   Rs 150/kg
Oats    Rs 200/kg
Bananas Rs 50/Kg
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'Rice':50,'sugar':30,'salt':20,'Oil':200,'Paneeer':150,'Boost':150,'Oats':200,'Bananas':50}

option=int(input('for list of items press 1:'))

if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 or press 2 to exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input('enter your item:')
        quantity=int(input('enter quantity:'))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print('sorry item is not available')
    else:
        print('you entered wrong number')
    inp=input('can i bill the items yes or no:')
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=",'Sagar super market',25*"=")
            print(28*" ","Karimnagar")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"_")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*" ",3*" ",ilist[i],8*" ",qlist[i],plist[i])
            print(75*"_")
            print(50*" ","TotalAmount:","Rs",totalprice)
            print("gst amount",53*" ",'Rs',gst)
            print(75*"_")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"_")
            print(25*" ",'Thanks for visiting')
            print(75*"_")
