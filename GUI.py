import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from map import creat_map,photo_c

# 登录界面
class Login:
    def __init__(self):
        self.window = tk.Tk()
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        ww = 600
        wh = 600
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.window.title('校园导游系统')
        self.window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        l = tk.Label(self.window, text='欢迎使用校园导游系统', bg='yellow', font=('Arial', 20), width=1200, height=4).pack()
        self.ID = tk.StringVar()
        self.ID.set("")
        self.PW = tk.StringVar()
        self.PW.set("")
        ent_ID = tk.Entry(self.window, show=None, textvariable=self.ID, font=('', 14)).place(x=200, y=250, anchor='w')
        ent_PW = tk.Entry(self.window, show='*', textvariable=self.PW, font=('', 14)).place(x=200, y=300, anchor='w')
        l3 = tk.Label(self.window, text='账号:', bg='pink', font=('', 12)).place(x=180, y=250, anchor='e')
        l4 = tk.Label(self.window, text='密码:', bg='pink', font=('', 12)).place(x=180, y=300, anchor='e')
        self.Ptype = tk.StringVar()
        self.Ptype.set("用户")
        r1 = tk.Radiobutton(self.window, text='管理员', variable=self.Ptype, value='管理员').place(x=280, y=350, anchor="nw")
        r2 = tk.Radiobutton(self.window, text='用户', variable=self.Ptype, value='用户').place(x=280, y=380, anchor="nw")
        b1 = tk.Button(self.window, text='登陆', bg='green', width=6, height=1,
                       command=self.login).place(x=260, y=430, anchor="e")
        b1 = tk.Button(self.window, text='注册', bg='green', width=6, height=1,
                       command=self.creat_P).place(x=340, y=430, anchor="w")
        self.window.mainloop()
    def to_use(self):
        type=self.Ptype.get()
        self.window.destroy()
        use(type)
    def login(self):
        usr_id = self.ID.get()
        usr_pwd = self.PW.get()
        usr_type = self.Ptype.get()
        if usr_type == "管理员":
            with open("Admin.txt", "r+") as fp:
                for line in fp.readlines():
                    a = line.split(" ")
                    if a[0] == usr_id and a[1][:-1] == usr_pwd:
                        tk.messagebox.showinfo(title='Hi', message='登录成功!')  # 提示信息对话窗
                        self.to_use()
                        return
                    elif a[0] == usr_id:
                        tk.messagebox.showwarning(title='警告', message='密码错误')
                        return
                tkinter.messagebox.showwarning(title='警告', message='账号不存在')
                return

            tk.messagebox.showinfo(title='Hi', message='欢迎上线，Administrator！')  # 提示信息对话窗
            # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
            # tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
            # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
            # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
            # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
        else:
            with open("number.txt", "r+") as fp:
                for line in fp.readlines():
                    a = line.split(" ")
                    if a[0] == usr_id and a[1][:-1] == usr_pwd:
                        tk.messagebox.showinfo(title='Hi', message='登录成功!')  # 提示信息对话窗
                        self.to_use()
                        return
                    elif a[0] == usr_id:
                        tk.messagebox.showwarning(title='警告', message='密码错误')
                        return
                tkinter.messagebox.showwarning(title='警告', message='账号不存在')
                return

    def creat_P(self):
        usr_id = self.ID.get()
        usr_pwd = self.PW.get()
        usr_type = self.Ptype.get()
        if usr_type == "管理员":
            tk.messagebox.showwarning(title='警告', message='管理员账号无法注册')
            return
        with open("number.txt", "r+") as fp:
            for line in fp.readlines():
                if line.split(" ")[0] == usr_id:
                    tk.messagebox.showwarning(title='警告', message='用户名已存在')
                    # 提出警告对话窗
                    return
            fp.write("%s %s\n" % (usr_id, usr_pwd))
            tk.messagebox.showinfo(title='Hi', message='注册成功!')
            return


class use:
    def __init__(self,type):
        self.type=type
        self.map = creat_map()
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        if type!="管理员":
            l = tk.Label(self.win, text='用户端',bg='pink', font=('Arial', 20), width=1000, height=3).pack()
            img_png = ImageTk.PhotoImage(photo)
            label_img = tk.Label(self.win, image=img_png).place(x=50,y=130)
            b_check = tk.Button(self.win, text='查询地点信息',font=('Arial', 14),bg='green', command=self.find_mid,width=30).place(x=590,y=240)
            b_mid_min = tk.Button(self.win, text='查询中转最少路径',font=('Arial', 14),bg='green',command=self.transfer_mid,width=30).place(x=590,y=280)
            b_w_min = tk.Button(self.win, text='查询权值最短路径',font=('Arial', 14),bg='green' ,command=self.short_mid,width=30).place(x=590,y=320)
            b_back = tk.Button(self.win, text='返回',font=('Arial', 14),bg='red', command=self.login_mid, width=30).place(x=590,y=520)
        else:
            l = tk.Label(self.win, text='管理端', bg='pink', font=('Arial', 20), width=1000, height=3).pack()
            img_png = ImageTk.PhotoImage(photo)
            label_img = tk.Label(self.win, image=img_png).place(x=50,y=130)
            b_add_node = tk.Button(self.win, text='添加地点',font=('Arial', 14),bg='green', command=self.add_node_mid,width=30).place(x=590,y=240)
            b_add_edge = tk.Button(self.win, text='添加道路',font=('Arial', 14),bg='green', command=self.add_edge_mid,width=30).place(x=590,y=280)
            b_del_edge = tk.Button(self.win, text='删除道路',font=('Arial', 14),bg='green', command=self.del_edge_mid,width=30).place(x=590,y=320)
            b_del_node = tk.Button(self.win, text='删除地点', font=('Arial', 14), bg='green', command=self.del_node_mid,width=30).place(x=590, y=360)
            b_change = tk.Button(self.win, text='修改信息',font=('Arial', 14),bg='green', command=self.change_mid, width=30).place(x=590,y=400)
            b_back = tk.Button(self.win, text='返回',font=('Arial', 14),bg='red', command=self.login_mid, width=30).place(x=590,y=520)
        self.win.mainloop()

    # 中转函数
    def change_mid(self):
        self.win.destroy()
        Change(self.map, self.type)
    def login_mid(self):
        self.win.destroy()
        Login()
    def find_mid(self):
        self.win.destroy()
        Find(self.map,self.type)
    def short_mid(self):
        self.win.destroy()
        Short(self.map, self.type)
    def transfer_mid(self):
        self.win.destroy()
        Transfer(self.map, self.type)
    def del_node_mid(self):
        self.win.destroy()
        Del_Node(self.map,self.type)
    def del_edge_mid(self):
        self.win.destroy()
        Del_Edge(self.map, self.type)
    def add_node_mid(self):
        self.win.destroy()
        Add_Node(self.map, self.type)
    def add_edge_mid(self):
        self.win.destroy()
        Add_edge(self.map, self.type)

# 修改信息
class Change:
    def __init__(self, map, type):
        self.map=map
        self.type=type
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='管理端', bg='pink', font=('Arial', 20), width=1000, height=3)
        l.pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png)
        label_img.place(x=50,y=130)
        self.name1 = tk.StringVar()
        self.name1.set("请输入修改的顶点名")
        self.function_c = tk.StringVar()
        self.function_c.set("请输入功能")
        e1 = tk.Entry(self.win, show=None, textvariable=self.name1, font=('Arial', 14),width=30).place(x=590,y=240)
        e3 = tk.Entry(self.win, show=None, textvariable=self.function_c, font=('Arial', 14),width=30).place(x=590,y=320)
        b = tk.Button(self.win, text='修改',font=('Arial', 14),bg='green',command=self.to_show, width=30).place(x=590,y=480)
        b1 = tk.Button(self.win, text='返回',font=('Arial', 14),bg='red',command=self.to_use, width=30).place(x=590,y=520)
        self.win.mainloop()
    def to_use(self):
        self.win.destroy()
        use(self.type)
    def to_show(self):
        name=self.comvalue.get()
        new=self.name1.get()
        function=self.function_c.get()
        if tkinter.messagebox.askokcancel(title='询问', message='是否要修改'):
            self.map.change(name,new,function)
            tk.messagebox.showinfo(title='Hi', message='修改成功！')  # 提示信息对话窗
        self.win.destroy()
        self.map=creat_map()
        Show_s(new, self.type, self.map)
class Show_s:
    def __init__(self, name, type, map):
        self.name = name
        self.type = type
        self.map = map
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='查找结果:', bg='white', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png)
        label_img.place(x=50,y=130)
        for top in self.map.nodes:
            if self.name == top.name:
                l1 = tk.Label(self.win, text='名称:%s\n坐标:(%s,%s)\n功能:%s' % (top.name, top.x, top.y, top.function),
                              bg='white', font=('Arial', 15), width=25, height=4)
                l1.place(x=590,y=480)
        b1 = tk.Button(self.win, text='返回', command=self.to_change, width=30).place(x=590,y=540)
        self.win.mainloop()
    def to_change(self):
        self.win.destroy()
        Change(self.map, self.type)

# 删除节点
class Del_Node:
    def __init__(self,map,type):
        self.map = map
        self.type = type
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='请选择要删除的节点', bg='white', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png)
        label_img.place(x=50,y=130)
        self.comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist = ttk.Combobox(self.win,font=('Arial', 14),width=30, textvariable=self.comvalue)
        comboxlist.place(x=590,y=240)  # 初始化
        tops = []
        for top in self.map.nodes:
            tops.append(top.name)
        comboxlist["values"] = tuple(tops)
        comboxlist.current(0)
        b = tk.Button(self.win, text='删除',font=('Arial', 14),bg='green',command=self.Del, width=30).place(x=590,y=480)
        b1 = tk.Button(self.win, text='返回',font=('Arial', 14),bg='red',command=self.to_use, width=30).place(x=590,y=520)
        self.win.mainloop()
    def to_use(self):
        self.win.destroy()
        use(self.type)
    def Del(self):
        name=self.comvalue.get()
        if tkinter.messagebox.askokcancel(title='询问', message='是否要删除'):
            self.map.Del_Node(name)
            tk.messagebox.showinfo(title='Hi', message='删除成功！')  # 提示信息对话窗
        self.to_use()

# 删除边
class Del_Edge:
    def __init__(self,map,type):
        self.map=map
        self.type=type
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='管理端', bg='pink', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png)
        label_img.place(x=50,y=130)
        tops = []
        for top in self.map.nodes:
            tops.append(top.name)
        self.comvalue1 = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist1 = ttk.Combobox(self.win,width=30,font=('Arial', 14),textvariable=self.comvalue1)
        comboxlist1.place(x=590,y=240)  # 初始化

        comboxlist1["values"] = tuple(tops)
        comboxlist1.current(0)
        self.comvalue2 = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist2 = ttk.Combobox(self.win,width=30,font=('Arial', 14),textvariable=self.comvalue2)
        comboxlist2.place(x=590,y=320)  # 初始化
        comboxlist2["values"] = tuple(tops)
        comboxlist2.current(0)
        b = tk.Button(self.win, text='删除',font=('Arial', 14),bg='green',command=self.Del, width=30).place(x=590,y=480)
        b1 = tk.Button(self.win, text='返回',font=('Arial', 14),bg='red',command=self.to_use, width=30).place(x=590,y=520)
        self.win.mainloop()
    def to_use(self):
        self.win.destroy()
        use(self.type)
    def Del(self):
        name1=self.comvalue1.get()
        name2=self.comvalue2.get()
        if tkinter.messagebox.askokcancel(title='询问', message='是否要删除'):
            self.map.Del_edge(name1,name2)
            tk.messagebox.showinfo(title='Hi', message='删除成功！')  # 提示信息对话窗
        self.to_use()

# 查询信息
class Find:
    def __init__(self,map,type):
        self.map=map
        self.type=type
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='用户端', bg='pink', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png).place(x=50,y=130)
        self.comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist = ttk.Combobox(self.win, width=30,font=('Arial', 14),textvariable=self.comvalue)
        comboxlist.place(x=590, y=240)  # 初始化
        tops=[]
        for top in self.map.nodes:
            tops.append(top.name)
        comboxlist["values"] = tuple(tops)
        comboxlist.current(0)
        b = tk.Button(self.win, text='查询',font=('Arial', 14), bg='green', command=self.to_show, width=30).place(x=590,y=480)
        b1 = tk.Button(self.win, text='返回', font=('Arial', 14), bg='red', command=self.to_use, width=30).place(x=590, y=520)
        self.win.mainloop()
    def to_use(self):
        self.win.destroy()
        use(self.type)
    def to_show(self):
        name=self.comvalue.get()
        self.win.destroy()
        Print(name,self.type,self.map)
class Print:
    def __init__(self,name,type,map):
        self.name=name
        self.type=type
        self.map=map

        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='用户端', bg='pink', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png).place(x=50,y=130)
        for top in self.map.nodes:
            if self.name == top.name:
                l1 = tk.Label(self.win, text='名称:%s\n坐标:(%s,%s)\n功能:%s'%(top.name,top.x,top.y,top.function),
                              bg='white', font=('Arial', 18), width=25, height=5).place(x=590,y=240)
        b1 = tk.Button(self.win, text='返回',font=('Arial', 14), bg='red', command=self.to_find, width=30).place(x=590,y=520)
        self.win.mainloop()
    def to_find(self):
        self.win.destroy()
        Find(self.map, self.type)

# 中转最少
class Transfer:
    def __init__(self, map, type):
        self.map = map
        self.type = type
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='用户端', bg='pink', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png).place(x=50, y=130)
        self.comvalue1 = tkinter.StringVar()
        comboxlist1 = ttk.Combobox(self.win, width=30, font=('Arial', 14), textvariable=self.comvalue1)
        comboxlist1.place(x=590, y=240)  # 初始化
        tops = []
        for top in self.map.nodes:
            tops.append(top.name)
        comboxlist1["values"] = tuple(tops)
        comboxlist1.current(0)
        self.comvalue2 = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist2 = ttk.Combobox(self.win, width=30, font=('Arial', 14), textvariable=self.comvalue2)
        comboxlist2.place(x=590, y=280)  # 初始化
        comboxlist2["values"] = tuple(tops)
        comboxlist2.current(1)
        b = tk.Button(self.win, text='查询', font=('Arial', 14), bg='green',
                      command=self.to_transfer, width=30).place(x=590, y=480)
        b1 = tk.Button(self.win, text='返回', font=('Arial', 14), bg='red',
                       command=self.to_use, width=30).place(x=590, y=520)
        self.win.mainloop()

    def to_use(self):
        self.win.destroy()
        use(self.type)

    def to_transfer(self):
        name1 = self.comvalue1.get()
        name2 = self.comvalue2.get()
        self.win.destroy()
        Show_mid(self.map, self.type, name1, name2)
class Show_mid:
    def __init__(self,map,type,name1,name2):
        self.map=map
        self.type=type
        self.type = type
        edges=self.map.short_mid(name1,name2)  # 返回路径
        photo = photo_c(self.map.nodes, edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='用户端', bg='pink', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png)
        label_img.place(x=50,y=130)
        str=edges[0].node_1
        for edge in edges:
            str+="->%s"%(edge.node_2)
        l = tk.Label(self.win, text=str, bg='white',font=('Arial', 11), height=5).place(x=570,y=200)
        b1 = tk.Button(self.win, text='返回',font=('Arial', 14), bg='red',
                       command=self.to_transfer, width=30).place(x=590,y=520)
        self.win.mainloop()
    def to_transfer(self):
        self.win.destroy()
        Transfer(self.map,self.type)

# 权值最小
class Short:
    def __init__(self, map, type):
        self.map=map
        self.type=type
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='用户端', bg='pink', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png).place(x=50,y=130)
        self.comvalue1 = tkinter.StringVar()
        comboxlist1 = ttk.Combobox(self.win,width=30,font=('Arial', 14),textvariable=self.comvalue1)
        comboxlist1.place(x=590,y=240)  # 初始化
        tops = []
        for top in self.map.nodes:
            tops.append(top.name)
        comboxlist1["values"] = tuple(tops)
        comboxlist1.current(0)
        self.comvalue2 = tkinter.StringVar()  # 窗体自带的文本，新建一个值
        comboxlist2 = ttk.Combobox(self.win,width=30,font=('Arial', 14),textvariable=self.comvalue2)
        comboxlist2.place(x=590,y=280)  # 初始化
        comboxlist2["values"] = tuple(tops)
        comboxlist2.current(1)
        b = tk.Button(self.win, text='查询',font=('Arial',14),bg='green',
                      command=self.to_show, width=30).place(x=590,y=480)
        b1 = tk.Button(self.win, text='返回',font=('Arial',14),bg='red',
                       command=self.to_use, width=30).place(x=590,y=520)
        self.win.mainloop()
    def to_use(self):
        self.win.destroy()
        use(self.type)
    def to_show(self):
        name1=self.comvalue1.get()
        name2=self.comvalue2.get()
        self.win.destroy()
        Show_c(self.map,self.type,name1,name2)
class Show_c:
    def __init__(self,map,type,name1,name2):
        self.map=map
        self.type=type
        self.type = type
        edges=self.map.short_weight(name1,name2)  # 返回路径
        photo = photo_c(self.map.nodes, edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='用户端', bg='pink', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png)
        label_img.place(x=50,y=130)
        str=edges[0].node_1
        for edge in edges:
            str+="->%s"%(edge.node_2)
        l = tk.Label(self.win, text=str, bg='white',font=('Arial', 11), height=5).place(x=570,y=200)
        b1 = tk.Button(self.win, text='返回',font=('Arial', 14), bg='red',
                       command=self.to_short, width=30).place(x=590,y=520)
        self.win.mainloop()
    def to_short(self):
        self.win.destroy()
        Short(self.map,self.type)

# 添加节点
class Add_Node:
    def __init__(self,map,type):
        self.map=map
        self.type=type
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='管理端', bg='pink', font=('Arial', 20), width=1000, height=3)
        l.pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png)
        label_img.place(x=50,y=130)
        self.name = tk.StringVar()
        self.name.set("请输入结点名")
        self.x = tk.StringVar()
        self.x.set("请输入x")
        self.y = tk.StringVar()
        self.y.set("请输入y")
        self.function = tk.StringVar()
        self.function.set("请输入功能")
        e1 = tk.Entry(self.win, show=None,textvariable=self.name, font=('Arial', 14),width=30).place(x=590, y=240)
        e2 = tk.Entry(self.win, show=None,textvariable=self.x, font=('Arial', 14),width=30).place(x=590, y=280)
        e3 = tk.Entry(self.win, show=None,textvariable=self.y, font=('Arial', 14),width=30).place(x=590, y=320)
        e4 = tk.Entry(self.win, show=None,textvariable=self.function, font=('Arial', 14),width=30).place(x=590,y=360)
        b = tk.Button(self.win, text='添加',font=('Arial', 14),bg='green',
                      command=self.ADD, width=30).place(x=590,y=480)
        b1 = tk.Button(self.win, text='返回',font=('Arial', 14),bg='red',
                       command=self.to_use, width=30).place(x=590,y=520)
        self.win.mainloop()
    def to_use(self):
        self.win.destroy()
        use(self.type)
    def ADD(self):
        name=self.name.get()
        x=self.x.get()
        y=self.y.get()
        function=self.function.get()

        if int(x)<0 or int(x)>640 or int(y)<0 or int(y)>679:
            tk.messagebox.showwarning(title='警告', message='x或y输入异常！')       # 提出警告对话窗
        else:
            if tkinter.messagebox.askokcancel(title='询问', message='是否要添加'):
                self.map.Add_Node(name,x,y,function)
                tk.messagebox.showinfo(title='Hi', message='添加成功！')  # 提示信息对话窗
        self.to_use()

# 删除节点
class Add_edge:
    def __init__(self,map,type):
        self.map=map
        self.type=type
        photo = photo_c(self.map.nodes, self.map.edges)
        self.win = tk.Tk()
        sw = self.win.winfo_screenwidth()
        sh = self.win.winfo_screenheight()
        ww = 1000
        wh = 630
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.win.title('校园导游系统')
        self.win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        l = tk.Label(self.win, text='管理端', bg='pink', font=('Arial', 20), width=1000, height=3).pack()
        img_png = ImageTk.PhotoImage(photo)
        label_img = tk.Label(self.win, image=img_png)
        label_img.place(x=50,y=130)
        self.name1 = tk.StringVar()
        self.name1.set("请输入顶点名")
        self.name2 = tk.StringVar()
        self.name2.set("请输入顶点名")
        self.weight = tk.StringVar()
        self.weight.set("请输入权重")
        e1 = tk.Entry(self.win, show=None,textvariable=self.name1, font=('Arial', 14),width=30).place(x=590,y=240)
        e2 = tk.Entry(self.win, show=None,textvariable=self.name2, font=('Arial', 14),width=30).place(x=590,y=280)
        e3 = tk.Entry(self.win, show=None,textvariable=self.weight, font=('Arial', 14),width=30).place(x=590,y=320)
        b = tk.Button(self.win, text='添加',font=('Arial', 14),bg='green',command=self.ADD, width=30).place(x=590,y=480)
        b1 = tk.Button(self.win, text='返回',font=('Arial', 14),bg='red',command=self.to_use, width=30).place(x=590,y=520)
        self.win.mainloop()
    def to_use(self):
        self.win.destroy()
        use(self.type)
    def ADD(self):
        name1=self.name1.get()
        name2=self.name2.get()
        weight=self.weight.get()
        if tkinter.messagebox.askokcancel(title='询问', message='是否要添加'):
            self.map.Add_Edge(name1,name2,weight)
            tk.messagebox.showinfo(title='Hi', message='添加成功！')  # 提示信息对话窗
        self.to_use()

if __name__ == '__main__':
    Login()