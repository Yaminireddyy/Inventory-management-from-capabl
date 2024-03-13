#!/usr/bin/env python
# coding: utf-8

# # Inventory Management

# In[1]:


dict1={}
def New_product(id,name,price,quantity):
    dict1[id]={"product_name":name,"product_price":price,"product_quantity":quantity}
def remove(id):
    dict1.pop(id)
def displayall():
    for i in dict1:
        print(i,":",dict1[i])
def display(id):
    print(id,":",dict1[id])
New_product(501,"phones",18000,20)
New_product(502,"laptops",75000,10)
New_product(503,"tv",25000,30)
New_product(504,"radio",10000,15)
New_product(505,"air_conditoner",15000,20)
print("Enter your choice:")
ch=int(input("1.Add product\n2.Remove product\n3.Display all products\n4.Display a product\n"))
if ch==1:
    id_=int(input("Enter product id:"))
    name=input("enter product name:")
    price=int(input("enter product price:"))
    quantity=int(input("enter product quantity:"))
    New_product(id_,name,price,quantity)
elif ch==2:
    id_=int(input("enter product id:"))
    remove(id_)
elif ch==3:
    displayall()
elif ch==4:
    id_=int(input("enter product id:"))
    display(id_)
else:
    print("Invalid choice")
    



# In[ ]:





# In[ ]:




