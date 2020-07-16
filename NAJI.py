import tkinter as tk,time
from tkinter.messagebox import *
from tkinter import ttk
from tkinter import *

#阿里云短信生成验证码
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

#生成四位随机验证码
import tkinter.font as tf
import random
import json



from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from PIL import Image,ImageTk

LARGE_FONT = ("Verdana", 12)


class Application(tk.Tk):
    '''

  多页面测试程序

      界面与逻辑分离

  '''

    def __init__(self):
        super().__init__()

        # self.iconbitmap(default="efon.ico")

        self.wm_title("NAJI")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]

        frame.tkraise()  # 切换，将指定画布对象移动到显示列表的顶部


class StartPage(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)

        label = tk.Label(self, text="NAJI----定格情绪瞬间", font=LARGE_FONT)

        label.pack(pady=10, padx=10)

        # button1 = ttk.Button(self, text="去到第一页", command=lambda: root.show_frame(PageOne)).pack()

        # button2 = ttk.Button(self, text="去到第二页", command=lambda: root.show_frame(PageTwo)).pack()

        # button3 = ttk.Button(self, text="去到绘图页", command=lambda: root.show_frame(PageThree)).pack()
        # =================================
        # 欢迎LOGO
        canvas = tk.Canvas(self, width=100, height=160)
        global image_file
        image_file = tk.PhotoImage(file="NAJI.png")
        global image
        image = canvas.create_image(0,0,anchor='nw',image=image_file)
        canvas.pack(side="top")





        # 表单控件 文字
        tk.Label(self, text="用户名").place(x=100, y=200)
        tk.Label(self, text="密  码").place(x=100, y=250)

        # 表单控件 输入框 用户名/密码
        username_text = tk.StringVar()
        entry_username = tk.Entry(self, textvariable=username_text, width=30)
        entry_username.place(x=180, y=200)

        password_text = tk.StringVar()
        entry_password = tk.Entry(self, textvariable=password_text, show="*", width=30)
        entry_password.place(x=180, y=250)
        # 注册登录按钮！！！
        btn_login = tk.Button(self, text="Login", command=lambda:user_login(username_text,password_text,root))
        btn_login.place(x=180, y=290)

        btn_signup = tk.Button(self, text="Sign Up", command=user_signup)
        btn_signup.place(x=280, y=290)


class PageOne(tk.Frame):
    '''第一页'''

    def __init__(self, parent, root):

        #修改颜色函数
        def changecolor():
            pass
        
        # 更新时间,每一秒调用一次
        def update_time():
            clock_label.configure(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
            clock_label.after(1000,update_time)

        super().__init__(parent)

        label = tk.Label(self, text="情绪瞬间", font=LARGE_FONT)

        label.pack(pady=0, padx=10)

        # button1 = ttk.Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).pack()

        # button2 = ttk.Button(self, text="去到第二页", command=lambda: root.show_frame(PageTwo)).pack()

# 时间控件----------------------------------
        clock_label = tk.Label(root)
        clock_label.pack()
        update_time()


        label = tk.Label(self, text="此刻心情", font=LARGE_FONT)
        label.place(x=40, y=40, anchor='nw')

        
        #创建3个单选颜色按钮
        rVar = IntVar()   
        mood1=Radiobutton(self, text="开心", variable=rVar, value=0,command=changecolor)
        mood2=Radiobutton(self, text="愤怒", variable=rVar, value=1,command=changecolor)
        mood3=Radiobutton(self, text="悲伤", variable=rVar, value=2,command=changecolor)
        mood4=Radiobutton(self, text="恐惧", variable=rVar, value=3,command=changecolor)
        mood5=Radiobutton(self, text="焦虑", variable=rVar, value=4,command=changecolor)
        mood6=Radiobutton(self, text="感动", variable=rVar, value=5,command=changecolor)

        #放置颜色按钮
        mood1.place(x=60,  y=70, anchor='nw')
        mood2.place(x=160, y=70, anchor='nw')
        mood3.place(x=260, y=70, anchor='nw')
        mood4.place(x=60,  y=100, anchor='nw')
        mood5.place(x=160, y=100, anchor='nw')
        mood6.place(x=260, y=100, anchor='nw')

        label = tk.Label(self, text="记录一下", font=LARGE_FONT)
        label.place(x=40, y=160, anchor='nw')

        #创建文本框
        ft = tf.Font(family='微软雅黑',size=10,weight=tf.BOLD,slant=tf.ITALIC)
        txt = Text(self,width=60,height=15)
        txt.insert(1.0,"在此编辑你的文本!")
        txt.place(x=60,  y=200, anchor='nw')
        txt.tag_add("myArea",1.0, END)
        txt.tag_config("myArea", foreground="red")
        txt.tag_config("myArea", font = ft)


        #创建一标签用于显示所选内容
        lbl1=Label(self, text="颜色选择",width=10)
        lbl1.place(x=140, y=160, anchor='nw')
        
        #创建一个下拉列表
        value = StringVar()  #绑定变量
        cbox = ttk.Combobox(self, width=10, textvariable=value)
        #设置下拉列表数据
        cbox['values'] = ("红色", "蓝色", "黄色", "绿色","黑色" )  
        cbox.place(x=220, y=160, anchor='nw')
        #设置下拉列表初次显示的项
        cbox.current(0)

        def setColor(event):
            
            if(cbox.get() == '红色'):
                color = 'red'
            elif(cbox.get() == '蓝色'):
                color = 'blue'
            elif(cbox.get() == '黄色'):
                color = 'yellow'
            elif(cbox.get() == '绿色'):
                color = 'green'
            elif(cbox.get() == '黑色'):
                color = 'black'

            print(cbox.get())
            txt.tag_add("myArea",1.0, END)
            txt.tag_config("myArea", foreground=color)
        #绑定事件
        target_mood = 0
        target_text  = ""
        def getTimeInput():
            # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
            return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        def getTextInput():
            target_text=txt.get("1.0","end")
            return target_text
        def getMoodInput():
            target_mood = rVar.get()
            if(target_mood == 0):
                target_mood = '开心'
            elif(target_mood == 1):
                target_mood = '愤怒'
            elif(target_mood == 2):
                target_mood = '悲伤'
            elif(target_mood == 3):
                target_mood = '恐惧'
            elif(target_mood == 4):
                target_mood = '焦虑'
            elif(target_mood == 5):
                target_mood = '感动'
            return target_mood
        def perDataSave():

            per_data = []
            per_data.append(getTimeInput())
            per_data.append(getTextInput())
            per_data.append(getMoodInput())
            exists_user_info[user_name]["text"].append(per_data)
            saveText(exists_user_info)
            print(exists_user_info)
            # getTimeInput()
            # target_mood = rVar.get()
            # print(target_mood)
            # getTextInput()
        def search():
            window_signup = tk.Toplevel()
            window_signup.title('welocme to sign up')
            window_signup.geometry('600x500')
            
            label = tk.Label(window_signup, text="情绪历史", font=LARGE_FONT)

            label.pack(pady=10, padx=10)


            global exists_user_info
            exists_user_info = readAccouts()

            print('-=-=-=-=-=-=-=-=-=-=')
            # print(exists_user_info)
            print(len(exists_user_info[user_name]["text"]))
            print('-=-=-=-=-=-=-=-=-=-=')
            length = len(exists_user_info[user_name]["text"])
            print(type(length))
            # print(len(exists_user_info["text"]))
            for i in range(length):
                # print(i)
                label = tk.Label(window_signup, text=exists_user_info[user_name]["text"][i][0], font=LARGE_FONT)
                label.place(x=40, y=70+80*i, anchor='nw')

                label = tk.Label(window_signup, text=exists_user_info[user_name]["text"][i][2], font=LARGE_FONT ,fg="green")
                label.place(x=400, y=70+80*i, anchor='nw')

                label = tk.Label(window_signup, text=exists_user_info[user_name]["text"][i][1], font=LARGE_FONT ,fg="skyblue")
                label.place(x=60, y=100+80*i, anchor='nw')

            

            # label = tk.Label(self, text="此刻心情", font=LARGE_FONT)
            # label.place(x=40, y=150, anchor='nw')

            # label = tk.Label(self, text="开心", font=LARGE_FONT)
            # label.place(x=400, y=150, anchor='nw')

            # label = tk.Label(self, text="此刻心情", font=LARGE_FONT)
            # label.place(x=60, y=180, anchor='nw')





        cbox.bind("<<ComboboxSelected>>",setColor)

        btn_deposit=Button(self,text="保存",width=15,height=4,command=perDataSave)
        btn_deposit.place(x=100, y=450, anchor='nw')
        btn_withdraw=Button(self,text="查询",width=15,height=4,command=search)
        btn_withdraw.place(x=300, y=450, anchor='nw')
        # button2 = ttk.Button(self, text="去到第二页", command=lambda: root.show_frame(PageTwo)).pack()
        


class PageThree(tk.Frame):
    '''第三页'''

    def __init__(self, parent, root):
        super().__init__(parent)

        tk.Label(self, text="这是绘图页", font=LARGE_FONT).pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="回到主页", command=lambda: root.show_frame(StartPage)).pack()

        fig = Figure(figsize=(5, 5), dpi=100)

        a = fig.add_subplot(111)

        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(fig, self)

        canvas.draw()

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)

        toolbar.update()

        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# 点击登陆按钮后处理的业务逻辑
def user_login(username_text,password_text,root):
    # 获取用户的登陆信息
    global user_name
    user_name = username_text.get()
    user_pwd = password_text.get()

    # 将用户信息存入本地
    global exists_user_info
    exists_user_info = readAccouts()
    print(exists_user_info)
    # 验证用户信息是否正确
    if user_name in exists_user_info:
        if (user_pwd == exists_user_info[user_name]["password"]):
            tk.messagebox.showinfo(title='welcome', message='hello ' + user_name)
            # Application().show_frame(PageOne)
            root.show_frame(PageOne)
        else:
            tk.messagebox.showerror(title='error', message='密码错误，请重试！')
    else:
        is_sign_up = tk.messagebox.askyesno(title="是否注册", message="您还没注册，请问是否注册呢？")
        if (is_sign_up):
            user_signup()

# 读取txt数据
def readAccouts():
    d = {}
    with open("data.txt") as f:
        for line in f:
            record = line.split()
            # print('-------------------------------------')
            # print(record)
            # print(record[0])
            # print(record[1])
            # print(record[2])
            # print('-------------------------------------')
            # record[1] = float(record[1])
            tmp_dict = {}
            tmp_dict["username"] = record[1]
            tmp_dict["password"] = record[2]
            if(len(record) == 3):
                tmp_dict["text"] = []
                # print('yes')
            else:
                # tmp_dict["text"] = json.loads(record[3])
                new_str=""
                new_record = line.split()[3:]
                for a in new_record:
                    new_str += a + ' '
                print(new_str)
                print(type(new_str))
                tmp_dict["text"] = json.loads(new_str)
            d[record[0]] = tmp_dict
    print(d)
    return d

def saveAccounts(d):
        print(d)
        with open("test.txt","w") as f:
            for name,item in d.items():
                username = item['username']
                password = item['password']
                f.write(f'{name}\t{username}\t{password}\n')    

def saveText(d):
        print(d)
        with open("test.txt","w") as f:
                for name,item in d.items():
                    username = item['username']
                    password = item['password']
                    text = json.dumps(item['text'])
                    f.write(f'{name}\t{username}\t{password}\t{text}\n')    

# 点击注册按钮后处理的业务逻辑
def user_signup():
    def sign_to_database(cha_num):

        n_pwd = new_pwd.get()
        nr_pwd = new_CHA.get()
        n_name = new_name.get()
        cha_num = cha_num
        # 读取本地用户信息
        global exists_user_info
        exists_user_info = readAccouts()
        if(len(n_name) != 11):
            tk.messagebox.showerror(title='error', message='手机号错误，请重试！')
            pass
        else:
            # 判断是两处密码是否一致
            if (cha_num != nr_pwd):
                tk.messagebox.showerror(title='error', message='验证码错误，请重试！')
                pass
            else:
                # 判断该用户是否存在数据库
                if (n_name in exists_user_info):
                    tk.messagebox.showerror(title='error', message='该用户已存在！')
                else:
                    # 更新写入本地数据
                    tmp = {}
                    tmp["username"] = n_name
                    tmp["password"] = n_pwd
                    exists_user_info[n_name] = tmp
                    # exists_user_info[n_name].username = n_name
                    # exists_user_info[n_name].password = n_pwd
                    print(exists_user_info)
                    # with open("user_info.pickle", 'wb') as f:
                    #     pickle.dump(exists_user_info, f)
                    saveAccounts(exists_user_info)
                    # 注册成功
                    tk.messagebox.showinfo(title='welocme', message='注册成功！')
                    # 关闭窗口
                    window_signup.destroy()




    # window = tk.Tk()
    window_signup = tk.Toplevel()
    window_signup.title('welocme to sign up')
    window_signup.geometry('350x200')
# 获取手机账号
    new_name = tk.StringVar()
    # new_name.set('example@python.com')
    tk.Label(window_signup, text='手机账号: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_signup, textvariable=new_name)
    entry_new_name.place(x=150, y=10)
# 获取设置密码
    new_pwd = tk.StringVar()
    tk.Label(window_signup, text='设置密码: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_signup, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

# 获取验证码
    new_CHA = tk.StringVar()
    tk.Label(window_signup, text="验证码: ").place(x=10, y=90)
    tk.Entry(window_signup, textvariable=new_CHA).place(x=150, y=90,width=100)

    # 短信验证码框


    def foo():
        global tim  # 标识全局变量
        clock = but.after(1000, foo)  # 延迟调用foo，每1000毫秒一次
        tim = tim - 1  # 倒计时
        if tim == 0:  # 如果倒计时为零时
            but['text'] = '再次发送'  # 按钮文字显示再次发送
            tim = 60  # 全局变量复原
            but.after_cancel(clock)  # 取消after时钟函数
            but['state'] = 'normal'  # 让按钮可用
        else:
            but['state'] = 'disable'  # 让按钮在倒计时期间不可用
            but['text'] = str(tim)  # 设置按钮显示文字倒计时

    def but_click(cha_num):
        phone_number=new_name.get()
        if(len(phone_number) == 11):
            but.after(1000, foo)  # 每1000毫秒调用一次foo
            # 调用阿里云短信服务
            client=AcsClient('LTAI4GDi1naCAPKMPbsrnmnS','CwM5eMsusKmISdzyRjKkrJBGxN5yyv','cn-hangzhou')
            
            print(phone_number)
            print(cha_num)
            
            #进行短信验证开始
            req1 = CommonRequest()
            req1.set_accept_format('json')
            req1.set_domain('dysmsapi.aliyuncs.com')
            req1.set_method('POST')
            req1.set_protocol_type('https') # https | http
            req1.set_version('2017-05-25')
            req1.set_action_name('SendSms')
            req1.add_query_param('RegionId', "cn-hangzhou")
            req1.add_query_param('PhoneNumbers', phone_number)
            req1.add_query_param('SignName', "NAJI纳己")
            req1.add_query_param('TemplateCode', "SMS_190727303")
            req1.add_query_param('TemplateParam', "{\"code\":\""+cha_num+"\"}")

            #进行短信验证结束
            req1.add_query_param('RegionId', "cn-hangzhou")

            response = client.do_action(req1)
            # python2:  print(response) 
            print(str(response, encoding = 'utf-8'))
        else:
            showinfo(title='错误提示', message='请输入正确的手机号')

    cha_num=str(random.randint(1000,9999))
    but = tk.Button(window_signup, text='倒计时', command=lambda:but_click(cha_num), width=10, bg='yellow')
    but.pack(side='right', padx=10, pady=80)
    

    # 确定按钮
    btn_comfirm_signup = tk.Button(window_signup, text="注册", command=lambda:sign_to_database(cha_num)).place(x=150, y=130)
    pass


if __name__ == '__main__':
    # 实例化Application

    # 图片
    image_file = ''
    image = ''
    # 图片


    user_name = ""
    exists_user_info = {}
    tim = 60  # 计时时长
    app = Application()

    # 主消息循环:

    app.mainloop()
