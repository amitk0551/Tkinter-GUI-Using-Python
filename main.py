from tkinter import *
from tkinter import ttk, messagebox
import database

win = Tk()
win.geometry("1000x700")

def showSale():
    newwin = Toplevel(win)
    def addsale():
        def addProdu(): 
         a = e6.get()
         b = variable.get()
         c = e2.get()
         d = e3.get()
         reslt = database.insert_data_sale(a,b,c,d)
         if reslt:
            messagebox.showinfo("Information","Record Inserted")


        newwi = Toplevel(newwin)
        options = ["Select Product Id"]
        variable = StringVar(newwi)
        variable.set(options[0]) 
        res = database.show_data()
        
        for data in res:
            prod_id = data[0]
            options.append(prod_id)
        l6 = Label(newwi, text="Sale Id")
        l6.grid( row = 1, column = 2,  sticky = W)
        e6 = Entry(newwi)
        e6.grid(row = 1, column = 3)
        l1 = Label(newwi, text="Product Id")
        l1.grid( row = 2, column = 2,  sticky = W)
        e1 = OptionMenu(newwi, variable, *options)
        e1.grid(row = 2, column = 3, sticky = W)

        l2 = Label(newwi, text="Qty Sold")
        l2.grid( row = 3, column = 2,  sticky = W)
        e2 = Entry(newwi)
        e2.grid(row = 3, column = 3)
        l3 = Label(newwi, text="Sale  Per Unit Price")
        l3.grid( row = 4, column = 2,  sticky = W)
        e3 = Entry(newwi)
        e3.grid(row = 4, column = 3)
        btn_add_p = Button(newwi, text = "Add", command = addProdu)
        btn_add_p.grid(row = 6, column = 4, sticky = W, padx = 3, pady = 3)


    def deleteSale():
         id = d.get()
         result = database.delete_sale(id)
         if result == "error":
            messagebox.showerror("Error", "Error message")
         else:
            messagebox.showinfo("Information","Record Deleted")
       
    
    def updateSale():
        def updat():
            i = id
            a = e2.get()
            b = e3.get()
            c = e4.get()
            result = database.update_sale(i, a, b, c)
            if res:
               messagebox.showinfo("Information","Record Updated")
            else:
                messagebox.showinfo("Information","Record Updated")
        id = u.get()
        newwin = Toplevel(win)
        
        data = database.show_data_sale_id(id)
        for res in data:
            l1 = Label(newwin, text="Sale Id")
            l1.grid( row = 2, column = 2,  sticky = W)
            e1 = Entry(newwin)
            e1.insert(0,res[0])
            e1.grid(row = 2, column = 3)
            l2 = Label(newwin, text="product Id")
            l2.grid( row = 3, column = 2,  sticky = W)
            e2 = Entry(newwin)
            e2.insert(0,res[2])
            e2.grid(row = 3, column = 3)
            l3 = Label(newwin, text="Qty Sold")
            l3.grid( row = 4, column = 2,  sticky = W)
            e3 = Entry(newwin)
            e3.insert(0,res[3])
            e3.grid(row = 4, column = 3)
            l4 = Label(newwin, text="Per unit Price")
            l4.grid( row = 5, column = 2,  sticky = W)
            e4 = Entry(newwin)
            e4.insert(0,res[4])
            e4.grid(row = 5, column = 3)
        btn_update =  Button(newwin, text= "Update", command = updat)
        btn_update.grid(row = 53, column = 3, sticky = W, padx = 2, pady = 2)
        




    heading =  Label(newwin, text="Product List", justify=CENTER )
    l1 = Label(newwin, text="Sale Id")
    l2 = Label(newwin, text="Sale Date")
    l3 = Label(newwin, text="Product Id")
    l4 = Label(newwin, text="Qty Sold")
    l5 = Label(newwin, text="Sale price per unit")

    heading.grid(row=1, column = 4, sticky = W, padx = 20, pady = 20)
    l1.grid(row=4, column = 1, sticky = W , pady = 2, padx =2)
    l2.grid(row=4, column = 2, sticky = W , pady = 2, padx =2)
    l3.grid(row=4, column = 3, sticky = W , pady = 2, padx =2)
    l4.grid(row=4, column = 4, sticky = W , pady = 2, padx =2)
    l5.grid(row=4, column = 5, sticky = W , pady = 2, padx =2)

    result = database.show_data_sale()
    rows = 5 
    for data in result:
        pro = Label(newwin, text = data[0])
        pro.grid(row = rows, column = 1, sticky = W, pady = 2, padx =2)
        name = Label(newwin, text = data[1])
        name.grid(row = rows, column = 2, sticky = W, pady = 2, padx =2)
        qty = Label(newwin, text = data[2])
        qty.grid(row = rows, column = 3, sticky = W, pady = 2, padx =2)
        unit = Label(newwin, text = data[3])
        unit.grid(row = rows, column = 4, sticky = W, pady = 2, padx =2)
        reoder = Label(newwin, text = data[4])
        reoder.grid(row = rows, column = 5, sticky = W)
        rows += 1
    btn_add = Button(newwin, text = "Add Sale", command = addsale)
    btn_add.grid(row = 1, column = 6, sticky = W, padx = 3, pady = 3)

    delete = Label(newwin, text="Delete Record")
    delete.grid( row = 50, column = 2,  sticky = W)
    d = Entry(newwin)
    d.grid(row = 50, column = 3,  sticky = W)
    btn_del =  Button(newwin, text= "Delete", command = deleteSale)
    btn_del.grid(row = 51, column = 3, sticky = W, padx = 2, pady = 2)



    update = Label(newwin, text="Update Record")
    update.grid( row = 52, column = 2,  sticky = W)
    u = Entry(newwin)
    u.grid(row = 52, column = 3,  sticky = W)
    btn_update =  Button(newwin, text= "Update", command = updateSale)
    btn_update.grid(row = 53, column = 3, sticky = W, padx = 2, pady = 2)







def addProduct():
     def addProduc():
         a = e6.get()
         b = e1.get()
         c = e2.get()
         d = e3.get()
         e = e4.get()
         res = database.insert_data(a,b,c,d,e)
         if res:
            messagebox.showinfo("Information","Record Inserted")
     newwin = Toplevel(win)
     l6 = Label(newwin, text="Product Id")
     l6.grid( row = 1, column = 2,  sticky = W)
     e6 = Entry(newwin)
     e6.grid(row = 1, column = 3)
     l1 = Label(newwin, text="Product Name")
     l1.grid( row = 2, column = 2,  sticky = W)
     e1 = Entry(newwin)
     e1.grid(row = 2, column = 3)
     l2 = Label(newwin, text="Qty on hand")
     l2.grid( row = 3, column = 2,  sticky = W)
     e2 = Entry(newwin)
     e2.grid(row = 3, column = 3)
     l3 = Label(newwin, text="Product Unit Price")
     l3.grid( row = 4, column = 2,  sticky = W)
     e3 = Entry(newwin)
     e3.grid(row = 4, column = 3)
     l4 = Label(newwin, text="Re-oder")
     l4.grid( row = 5, column = 2,  sticky = W)
     e4 = Entry(newwin)
     e4.grid(row = 5, column = 3)
     btn_add_p = Button(newwin, text = "Add", command = addProduc)
     btn_add_p.grid(row = 6, column = 4, sticky = W, padx = 3, pady = 3)

def deleteRecod():
    id = E1.get()
    result = database.delete_stock(id)
    if result == "error":
       messagebox.showerror("Error", "Error message")
    else:
        messagebox.showinfo("Information","Record Deleted")

def updateRecod():
    def update():
        a = e1.get()
        b = e2.get()
        c = e3.get()
        d = e4.get()
        res = database.update_stock(id,a,b,c,d)
        if res:
             messagebox.showinfo("Information","Record Updated")
        else:
            messagebox.showinfo("Information","Record Updated")
    id = E2.get()
    newwin = Toplevel(win)
    data = database.show_data_id(id)
    for res in data:
        l1 = Label(newwin, text="Product Name")
        l1.grid( row = 2, column = 2,  sticky = W)
        e1 = Entry(newwin)
        e1.insert(0,res[1])
        e1.grid(row = 2, column = 3)
        l2 = Label(newwin, text="Qty on hand")
        l2.grid( row = 3, column = 2,  sticky = W)
        e2 = Entry(newwin)
        e2.insert(0,res[2])
        e2.grid(row = 3, column = 3)
        l3 = Label(newwin, text="Product Unit Price")
        l3.grid( row = 4, column = 2,  sticky = W)
        e3 = Entry(newwin)
        e3.insert(0,res[3])
        e3.grid(row = 4, column = 3)
        l4 = Label(newwin, text="Re-oder")
        l4.grid( row = 5, column = 2,  sticky = W)
        e4 = Entry(newwin)
        e4.insert(0,res[4])
        e4.grid(row = 5, column = 3)
    btn_update =  Button(newwin, text= "Update", command = update)
    btn_update.grid(row = 53, column = 3, sticky = W, padx = 2, pady = 2)
    

    


heading =  Label(win, text="Product List", justify=CENTER )
l1 = Label(win, text="Product ID")
l2 = Label(win, text="Product Name")
l3 = Label(win, text="Qty on hand")
l4 = Label(win, text="Product Unit Price")
l5 = Label(win, text="Re-oder")


heading.grid(row=1, column = 4, sticky = W, padx = 20, pady = 20)
l1.grid(row=4, column = 1, sticky = W , pady = 2, padx =2)
l2.grid(row=4, column = 2, sticky = W , pady = 2, padx =2)
l3.grid(row=4, column = 3, sticky = W , pady = 2, padx =2)
l4.grid(row=4, column = 4, sticky = W , pady = 2, padx =2)
l5.grid(row=4, column = 5, sticky = W , pady = 2, padx =2)

result = database.show_data()
rows = 5 
for data in result:
    pro = Label(win, text = data[0])
    pro.grid(row = rows, column = 1, sticky = W, pady = 2, padx =2)
    name = Label(win, text = data[1])
    name.grid(row = rows, column = 2, sticky = W, pady = 2, padx =2)
    qty = Label(win, text = data[2])
    qty.grid(row = rows, column = 3, sticky = W, pady = 2, padx =2)
    unit = Label(win, text = data[3])
    unit.grid(row = rows, column = 4, sticky = W, pady = 2, padx =2)
    reoder = Label(win, text = data[4])
    reoder.grid(row = rows, column = 5, sticky = W)
    rows += 1


btn_add = Button(win, text = "Add Product", command = addProduct)
btn_add.grid(row = 1, column = 6, sticky = W, padx = 3, pady = 3)

show = Button(win, text = "Show Sale Table", command = showSale)
show.grid(row = 1, column = 7, sticky = W, padx = 3, pady = 3)

delete = Label(win, text="Delete Record")
delete.grid( row = 50, column = 2,  sticky = W)
E1 = Entry(win)
E1.grid(row = 50, column = 3,  sticky = W)
btn_del =  Button(win, text= "Delete", command = deleteRecod)
btn_del.grid(row = 51, column = 3, sticky = W, padx = 2, pady = 2)



update = Label(win, text="Update Record")
update.grid( row = 52, column = 2,  sticky = W)
E2 = Entry(win)
E2.grid(row = 52, column = 3,  sticky = W)
btn_update =  Button(win, text= "Update", command = updateRecod)
btn_update.grid(row = 53, column = 3, sticky = W, padx = 2, pady = 2)


win.mainloop()