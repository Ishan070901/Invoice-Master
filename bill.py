from tkinter import*
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title("BILLING SOFTWARE")
        bg_color='#737373'
        title=Label(self.root,text='Billing Software',bd=12,relief=GROOVE,bg=bg_color,fg='black'  ,font=('times new roman',30,'bold'),pady=2).pack(fill=X)

#================VARIABLES=====================


#===============cosmetics=========
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()


# =============grocery==============
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

#===========Cold Drinks===============
        self.maza=IntVar()
        self.redbull=IntVar()
        self.frooti=IntVar()
        self.thumbs_up=IntVar()
        self.slice=IntVar()
        self.sprite=IntVar()


#==============Total product price & Tax variable===========
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drinks_price=StringVar()


        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()



#=========customer=============
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()


#===========CUSTOMER DETAILS =====================


        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text='Customer Details',font=('times new roman',15,'bold'),fg='#b3003b',bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)



        cname_lb1=Label(F1,text='Customer Name',bg=bg_color,font=('times new roman',15,'bold')).grid(row=0,column=0, padx=20,pady=5 )
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font='arial 15',bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lb1 = Label(F1, text='Phone No.', bg=bg_color, font=('times new roman', 15, 'bold')).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt = Entry(F1, width=15,textvariable=self.c_phone ,font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        cbill_lb1 = Label(F1, text='Bill Number', bg=bg_color, font=('times new roman', 15, 'bold')).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt = Entry(F1, width=15, textvariable=self.search_bill,font='arial 15', bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text='Search',width=10,bd=7,font='arial 12 bold').grid(row=0,column=6,pady=10,padx=10)


#===========COSMATICS DETAILS============================


        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text='Cosmetics',font=('times new roman',15,'bold'),fg='#b3003b',bg=bg_color)
        F2.place(x=5,y=180,width=325,height=370)



        bath_lbl=Label(F2,text='Bath Soap',font=('times new roman',16,'bold'),bg=bg_color,fg='BLACK').grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl = Label(F2, text='Face Cream', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream ,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        Face_wash_lbl = Label(F2, text='Face Wash', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_wash_txt = Entry(F2, width=10,textvariable=self.face_wash, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10, textvariable=self.spray,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        Hair_g_lbl = Label(F2, text='Hair Gel', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10, textvariable=self.gel,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        Body_lbl = Label(F2, text='Body Lotion', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_txt = Entry(F2, width=10, textvariable=self.lotion,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5 ,column=1,padx=10,pady=10)




#==========Grocery Frame===================================

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text='Grocery', font=('times new roman', 15, 'bold'),fg='#b3003b', bg=bg_color)
        F3.place(x=340, y=180, width=300, height=370)

        g1_lbl = Label(F3, text='Rice', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3, width=10, textvariable=self.rice,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        g2_lbl = Label(F3, text='Food Oil', font=('times new roman', 16, 'bold'), bg=bg_color,fg='BLACK').grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3, width=10, textvariable=self.food_oil,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl = Label(F3, text='Daal', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3, width=10, textvariable=self.daal,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_txt = Entry(F3, width=10, textvariable=self.wheat,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl = Label(F3, text='Sugar', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3, width=10, textvariable=self.sugar,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl = Label(F3, text='Tea', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3, width=10, textvariable=self.tea,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)



#===============Cold Drinks============================

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text='Cold Drinks', font=('times new roman', 15, 'bold'),fg='#b3003b', bg=bg_color)
        F4.place(x=650, y=180, width=300, height=370)

        c1_lbl = Label(F4, text='Maza', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt = Entry(F4, width=10, textvariable=self.maza,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        c2_lbl = Label(F4, text='RedBull', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt = Entry(F4, width=10, textvariable=self.redbull,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        c3_lbl = Label(F4, text='Frooti', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt = Entry(F4, width=10, textvariable=self.frooti,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10, pady=10)

        c4_lbl = Label(F4, text="Thumbs up", font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt = Entry(F4, width=10, textvariable=self.thumbs_up,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10, pady=10)

        c5_lbl = Label(F4, text='Slice', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt = Entry(F4, width=10, textvariable=self.slice,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10, pady=10)

        c6_lbl = Label(F4, text='Sprite', font=('times new roman', 16, 'bold'), bg=bg_color, fg='BLACK').grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt = Entry(F4, width=10, textvariable=self.sprite,font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)


#==========BIll AREA====================================

        F5 =Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=960, y=180, width=310, height=370)
        bill_title=Label(F5,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

#=================Button Frame========================

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu ", font=('times new roman', 15, 'bold'),fg='#b3003b', bg=bg_color)
        F6.place(x=0,y=555,relwidth=1,height=140)

        m1=Label(F6,text='Total Cometics Price',bg=bg_color,fg='black',font=('times new roman',14,'bold')).grid(row=0,column=0 ,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2 = Label(F6, text='Total Grocery Price', bg=bg_color, fg='black', font=('times new roman', 14, 'bold')).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text='Total Cold Drinks Price', bg=bg_color, fg='black', font=('times new roman', 14, 'bold')).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price,font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1 = Label(F6, text='Cometics Tax', bg=bg_color, fg='black', font=('times new roman', 14, 'bold')).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax,font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2 = Label(F6, text='Grocery Tax', bg=bg_color, fg='black', font=('times new roman', 14, 'bold')).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax,font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3 = Label(F6, text='Cold Drinks Tax', bg=bg_color, fg='black',font=('times new roman', 14, 'bold')).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax,font='arial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=3 , padx=10, pady=1)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=505,height=105)

        total_btn=Button(btn_F,text='Total',bg=bg_color,fg='black',bd=5,pady=15,width=8,font='arial 15 bold ').grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text='Bill',bg=bg_color,fg='black',bd=5,pady=15,width=8,font='arial 15 bold ').grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text='Clear',bg=bg_color,fg='black',bd=5,pady=15,width=8,font='arial 15 bold ').grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text='Exit',bg=bg_color,fg='black',bd=5,pady=15,width=8,font='arial 15 bold ').grid(row=0,column=3,padx=5,pady=5)



    def total(self):
         self.total_cosmetic_price=(
                                     (self.soap.get()*40)+
                                     (self.face_cream.get() *120)+
                                     (self.face_wash.get() * 60)+
                                     (self.spray.get() * 180)+
                                     (self.gel.get() * 140)+
                                     (self.lotion.get() * 150)
                                     )

         self.cosmetic_price.set(str(self.total_cosmetic_price))

root=Tk()
obj =  Bill_App(root)
root.mainloop()