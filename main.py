import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
account = 'root'
keypass = '226030226030zwkZ'
database = 'database'
gender = ['男','女']
dept = ['CS','CS','MA','IS']
id_len = 9

# -----------------------------------开始页面-----------------------------------------

class StartPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生信息管理系统')
        self.window.geometry('300x470')

        label = Label(self.window, text="学生信息管理系统", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="管理员登陆", font=tkFont.Font(size=16), command=lambda: Admin_login(self.window), width=30,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="学生登陆", font=tkFont.Font(size=16), command=lambda: Student_login(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="教师登陆", font=tkFont.Font(size=16), command=lambda: TeaPage(self.window),
               width=30,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text='退出系统', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

        self.window.mainloop()  # 主消息循环

    def teacher_login(self):
        messagebox.showinfo("教师登录", "教师登录功能待实现")

#------------------------------------管理员模块------------------------------------------

# 管理员操作界面
class Admin_manage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员操作系统')
        self.window.geometry('300x470')

        label = Label(self.window, text="管理员操作系统", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="学生信息管理系统", font=tkFont.Font(size=16), command=lambda: student_manage(self.window), width=30,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="教师信息管理系统", font=tkFont.Font(size=16), command=lambda: teacher_manage(self.window), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="课程信息管理系统", font=tkFont.Font(size=16), command=lambda: course_manage(self.window),
               width=30,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="选课信息管理系统", font=tkFont.Font(size=16), command=lambda: s_course_manage(self.window),
               width=30,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

        Button(self.window, text='退出系统', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        self.window.mainloop()  # 主消息循环


    def teacher_login(self):
        messagebox.showinfo("选课信息", "选课功能待实现")
# 管理员选课信息界面
class s_course_manage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('管理员操作界面')

        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=250)
        self.frame_center = tk.Frame(width=500, height=200)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号","学生姓名", "课程号","课程名","成绩")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("学生姓名", width=100, anchor='center')
        self.tree.column("课程号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("课程名", width=100, anchor='center')
        self.tree.column("成绩", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.SNO = []
        self.NAME = []
        self.CNO = []
        self.CNAME = []
        self.grade = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT s.SNO, sk.name, s.CNO, c.CNAME, s.GRADE   \
                FROM s_course s \
                JOIN student_k sk ON s.SNO = sk.id  \
                JOIN course c ON s.CNO = c.CNO  \
            "  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.SNO.append(row[0])
                self.NAME.append(row[1])
                self.CNO.append(row[2])
                self.CNAME.append(row[3])
                self.grade.append(row[4])

            # print(self.CNO)
            # print(self.CNAME)
            # print(self.gender)
            # print(self.CCREDIR)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.CNO), len(self.CNAME))):  # 写入数据
            self.tree.insert('', i, values=(self.SNO[i], self.NAME[i], self.CNO[i],self.CNAME[i],self.grade[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="课程信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_sno = StringVar()  # 声明工号
        self.var_name = StringVar()  # 声明姓名
        self.var_cno = IntVar()  # 声明年龄
        self.var_cname = StringVar()  # 声明专业
        self.var_grade = IntVar()
        # 课程号
        self.right_top_id_label = Label(self.frame_left_top, text="学号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_sno, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 课程名
        self.right_top_name_label = Label(self.frame_left_top, text="学生姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 学分
        self.right_top_age_label = Label(self.frame_left_top, text="课程号：", font=('Verdana', 15))
        self.right_top_age_entry = Entry(self.frame_left_top, textvariable=self.var_cno,
                                            font=('Verdana', 15))
        self.right_top_age_label.grid(row=3, column=0)  # 位置设置
        self.right_top_age_entry.grid(row=3, column=1)
        # 授课老师
        self.right_top_dept_label = Label(self.frame_left_top, text="课程名：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_cname,
                                            font=('Verdana', 15))
        self.right_top_dept_label.grid(row=4, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=4, column=1)

        self.right_top_dept_label = Label(self.frame_left_top, text="成绩：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_grade,
                                            font=('Verdana', 15))
        self.right_top_dept_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=5, column=1)
        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建选课信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='修改学生成绩信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中选课信息', width=20,
                                            command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='(学号)查询选课信息', width=20,command=self.find)
        self.right_top_button5 = ttk.Button(self.frame_bottom, text='退出选课信息管理系统', width=20,command=self.back)
        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=4, column=0, padx=20, pady=10)
        self.right_top_button5.grid(row=5, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=1, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击


    def back(self):
        Admin_manage(self.window)  # 显示主窗口 销毁本窗口

    def CHECK(self):
        if len(self.var_sno.get()) != id_len or (self.var_grade.get() < 0 or self.var_grade.get() > 100):
            messagebox.showinfo('错误！', '请注意信息更新规范！如工号、性别、学分、授课老师')
            return 1
        else:
            return 0
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_sno.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_cno.set(self.row_info[2])
        self.var_cname.set(self.row_info[3])
        self.var_grade.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_sno,
                                        font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def find(self):
        # 数据库操作 查询管理员表
        row = None
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass) # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT s.SNO, sk.name, s.CNO, c.CNAME, s.GRADE   \
                FROM s_course s \
                JOIN student_k sk ON s.SNO = sk.id  \
                JOIN course c ON s.CNO = c.CNO  WHERE s.SNO = '%s' and s.CNO = '%s'" % (self.right_top_id_entry.get(),self.right_top_age_entry.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                # 打印结果
                #print("cno=%s,cname=%s,credit=%s,teacher=%s" % (cno, cname,ccredit,cteacher))
                self.var_sno.set(row[0])
                self.var_name.set(row[1])
                self.var_cno.set(row[2])
                self.var_cname.set(row[3])
                self.var_grade.set(row[4])
                db.close()  # 关闭数据库连接
                return row
        except:
            print("Error: 未找到该选课信息")
            messagebox.showinfo('异常！', '未找到该选课！')
        return None
    def new_row(self):
        if self.CHECK():
            return
        print(self.var_cno.get())
        print(self.CNO)
        row = self.find()
        row1 = None
        if row is not None :
            messagebox.showinfo('警告！', '该课程已存在！')
        else:
            if self.var_cno.get() != '' and self.var_cname.get() != '':
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO s_course(SNO, CNO, GRADE) \
				       VALUES ('%s', '%s', '%s')" % \
                      (self.var_sno.get(), self.var_cno.get(), self.var_grade.get())  # SQL 插入语句

                sql_show = "SELECT s.SNO, sk.name, s.CNO, c.CNAME, s.GRADE   \
                FROM s_course s \
                JOIN student_k sk ON s.SNO = sk.id  \
                JOIN course c ON s.CNO = c.CNO  WHERE s.SNO = '%s' and s.CNO = '%s'" % (self.var_sno.get(),self.var_cno.get())  # SQL 查询语句

                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行

                    # 执行SQL语句
                    cursor.execute(sql_show)
                    # 获取所有记录列表
                    results = cursor.fetchall()
                    for row in results:
                        # 打印结果
                        # print("cno=%s,cname=%s,credit=%s,teacher=%s" % (cno, cname,ccredit,cteacher))
                        self.var_sno.set(row[0])
                        self.var_name.set(row[1])
                        self.var_cno.set(row[2])
                        self.var_cname.set(row[3])
                        self.var_grade.set(row[4])
                        row1 = row
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.SNO.append(self.var_sno.get())
                self.NAME.append(row1[1])
                self.CNO.append(self.var_cno.get())
                self.CNAME.append(row1[3])
                self.grade.append(self.var_grade.get())
                self.tree.insert('', len(self.CNO) - 1, values=(
                    self.SNO[len(self.CNO) - 1], self.NAME[len(self.CNO) - 1],
                    self.CNO[len(self.CNO) - 1],self.CNAME[len(self.CNO) - 1],self.grade[len(self.CNO) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写课程数据')

    def updata_row(self):
        if self.CHECK():
            return
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_sno.get() == self.row_info[0]:  # 如果所填工号 与 所选工号一致
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql_update = f"UPDATE s_course SET SNO= '{self.var_sno.get()}', CNO = '{self.var_cno.get()}', GRADE = '{self.var_grade.get()}' WHERE SNO = '{self.var_sno.get()}' and CNO = '{self.var_cno.get()}'"  # SQL 插入语句
                try:
                    cursor.execute(sql_update)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接
                row = self.find()
                id_index = self.SNO.index(self.row_info[0])
                self.SNO[id_index] = row[0]
                self.NAME[id_index] = row[1]
                self.CNO[id_index] = row[2]
                self.CNAME[id_index] = row[3]
                self.grade[id_index] = row[4]
                self.tree.item(self.tree.selection()[id_index], values=(
                    self.var_sno.get(), self.var_name.get(),
                    self.var_cno.get(),self.var_cname.get(),self.var_grade.get()))  # 修改对于行信息
            else:
                messagebox.showinfo('警告！', '不能修改课程学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的工号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_delete = "DELETE FROM s_course WHERE SNO = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql_delete)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.SNO.index(self.row_info[0])
            print(id_index)
            del self.SNO[id_index]
            del self.NAME[id_index]
            del self.CNO[id_index]
            del self.CNAME[id_index]
            del self.grade[id_index]
            print(self.CNO)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())
# 管理员课程信息界面
class course_manage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('管理员操作界面')

        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=250)
        self.frame_center = tk.Frame(width=500, height=200)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("课程号", "课程名", "学分","授课老师工号","授课老师")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("课程号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("课程名", width=100, anchor='center')
        self.tree.column("学分", width=100, anchor='center')
        self.tree.column("授课老师工号", width=100, anchor='center')
        self.tree.column("授课老师", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.CNO = []
        self.CNAME = []
        self.CCREDIR = []
        self.CTEACHER = []
        self.CTNAME = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        #sql = "SELECT * FROM course"  # SQL 查询语句
        sql ="SELECT course.*, teacher_k.tea_name \
            FROM course \
            JOIN teacher_k ON course.CTEACHER = teacher_k.tea_id"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.CNO.append(row[0])
                self.CNAME.append(row[1])
                self.CCREDIR.append(row[2])
                self.CTEACHER.append(row[3])
                self.CTNAME.append(row[4])
            # print(self.CNO)
            # print(self.CNAME)
            # print(self.gender)
            # print(self.CCREDIR)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.CNO), len(self.CNAME), len(self.CCREDIR),len(self.CTEACHER))):  # 写入数据
            self.tree.insert('', i, values=(self.CNO[i], self.CNAME[i], self.CCREDIR[i],self.CTEACHER[i],self.CTNAME[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="课程信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_cno = StringVar()  # 声明工号
        self.var_cname = StringVar()  # 声明姓名
        self.var_ccredit = IntVar()  # 声明年龄
        self.var_cteacher = StringVar()  # 声明专业
        self.var_ctname = StringVar()  # 声明
        # 课程号
        self.right_top_id_label = Label(self.frame_left_top, text="课程号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_cno, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 课程名
        self.right_top_name_label = Label(self.frame_left_top, text="课程名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_cname, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 学分
        self.right_top_age_label = Label(self.frame_left_top, text="学分：", font=('Verdana', 15))
        self.right_top_age_entry = Entry(self.frame_left_top, textvariable=self.var_ccredit,
                                            font=('Verdana', 15))
        self.right_top_age_label.grid(row=3, column=0)  # 位置设置
        self.right_top_age_entry.grid(row=3, column=1)
        # 授课老师工号
        self.right_top_dept_label = Label(self.frame_left_top, text="授课老师工号：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_cteacher,
                                            font=('Verdana', 15))
        self.right_top_dept_label.grid(row=4, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=4, column=1)

        self.right_top_dept_label = Label(self.frame_left_top, text="授课老师：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_ctname,
                                            font=('Verdana', 15))
        self.right_top_dept_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建课程信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中课程信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中课程信息', width=20,
                                            command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='(课程号)查询课程信息', width=20,command=self.find)
        self.right_top_button5 = ttk.Button(self.frame_bottom, text='退出课程信息管理系统', width=20,command=self.back)
        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=4, column=0, padx=20, pady=10)
        self.right_top_button5.grid(row=5, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=1, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击


    def back(self):
        Admin_manage(self.window)  # 显示主窗口 销毁本窗口

    def CHECK(self):
        if self.var_ccredit.get() < 0 or self.var_ccredit.get() > 10:
            messagebox.showinfo('错误！', '请注意信息更新规范！如学分')
            return 1
        else:
            return 0
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        print(self.row_info)
        self.var_cno.set(self.row_info[0])
        self.var_cname.set(self.row_info[1])
        self.var_ccredit.set(self.row_info[2])
        self.var_cteacher.set(self.row_info[3])
        self.var_ctname.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_cno,
                                        font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def find(self):
        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass) # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT course.*, teacher_k.tea_name \
            FROM course \
            JOIN teacher_k ON course.CTEACHER = teacher_k.tea_id WHERE CNO = '%s'" % (self.right_top_id_entry.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                cno = row[0]
                cname = row[1]
                ccredit = row[2]
                cteacher = row[3]
                ctname = row[4]
                # 打印结果
                print("cno=%s,cname=%s,credit=%s,teacher=%s" % (cno, cname,ccredit,cteacher))
                self.var_cno.set(cno)
                self.var_cname.set(cname)
                self.var_ccredit.set(ccredit)
                self.var_cteacher.set(cteacher)
                self.var_ctname.set(ctname)
        except:
            print("Error: 未找到该同学")
            messagebox.showinfo('异常！', '未找到该同学！')
        db.close()  # 关闭数据库连接
        return ctname
    def new_row(self):
        if self.CHECK():
            return
        print(self.var_cno.get())
        print(self.CNO)
        if str(self.var_cno.get()) in self.CNO:
            messagebox.showinfo('警告！', '该课程已存在！')
        else:
            if self.var_cno.get() != '' and self.var_cname.get() != '' and self.var_ccredit.get() != 0:
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO course(CNO, CNAME, CCREDIT, CTEACHER) \
				       VALUES ('%s', '%s', '%s','%s')" % \
                      (self.var_cno.get(), self.var_cname.get(), self.var_ccredit.get(),self.var_cteacher.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
                ctname=self.find()
                self.CNO.append(self.var_cno.get())
                self.CNAME.append(self.var_cname.get())
                self.CCREDIR.append(self.var_ccredit.get())
                self.CTEACHER.append(self.var_cteacher.get())
                self.CTNAME.append(ctname)
                self.tree.insert('', len(self.CNO) - 1, values=(
                    self.CNO[len(self.CNO) - 1], self.CNAME[len(self.CNO) - 1],
                    self.CCREDIR[len(self.CNO) - 1],self.CTEACHER[len(self.CNO) - 1],ctname))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写课程数据')

    def updata_row(self):
        if self.CHECK():
            return
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_cno.get() == self.row_info[0]:  # 如果所填工号 与 所选工号一致
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql_update = f"UPDATE course SET CNAME = '{self.var_cname.get()}', CCREDIT = '{self.var_ccredit.get()}', CTEACHER = '{self.var_cteacher.get()}' WHERE CNO = '{self.var_cno.get()}'"  # SQL 插入语句

                try:
                    cursor.execute(sql_update)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')

                db.close()  # 关闭数据库连接
                ctname = self.find()
                id_index = self.CNO.index(self.row_info[0])
                self.CNAME[id_index] = self.var_cname.get()
                self.CCREDIR[id_index] = self.var_ccredit.get()
                self.CTEACHER[id_index] = self.var_cteacher.get()
                self.CTNAME[id_index]=ctname
                self.tree.item(self.tree.selection()[id_index], values=(
                    self.var_cno.get(), self.var_cname.get(),
                    self.var_ccredit.get(),self.var_cteacher.get(),ctname))  # 修改对于行信息
            else:
                messagebox.showinfo('警告！', '不能修改课程号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的工号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_delete = "DELETE FROM course WHERE CNO = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql_delete)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.CNO.index(self.row_info[0])
            print(id_index)
            del self.CNO[id_index]
            del self.CNAME[id_index]
            del self.CCREDIR[id_index]
            del self.CTNAME[id_index]
            del self.CTEACHER[id_index]
            print(self.CNO)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())
# 管理员教师信息界面
class teacher_manage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('管理员操作界面')

        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=250)
        self.frame_center = tk.Frame(width=500, height=200)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("工号", "姓名", "性别", "年龄","专业")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("工号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("年龄", width=100, anchor='center')
        self.tree.column("专业", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.dept = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teacher_k"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                self.dept.append(row[4])
            # print(self.id)
            # print(self.name)
            # print(self.gender)
            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age),len(self.dept))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i],self.dept[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="教师信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明工号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = IntVar()  # 声明年龄
        self.var_dept = StringVar()  # 声明专业
        # 工号
        self.right_top_id_label = Label(self.frame_left_top, text="工号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 性别
        self.right_top_gender_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender,
                                            font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 年龄
        self.right_top_age_label = Label(self.frame_left_top, text="年龄：", font=('Verdana', 15))
        self.right_top_age_entry = Entry(self.frame_left_top, textvariable=self.var_age,
                                            font=('Verdana', 15))
        self.right_top_age_label.grid(row=4, column=0)  # 位置设置
        self.right_top_age_entry.grid(row=4, column=1)

        # 专业
        self.right_top_dept_label = Label(self.frame_left_top, text="专业：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_dept,
                                            font=('Verdana', 15))
        self.right_top_dept_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建教师信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中教师信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中教师信息', width=20,
                                            command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='(工号)查询教师信息', width=20,command=self.find)
        self.right_top_button5 = ttk.Button(self.frame_bottom, text='退出教师信息管理系统', width=20,command=self.back)
        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=4, column=0, padx=20, pady=10)
        self.right_top_button5.grid(row=5, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=1, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击


    def back(self):
        Admin_manage(self.window)  # 显示主窗口 销毁本窗口

    def CHECK(self):
        if len(self.var_id.get()) != 5 or (self.var_age.get() < 0 or self.var_age.get() > 100) or \
                (self.var_gender.get() not in gender) or (self.var_dept.get() not in dept):
            messagebox.showinfo('错误！', '请注意信息更新规范！如工号、性别、年龄、专业')
            return 1
        else:
            return 0
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.var_dept.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def find(self):
        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass) # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM course WHERE tea_id = '%s'" % (self.right_top_id_entry.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                stu_id = row[0]
                stu_name = row[1]
                stu_gender = row[2]
                stu_age = row[3]
                stu_dept = row[4]
                # 打印结果
                print("id=%s,name=%s,gender=%s,age=%s,dept=%s" % (stu_id, stu_name,stu_gender,stu_age,stu_dept))
                self.var_id.set(stu_id)
                self.var_name.set(stu_name)
                self.var_gender.set(stu_gender)
                self.var_age.set(stu_age)
                self.var_dept.set(stu_dept)
        except:
            print("Error: 未找到该同学")
            messagebox.showinfo('异常！', '未找到该同学！')
        db.close()  # 关闭数据库连接

    def new_row(self):
        if self.CHECK():
            return
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该教师已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '' and self.var_age.get() != 0:
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO teacher_k(tea_id, tea_name, tea_gender, tea_age,tea_dept) \
				       VALUES ('%s', '%s', '%s', '%s','%s')" % \
                      (self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get(),self.var_dept.get())  # SQL 插入语句
                sqls = "INSERT INTO `tea_login_k` VALUES ('%s', '123456')" % (self.var_id.get())
                try:
                    cursor.execute(sql)  # 执行sql语句
                    cursor.execute(sqls)
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())
                self.gender.append(self.var_gender.get())
                self.age.append(self.var_age.get())
                self.dept.append(self.var_dept.get())
                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                    self.age[len(self.id) - 1],self.dept[len(self.id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写教师数据')

    def updata_row(self):
        if self.CHECK():
            return
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填工号 与 所选工号一致
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql_update = f"UPDATE teacher_k SET tea_name = '{self.var_name.get()}', tea_gender = '{self.var_gender.get()}', tea_age = {self.var_age.get()}, tea_dept = '{self.var_dept.get()}' WHERE tea_id = '{self.var_id.get()}'"  # SQL 插入语句
                try:
                    cursor.execute(sql_update)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接

                id_index = self.id.index(self.row_info[0])

                self.name[id_index] = self.var_name.get()
                self.gender[id_index] = self.var_gender.get()
                self.age[id_index] = self.var_age.get()
                self.dept[id_index] = self.var_dept.get()
                self.tree.item(self.tree.selection()[id_index], values=(
                    self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                    self.var_age.get(),self.var_dept.get()))  # 修改对于行信息
            else:
                messagebox.showinfo('警告！', '不能修改教师工号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的工号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_delete = "DELETE FROM teacher_k WHERE tea_id = '%s'" % (self.row_info[0])  # SQL 插入语句
            sql_deletes = "DELETE  FROM tea_login_k WHERE tea_id = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql_delete)  # 执行sql语句
                cursor.execute(sql_deletes)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.name[id_index]
            del self.age[id_index]
            del self.gender[id_index]
            del self.dept[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())
# 管理员学生信息界面
class student_manage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('管理员操作界面')

        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=250)
        self.frame_center = tk.Frame(width=500, height=200)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "性别", "年龄","专业")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("年龄", width=100, anchor='center')
        self.tree.column("专业", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.dept = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student_k"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                self.dept.append(row[4])
            # print(self.id)
            # print(self.name)
            # print(self.gender)
            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age),len(self.dept))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i],self.dept[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="学生信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明学号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = IntVar()  # 声明年龄
        self.var_dept = StringVar()  # 声明专业
        # 学号
        self.right_top_id_label = Label(self.frame_left_top, text="学号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 性别
        self.right_top_gender_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender,
                                            font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 年龄
        self.right_top_age_label = Label(self.frame_left_top, text="年龄：", font=('Verdana', 15))
        self.right_top_age_entry = Entry(self.frame_left_top, textvariable=self.var_age,
                                            font=('Verdana', 15))
        self.right_top_age_label.grid(row=4, column=0)  # 位置设置
        self.right_top_age_entry.grid(row=4, column=1)

        # 专业
        self.right_top_dept_label = Label(self.frame_left_top, text="专业：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_dept,
                                            font=('Verdana', 15))
        self.right_top_dept_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建学生信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中学生信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中学生信息', width=20,
                                            command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='(学号)查询学生信息', width=20,command=self.find)
        self.right_top_button5 = ttk.Button(self.frame_bottom, text='退出学生信息管理系统', width=20,command=self.back)
        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=4, column=0, padx=20, pady=10)
        self.right_top_button5.grid(row=5, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=1, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击


    def back(self):
        Admin_manage(self.window)  # 显示主窗口 销毁本窗口

    def CHECK(self):
        if len(self.var_id.get()) != id_len or (self.var_age.get() < 0 or self.var_age.get() > 100) or \
                (self.var_gender.get() not in gender) or (self.var_dept.get() not in dept):
            messagebox.showinfo('错误！', '请注意信息更新规范！如学号、性别、年龄、专业')
            return 1
        else:
            return 0
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.var_dept.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def find(self):
        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass) # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student_k WHERE id = '%s'" % (self.right_top_id_entry.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                stu_id = row[0]
                stu_name = row[1]
                stu_gender = row[2]
                stu_age = row[3]
                stu_dept = row[4]
                # 打印结果
                print("id=%s,name=%s,gender=%s,age=%s,dept=%s" % (stu_id, stu_name,stu_gender,stu_age,stu_dept))
                self.var_id.set(stu_id)
                self.var_name.set(stu_name)
                self.var_gender.set(stu_gender)
                self.var_age.set(stu_age)
                self.var_dept.set(stu_dept)
        except:
            print("Error: 未找到该同学")
            messagebox.showinfo('异常！', '未找到该同学！')
        db.close()  # 关闭数据库连接

    def new_row(self):
        if self.CHECK():
            return
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该学生已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '' and self.var_age.get() != 0:
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO student_k(id, name, gender, age,dept) \
				       VALUES ('%s', '%s', '%s', '%s','%s')" % \
                      (self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get(),self.var_dept.get())  # SQL 插入语句
                sqls = "INSERT INTO `stu_login_k` VALUES ('%s', '123456')" % (self.var_id.get())
                try:
                    cursor.execute(sql)  # 执行sql语句
                    cursor.execute(sqls)
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())
                self.gender.append(self.var_gender.get())
                self.age.append(self.var_age.get())
                self.dept.append(self.var_dept.get())
                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                    self.age[len(self.id) - 1],self.dept[len(self.id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写学生数据')

    def updata_row(self):
        if self.CHECK():
            return
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql_update = f"UPDATE student_k SET name = '{self.var_name.get()}', gender = '{self.var_gender.get()}', age = {self.var_age.get()}, dept = '{self.var_dept.get()}' WHERE id = '{self.var_id.get()}'"  # SQL 插入语句
                try:
                    cursor.execute(sql_update)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接

                id_index = self.id.index(self.row_info[0])
                self.name[id_index] = self.var_name.get()
                self.gender[id_index] = self.var_gender.get()
                self.age[id_index] = self.var_age.get()
                self.dept[id_index] = self.var_dept.get()
                self.tree.item(self.tree.selection()[0], values=(
                    self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                    self.var_age.get(),self.var_dept.get()))  # 修改对于行信息
            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_delete = "DELETE FROM student_k WHERE id = '%s'" % (self.row_info[0])  # SQL 插入语句
            sql_deletes = "DELETE  FROM stu_login_k WHERE stu_id = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql_delete)  # 执行sql语句
                cursor.execute(sql_deletes)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.dept[id_index]
            del self.name[id_index]
            del self.gender[id_index]
            del self.age[id_index]
            del self.id[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())
# 管理员登陆页面
class Admin_login:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员登陆页面')
        self.window.geometry('300x450')

        label = tk.Label(self.window, text='管理员登陆', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='管理员账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()

        Label(self.window, text='管理员密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.admin_username.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass) # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM admin_login_k WHERE admin_id = '%s'" % (self.admin_username.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
                # 打印结果
                print("admin_id=%s,admin_pass=%s" % (admin_id, admin_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆管理员管理界面")
        print("self", self.admin_pass)
        print("local", admin_pass)

        if self.admin_pass.get() == admin_pass:
            Admin_manage(self.window)  # 进入管理员操作界面
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

#------------------------------------学生模块------------------------------------------


# 学生操作界面
class Student_manage:
    def __init__(self, parent_window,stu_id):
        parent_window.destroy()  # 销毁子界面

        self.stu_id = stu_id
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生操作系统')
        self.window.geometry('300x470')

        label = Label(self.window, text="学生操作系统", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="学生个人信息管理系统", font=tkFont.Font(size=16), command=lambda: Stu_student_manage(self.window,self.stu_id), width=30,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="选课系统", font=tkFont.Font(size=16), command=lambda: Stu_course_manage(self.window,self.stu_id), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="个人成绩查询系统", font=tkFont.Font(size=16),
               command=lambda: Stu_s_course_manage(self.window, self.stu_id), width=30,
               height=2, fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

        Button(self.window, text='退出系统', height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        self.window.mainloop()  # 主消息循环
# 学生个人成绩查询界面
class Stu_s_course_manage:
    def __init__(self, parent_window,stu_id):
        parent_window.destroy()  # 销毁主界面

        self.stu_id = stu_id
        self.window = Tk()  # 初始框的声明
        self.window.title('学生操作界面')

        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=250)
        self.frame_center = tk.Frame(width=500, height=200)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "学生姓名", "课程号", "课程名", "成绩")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("学生姓名", width=100, anchor='center')
        self.tree.column("课程号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("课程名", width=100, anchor='center')
        self.tree.column("成绩", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.SNO = []
        self.NAME = []
        self.CNO = []
        self.CNAME = []
        self.grade = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT s.SNO, sk.name, s.CNO, c.CNAME, s.GRADE   \
                    FROM s_course s \
                    JOIN student_k sk ON s.SNO = sk.id  \
                    JOIN course c ON s.CNO = c.CNO WHERE s.SNO = '%s'"%(self.stu_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.SNO.append(row[0])
                self.NAME.append(row[1])
                self.CNO.append(row[2])
                self.CNAME.append(row[3])
                self.grade.append(row[4])

            # print(self.CNO)
            # print(self.CNAME)
            # print(self.gender)
            # print(self.CCREDIR)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.CNO), len(self.CNAME))):  # 写入数据
            self.tree.insert('', i, values=(self.SNO[i], self.NAME[i], self.CNO[i], self.CNAME[i], self.grade[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="课程信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_sno = StringVar()  # 声明工号
        self.var_name = StringVar()  # 声明姓名
        self.var_cno = IntVar()  # 声明年龄
        self.var_cname = StringVar()  # 声明专业
        self.var_grade = IntVar()
        # 课程号
        self.right_top_id_label = Label(self.frame_left_top, text="学号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_sno, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 课程名
        self.right_top_name_label = Label(self.frame_left_top, text="学生姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 学分
        self.right_top_age_label = Label(self.frame_left_top, text="课程号：", font=('Verdana', 15))
        self.right_top_age_entry = Entry(self.frame_left_top, textvariable=self.var_cno,
                                         font=('Verdana', 15))
        self.right_top_age_label.grid(row=3, column=0)  # 位置设置
        self.right_top_age_entry.grid(row=3, column=1)
        # 授课老师
        self.right_top_dept1_label = Label(self.frame_left_top, text="课程名：", font=('Verdana', 15))
        self.right_top_dept1_entry = Entry(self.frame_left_top, textvariable=self.var_cname,
                                          font=('Verdana', 15))
        self.right_top_dept1_label.grid(row=4, column=0)  # 位置设置
        self.right_top_dept1_entry.grid(row=4, column=1)

        self.right_top_dept_label = Label(self.frame_left_top, text="成绩：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_grade,
                                          font=('Verdana', 15))
        self.right_top_dept_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=5, column=1)
        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='(课程号)查询选课信息', width=20,
                                            command=self.find)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='(课程名)查询选课信息', width=20,
                                            command=self.find1)
        self.right_top_button5 = ttk.Button(self.frame_bottom, text='退出个人成绩查询管理系统', width=20, command=self.back)
        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button3.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button5.grid(row=3, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=1, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def back(self):
        Student_manage(self.window,self.stu_id)  # 显示主窗口 销毁本窗口


    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_sno.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_cno.set(self.row_info[2])
        self.var_cname.set(self.row_info[3])
        self.var_grade.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_sno,
                                        font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def find(self):
        # 数据库操作 查询管理员表
        row = None
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT s.SNO, sk.name, s.CNO, c.CNAME, s.GRADE   \
                            FROM s_course s \
                            JOIN student_k sk ON s.SNO = sk.id  \
                            JOIN course c ON s.CNO = c.CNO  WHERE s.SNO = '%s' and s.CNO = '%s'" % (
            self.stu_id, self.right_top_age_entry.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            if len(results)==0:
                messagebox.showinfo('异常！', '未找到该选课！')
            for row in results:
                # 打印结果
                # print("cno=%s,cname=%s,credit=%s,teacher=%s" % (cno, cname,ccredit,cteacher))
                self.var_sno.set(row[0])
                self.var_name.set(row[1])
                self.var_cno.set(row[2])
                self.var_cname.set(row[3])
                self.var_grade.set(row[4])
                db.close()  # 关闭数据库连接
                messagebox.showinfo('提示！', '查询成功！')
                return row
        except:
            print("Error: 未找到该选课信息")
            messagebox.showinfo('异常！', '未找到该选课！')
        return None

    def find1(self):
        # 数据库操作 查询管理员表
        row = None
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT s.SNO, sk.name, s.CNO, c.CNAME, s.GRADE   \
                            FROM s_course s \
                            JOIN student_k sk ON s.SNO = sk.id  \
                            JOIN course c ON s.CNO = c.CNO  WHERE s.SNO = '%s' and c.CNAME = '%s'" % (
            self.stu_id, self.right_top_dept1_entry.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            if len(results)==0:
                messagebox.showinfo('异常！', '未找到该选课！')
            for row in results:
                # 打印结果
                # print("cno=%s,cname=%s,credit=%s,teacher=%s" % (cno, cname,ccredit,cteacher))
                self.var_sno.set(row[0])
                self.var_name.set(row[1])
                self.var_cno.set(row[2])
                self.var_cname.set(row[3])
                self.var_grade.set(row[4])
                db.close()  # 关闭数据库连接
                messagebox.showinfo('提示！', '查询成功！')
                return row
        except:
            print("Error: 未找到该选课信息")
            messagebox.showinfo('异常！', '未找到该选课！')
        return None
# 学生选课界面
class Stu_course_manage:
    def __init__(self, parent_window,stu_id):

        parent_window.destroy()  # 销毁主界面

        self.stu_id = stu_id
        self.window = Tk()  # 初始框的声明
        self.window.title('学生操作界面')

        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=250)
        self.frame_center1 = tk.Frame(width=500,height=200)
        self.frame_center = tk.Frame(width=500, height=200)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义上方中心列表区域  1
        self.center1_title = Label(self.frame_center1, text="已选课程信息:", font=('Verdana', 20))
        self.center1_title.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.columns1 = ("学号", "学生姓名", "课程号", "课程名","学分", "授课教师")
        self.tree1 = ttk.Treeview(self.frame_center1, show="headings", height=18, columns=self.columns1)
        self.vbar1 = ttk.Scrollbar(self.frame_center1, orient=VERTICAL, command=self.tree1.yview)
        # 定义树形结构与滚动条
        self.tree1.configure(yscrollcommand=self.vbar1.set)

        # 表格的标题
        self.tree1.column("学号", width=100, anchor='center')  # 表示列,不显示
        self.tree1.column("学生姓名", width=100, anchor='center')
        self.tree1.column("课程号", width=50, anchor='center')  # 表示列,不显示
        self.tree1.column("课程名", width=100, anchor='center')
        self.tree1.column("学分", width=50, anchor='center')
        self.tree1.column("授课教师", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree1.grid(row=0, column=0, sticky=NSEW)
        self.vbar1.grid(row=0, column=1, sticky=NS)

        self.SNO1 = []
        self.NAME1 = []
        self.CNO1 = []
        self.CNAME1 = []
        self.CS1 = []
        self.grade1 = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT s.SNO, sk.name, s.CNO, c.CNAME, c.CCREDIT,t.tea_name   \
                           FROM s_course s \
                           JOIN student_k sk ON s.SNO = sk.id  \
                           JOIN course c ON s.CNO = c.CNO \
                           JOIN teacher_k t ON c.CTEACHER = t.tea_id\
                           WHERE s.SNO = '%s'" % (self.stu_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.SNO1.append(row[0])
                self.NAME1.append(row[1])
                self.CNO1.append(row[2])
                self.CNAME1.append(row[3])
                self.CS1.append(row[4])
                self.grade1.append(row[5])

            # print(self.CNO)
            # print(self.CNAME)
            # print(self.gender)
            # print(self.CCREDIR)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.CNO1), len(self.CNAME1))):  # 写入数据
            self.tree1.insert('', i, values=(self.SNO1[i], self.NAME1[i], self.CNO1[i], self.CNAME1[i], self.CS1[i],self.grade1[i]))

        for col in self.columns1:  # 绑定函数，使表头可排序
            self.tree1.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree1, _col, False))

        # 定义下方中心列表区域
        self.center_title = Label(self.frame_center, text="所有课程信息:", font=('Verdana', 20))
        self.center_title.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)
        self.columns = ("课程号", "课程名", "学分","授课老师工号","授课老师")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("课程号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("课程名", width=100, anchor='center')
        self.tree.column("学分", width=100, anchor='center')
        self.tree.column("授课老师工号", width=100, anchor='center')
        self.tree.column("授课老师", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.CNO = []
        self.CNAME = []
        self.CCREDIR = []
        self.CTEACHER = []
        self.CTNAME = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        #sql = "SELECT * FROM course"  # SQL 查询语句
        sql ="SELECT course.*, teacher_k.tea_name \
            FROM course \
            JOIN teacher_k ON course.CTEACHER = teacher_k.tea_id"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.CNO.append(row[0])
                self.CNAME.append(row[1])
                self.CCREDIR.append(row[2])
                self.CTEACHER.append(row[3])
                self.CTNAME.append(row[4])
            # print(self.CNO)
            # print(self.CNAME)
            # print(self.gender)
            # print(self.CCREDIR)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.CNO), len(self.CNAME), len(self.CCREDIR),len(self.CTEACHER))):  # 写入数据
            self.tree.insert('', i, values=(self.CNO[i], self.CNAME[i], self.CCREDIR[i],self.CTEACHER[i],self.CTNAME[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="课程信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_cno = StringVar()  # 声明工号
        self.var_cname = StringVar()  # 声明姓名
        self.var_ccredit = IntVar()  # 声明年龄
        self.var_cteacher = StringVar()  # 声明专业
        self.var_ctname = StringVar()  # 声明
        # 课程号
        self.right_top_id_label = Label(self.frame_left_top, text="课程号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_cno, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 课程名
        self.right_top_name_label = Label(self.frame_left_top, text="课程名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_cname, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 学分
        self.right_top_age_label = Label(self.frame_left_top, text="学分：", font=('Verdana', 15))
        self.right_top_age_entry = Entry(self.frame_left_top, textvariable=self.var_ccredit,
                                            font=('Verdana', 15))
        self.right_top_age_label.grid(row=3, column=0)  # 位置设置
        self.right_top_age_entry.grid(row=3, column=1)
        # 授课老师工号
        self.right_top_dept_label = Label(self.frame_left_top, text="授课老师工号：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_cteacher,
                                            font=('Verdana', 15))
        self.right_top_dept_label.grid(row=4, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=4, column=1)

        self.right_top_dept1_label = Label(self.frame_left_top, text="授课老师：", font=('Verdana', 15))
        self.right_top_dept1_entry = Entry(self.frame_left_top, textvariable=self.var_ctname,
                                            font=('Verdana', 15))
        self.right_top_dept1_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dept1_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.tree1.bind('<Button-1>', self.click1)
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='选课', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='退课', width=20,
                                            command=self.del_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='(授课教师)查询课程', width=20,command=self.find_all)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='(课程名)查询课程', width=20,
                                            command=self.find_all_byc)
        self.right_top_button5 = ttk.Button(self.frame_bottom, text='退出选信息管理系统', width=20,command=self.back)
        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=4, column=0, padx=20, pady=10)
        self.right_top_button5.grid(row=4, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center1.grid(row=1, column=0, columnspan=2, padx=1, pady=5)
        self.frame_center.grid(row=2, column=0, columnspan=2, padx=1, pady=5)
        self.frame_bottom.grid(row=3, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center1.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center1.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击


    def back(self):
        Student_manage(self.window,self.stu_id)  # 显示主窗口 销毁本窗口

    def CHECK(self):
        if self.var_ccredit.get() < 0 or self.var_ccredit.get() > 10:
            messagebox.showinfo('错误！', '请注意信息更新规范！如学分')
            return 1
        else:
            return 0
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        print(self.row_info)
        self.var_cno.set(self.row_info[0])
        self.var_cname.set(self.row_info[1])
        self.var_ccredit.set(self.row_info[2])
        self.var_cteacher.set(self.row_info[3])
        self.var_ctname.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_cno,
                                        font=('Verdana', 15))

    def click1(self,event):
        self.col1 = self.tree1.identify_column(event.x)  # 列
        self.row1 = self.tree1.identify_row(event.y)  # 行
        self.row_info1 = self.tree1.item(self.row1, "values")
        print(self.row_info1)


    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def find_have(self):
        # 数据库操作 查询管理员表
        row = None
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT s.SNO, sk.name, s.CNO, c.CNAME, s.GRADE   \
                        FROM s_course s \
                        JOIN student_k sk ON s.SNO = sk.id  \
                        JOIN course c ON s.CNO = c.CNO  WHERE s.SNO = '%s' and s.CNO = '%s'" % (
        self.stu_id, self.right_top_id_entry.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                db.close()  # 关闭数据库连接
                return row
        except:
            print("Error: 未找到该选课信息")
            messagebox.showinfo('异常！', '未找到该选课！')
        return None

    def find_all(self):
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        # sql = "SELECT * FROM course"  # SQL 查询语句
        if len(self.var_ctname.get()):
            sql = "SELECT course.*, teacher_k.tea_name \
                       FROM course \
                       JOIN teacher_k ON course.CTEACHER = teacher_k.tea_id\
                       WHERE teacher_k.tea_name = '%s'"%(self.var_ctname.get())
        else:
            sql = "SELECT course.*, teacher_k.tea_name \
                       FROM course \
                       JOIN teacher_k ON course.CTEACHER = teacher_k.tea_id"
        CNO = []
        CNAME = []
        CCREDIR = []
        CTEACHER = []
        CTNAME = []
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
                CNO.append(row[0])
                CNAME.append(row[1])
                CCREDIR.append(row[2])
                CTEACHER.append(row[3])
                CTNAME.append(row[4])
            # print(self.CNO)
            # print(self.CNAME)
            # print(self.gender)
            # print(self.CCREDIR)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        # 清除所有数据
        self.tree.delete(*self.tree.get_children())
        self.tree.update() #强制更新

        for i in range(min(len(CNO), len(CNAME), len(CCREDIR), len(CTEACHER))):  # 写入数据
            self.tree.insert('', i,
                             values=(CNO[i], CNAME[i], CCREDIR[i], CTEACHER[i], CTNAME[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

    def find_all_byc(self):
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        # sql = "SELECT * FROM course"  # SQL 查询语句
        if len(self.var_cname.get()):
            sql = "SELECT course.*, teacher_k.tea_name \
                       FROM course \
                       JOIN teacher_k ON course.CTEACHER = teacher_k.tea_id\
                       WHERE course.CNAME = '%s'" % (self.var_cname.get())
        else:
            sql = "SELECT course.*, teacher_k.tea_name \
                       FROM course \
                       JOIN teacher_k ON course.CTEACHER = teacher_k.tea_id"
        CNO = []
        CNAME = []
        CCREDIR = []
        CTEACHER = []
        CTNAME = []
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                print(row)
                CNO.append(row[0])
                CNAME.append(row[1])
                CCREDIR.append(row[2])
                CTEACHER.append(row[3])
                CTNAME.append(row[4])
            # print(self.CNO)
            # print(self.CNAME)
            # print(self.gender)
            # print(self.CCREDIR)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        # 清除所有数据
        self.tree.delete(*self.tree.get_children())
        self.tree.update()  # 强制更新

        for i in range(min(len(CNO), len(CNAME), len(CCREDIR), len(CTEACHER))):  # 写入数据
            self.tree.insert('', i,
                             values=(CNO[i], CNAME[i], CCREDIR[i], CTEACHER[i], CTNAME[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

    def new_row(self):
        if self.CHECK():
            return
        print(self.var_cno.get())
        print(self.CNO)
        row = self.find_have()
        row1 = None
        if row is not None:
            messagebox.showinfo('警告！', '该课程已存在！')
        else:
            if self.var_cno.get() != '' and self.var_cname.get() != '':
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO s_course(SNO, CNO) \
        				       VALUES ('%s', '%s')" % \
                      (self.stu_id, self.var_cno.get())  # SQL 插入语句

                sql_show = "SELECT s.SNO, sk.name, s.CNO, c.CNAME, c.CCREDIT,t.tea_name   \
                                           FROM s_course s \
                                           JOIN student_k sk ON s.SNO = sk.id  \
                                           JOIN course c ON s.CNO = c.CNO \
                                           JOIN teacher_k t ON c.CTEACHER = t.tea_id\
                                           WHERE s.SNO = '%s'" % (self.stu_id)  # SQL 查询语句

                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行

                    # 执行SQL语句
                    cursor.execute(sql_show)
                    # 获取所有记录列表
                    results = cursor.fetchall()
                    for row in results:
                        # 打印结果
                        # print("cno=%s,cname=%s,credit=%s,teacher=%s" % (cno, cname,ccredit,cteacher))
                        self.SNO1.append(row[0])
                        self.NAME1.append(row[1])
                        self.CNO1.append(row[2])
                        self.CNAME1.append(row[3])
                        self.CS1.append(row[4])
                        self.grade1.append(row[5])
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                id_index = self.CNO1.index(self.var_cno.get())
                self.tree1.insert('', len(self.CNO1)-1, values=(
                    self.SNO1[id_index], self.NAME1[id_index],
                    self.CNO1[id_index], self.CNAME1[id_index],
                    self.CS1[id_index],self.grade1[id_index]))
                self.tree1.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写课程数据')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_delete = "DELETE FROM s_course WHERE SNO = '%s' and CNO = '%s'" % (self.stu_id, self.row_info1[2])  # SQL 插入语句
            print(self.stu_id, self.row_info1[2])
            try:
                cursor.execute(sql_delete)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.CNO1.index(self.row_info1[2])
            print(id_index)
            del self.SNO1[id_index]
            del self.NAME1[id_index]
            del self.CNO1[id_index]
            del self.CNAME1[id_index]
            del self.CS1[id_index]
            del self.grade1[id_index]
            self.tree1.delete(self.tree1.selection()[0])  # 删除所选行
# 学生教师信息界面（000）
class Stu_teacher_manage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('管理员操作界面')

        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=250)
        self.frame_center = tk.Frame(width=500, height=200)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("工号", "姓名", "性别", "年龄","专业")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("工号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("年龄", width=100, anchor='center')
        self.tree.column("专业", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.dept = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM teacher_k"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                self.dept.append(row[4])
            # print(self.id)
            # print(self.name)
            # print(self.gender)
            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age),len(self.dept))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i],self.dept[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="教师信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明工号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = IntVar()  # 声明年龄
        self.var_dept = StringVar()  # 声明专业
        # 工号
        self.right_top_id_label = Label(self.frame_left_top, text="工号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 性别
        self.right_top_gender_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender,
                                            font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 年龄
        self.right_top_age_label = Label(self.frame_left_top, text="年龄：", font=('Verdana', 15))
        self.right_top_age_entry = Entry(self.frame_left_top, textvariable=self.var_age,
                                            font=('Verdana', 15))
        self.right_top_age_label.grid(row=4, column=0)  # 位置设置
        self.right_top_age_entry.grid(row=4, column=1)

        # 专业
        self.right_top_dept_label = Label(self.frame_left_top, text="专业：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_dept,
                                            font=('Verdana', 15))
        self.right_top_dept_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建教师信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中教师信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中教师信息', width=20,
                                            command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='(工号)查询教师信息', width=20,command=self.find)
        self.right_top_button5 = ttk.Button(self.frame_bottom, text='退出教师信息管理系统', width=20,command=self.back)
        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=4, column=0, padx=20, pady=10)
        self.right_top_button5.grid(row=5, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=1, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击


    def back(self):
        Admin_manage(self.window)  # 显示主窗口 销毁本窗口

    def CHECK(self):
        if len(self.var_id.get()) != 5 or (self.var_age.get() < 0 or self.var_age.get() > 100) or \
                (self.var_gender.get() not in gender) or (self.var_dept.get() not in dept):
            messagebox.showinfo('错误！', '请注意信息更新规范！如工号、性别、年龄、专业')
            return 1
        else:
            return 0
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.var_dept.set(self.row_info[4])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    def find(self):
        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass) # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM course WHERE tea_id = '%s'" % (self.right_top_id_entry.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                stu_id = row[0]
                stu_name = row[1]
                stu_gender = row[2]
                stu_age = row[3]
                stu_dept = row[4]
                # 打印结果
                print("id=%s,name=%s,gender=%s,age=%s,dept=%s" % (stu_id, stu_name,stu_gender,stu_age,stu_dept))
                self.var_id.set(stu_id)
                self.var_name.set(stu_name)
                self.var_gender.set(stu_gender)
                self.var_age.set(stu_age)
                self.var_dept.set(stu_dept)
        except:
            print("Error: 未找到该同学")
            messagebox.showinfo('异常！', '未找到该同学！')
        db.close()  # 关闭数据库连接

    def new_row(self):
        if self.CHECK():
            return
        print(self.var_id.get())
        print(self.id)
        if str(self.var_id.get()) in self.id:
            messagebox.showinfo('警告！', '该教师已存在！')
        else:
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '' and self.var_age.get() != 0:
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO teacher_k(tea_id, tea_name, tea_gender, tea_age,tea_dept) \
				       VALUES ('%s', '%s', '%s', '%s','%s')" % \
                      (self.var_id.get(), self.var_name.get(), self.var_gender.get(), self.var_age.get(),self.var_dept.get())  # SQL 插入语句
                sqls = "INSERT INTO `tea_login_k` VALUES ('%s', '123456')" % (self.var_id.get())
                try:
                    cursor.execute(sql)  # 执行sql语句
                    cursor.execute(sqls)
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接

                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())
                self.gender.append(self.var_gender.get())
                self.age.append(self.var_age.get())
                self.dept.append(self.var_dept.get())
                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                    self.age[len(self.id) - 1],self.dept[len(self.id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写教师数据')

    def updata_row(self):
        if self.CHECK():
            return
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:  # 如果所填工号 与 所选工号一致
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql_update = f"UPDATE teacher_k SET tea_name = '{self.var_name.get()}', tea_gender = '{self.var_gender.get()}', tea_age = {self.var_age.get()}, tea_dept = '{self.var_dept.get()}' WHERE tea_id = '{self.var_id.get()}'"  # SQL 插入语句
                try:
                    cursor.execute(sql_update)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接

                id_index = self.id.index(self.row_info[0])

                self.name[id_index] = self.var_name.get()
                self.gender[id_index] = self.var_gender.get()
                self.age[id_index] = self.var_age.get()
                self.dept[id_index] = self.var_dept.get()
                self.tree.item(self.tree.selection()[id_index], values=(
                    self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                    self.var_age.get(),self.var_dept.get()))  # 修改对于行信息
            else:
                messagebox.showinfo('警告！', '不能修改教师工号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的工号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_delete = "DELETE FROM teacher_k WHERE tea_id = '%s'" % (self.row_info[0])  # SQL 插入语句
            sql_deletes = "DELETE  FROM tea_login_k WHERE tea_id = '%s'" % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql_delete)  # 执行sql语句
                cursor.execute(sql_deletes)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.name[id_index]
            del self.age[id_index]
            del self.gender[id_index]
            del self.dept[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())
# 学生个人信息管理界面
class Stu_student_manage:
    def __init__(self, parent_window,stu_id):
        parent_window.destroy()  # 销毁主界面

        self.stu_id = stu_id
        self.window = Tk()  # 初始框的声明
        self.window.title('学生操作界面')

        self.frame_left_top = tk.Frame(width=300, height=250)
        self.frame_right_top = tk.Frame(width=200, height=250)
        self.frame_center = tk.Frame(width=500, height=200)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "性别", "年龄","专业")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=100, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("年龄", width=100, anchor='center')
        self.tree.column("专业", width=100, anchor='center')
        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.dept = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student_k WHERE id = '%s'" % (self.stu_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                self.dept.append(row[4])
            # print(self.id)
            # print(self.name)
            # print(self.gender)
            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age),len(self.dept))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i],self.dept[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="学生信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_name = StringVar()  # 声明姓名
        self.var_age = IntVar()  # 声明年龄
        self.var_pass = StringVar()  # 声明密码
        self.var_name.set(self.name[0])
        self.var_age.set(self.age[0])
        # 姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 年龄
        self.right_top_age_label = Label(self.frame_left_top, text="年龄：", font=('Verdana', 15))
        self.right_top_age_entry = Entry(self.frame_left_top, textvariable=self.var_age,
                                            font=('Verdana', 15))
        self.right_top_age_label.grid(row=4, column=0)  # 位置设置
        self.right_top_age_entry.grid(row=4, column=1)

        # 密码
        self.right_top_dept_label = Label(self.frame_left_top, text="密码：", font=('Verdana', 15))
        self.right_top_dept_entry = Entry(self.frame_left_top, textvariable=self.var_pass,
                                            font=('Verdana', 15))
        self.right_top_dept_label.grid(row=5, column=0)  # 位置设置
        self.right_top_dept_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新个人信息', width=20,
                                            command=self.updata_row)
        self.right_top_button5 = ttk.Button(self.frame_bottom, text='退出个人信息管理系统', width=20,command=self.back)
        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=20)
        self.right_top_button5.grid(row=3, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=1, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击


    def back(self):
        Student_manage(self.window,self.stu_id)  # 显示主窗口 销毁本窗口

    def CHECK(self):
        if (self.var_age.get() < 0 or self.var_age.get() > 100) :
            messagebox.showinfo('错误！', '请注意信息更新规范！年龄')
            return 1
        else:
            return 0
    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_name.set(self.row_info[1])
        self.var_age.set(int(self.row_info[3]))
        print('')
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def updata_row(self):
        if self.CHECK():
            return
        res = messagebox.askyesnocancel('警告！', '密码将会更新，是否更新所填数据？')
        if res == True:
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_update = f"UPDATE student_k SET name = '{self.var_name.get()}', age = {self.var_age.get()} WHERE id = '{self.stu_id}'"  # SQL 插入语句
            sql_update1 = f"UPDATE stu_login_k SET stu_pass = '{self.var_pass.get()}'WHERE stu_id = '{self.stu_id}'"
            try:
                cursor.execute(sql_update)  # 执行sql语句
                cursor.execute(sql_update1)
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = 0
            self.name[id_index] = self.var_name.get()
            self.age[id_index] = self.var_age.get()
            self.tree.item('I001', values=(
                self.stu_id, self.var_name.get(), self.gender[0],
                self.var_age.get(), self.dept[0])) # 修改对于行信息
# 学生登陆页面
class Student_login:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生登陆页面')
        self.window.geometry('300x450')

        label = tk.Label(self.window, text='学生登陆', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='学生账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()

        Label(self.window, text='学生密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.admin_username.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass) # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM stu_login_k WHERE stu_id = '%s'" % (self.admin_username.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
                # 打印结果
                print("stu_id=%s,stu_pass=%s" % (admin_id, admin_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆学生管理界面")
        print("self", self.admin_pass)
        print("local", admin_pass)

        if self.admin_pass.get() == admin_pass:
            Student_manage(self.window,admin_id)  # 进入学生操作界面
        else:
            print("*"*10)
            print(admin_pass)
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

#------------------------------------教师模块------------------------------------------

class TeaPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教师登陆页面')
        self.window.geometry('300x450')

        label = tk.Label(self.window, text='教师登陆', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='教师账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.tea_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.tea_username.pack()

        Label(self.window, text='教师密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.tea_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.tea_pass.pack()

        Button(self.window, text="登陆", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        print(str(self.tea_username.get()))
        print(str(self.tea_pass.get()))
        tea_pass = None

        # 数据库操作 查询教师表
        db = pymysql.connect(host='localhost', port=3306, db=database, user='root', password=keypass) # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        user_input = self.tea_username.get()
        sql = "SELECT * FROM tea_login_k WHERE tea_id = %s"  # SQL 查询语句
        try:
            # 防止sql注入
            cursor.execute(sql,(user_input,))
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                tea_id = row[0]
                tea_pass = row[1]
                # 打印结果
                print("tea_id=%s,tea_pass=%s" % (tea_id, tea_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆教师管理界面")
        print("self", self.tea_pass)
        print("local", tea_pass)

        if self.tea_pass.get() == tea_pass:
            print("good")
            #TeaManage(self.window,tea_id)  # 进入教师操作界面
            TeaSelect(self.window,tea_id)
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

# 教师选择界面
class  TeaSelect:
    def __init__(self,parent_window,tea_id):
        parent_window.destroy()
        self.tea_id = tea_id
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('教师登陆页面')
        self.window.geometry('300x450')
        # 定义一个按钮叫查询老师教授课程，如果按下进入一个新的页面
        Button(self.window, text="查询教授课程", width=16, font=tkFont.Font(size=20), command=self.function1).pack(pady=20)
        Button(self.window, text="查询课程学生信息", width=16, font=tkFont.Font(size=20), command=self.function2).pack(pady=20)
        Button(self.window, text="录入学生成绩", width=16, font=tkFont.Font(size=20), command=self.function3).pack(pady=20)
        Button(self.window, text="修改个人信息", width=16, font=tkFont.Font(size=20), command=self.function4).pack(pady=20)
        Button(self.window, text="返回上一级", width=16, font=tkFont.Font(size=20), command=self.back).pack(pady=20)
    def function1(self):
        messagebox.showinfo("提示", "查询老师教授课程")
        TeaManage1(self.window,self.tea_id)
    def function2(self):
        messagebox.showinfo("提示", "查询课程学生信息")
        TeaManage2(self.window,self.tea_id)
    def function3(self):
        messagebox.showinfo("提示", "录入学生成绩")
        TeaManage3(self.window,self.tea_id)
    def function4(self):
        messagebox.showinfo("提示", "修改个人信息")
        TeaManage4(self.window,self.tea_id)
    def back(self):
        TeaPage(self.window)

# 教师操作界面1
class TeaManage1:
    def __init__(self, parent_window,tea_id):
        parent_window.destroy()
        self.tea_id = tea_id

        self.CNO= []
        self.CNAME = []
        self.CCREDIT = []
        self.CTEACHER = []
        db = pymysql.connect(host='localhost', port=3306, db=database, user='root', password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标

        sql = "SELECT * FROM course WHERE CTEACHER=(SELECT tea_name FROM teacher_k WHERE tea_id='%s')" % (self.tea_id)  # SQL 查询语句
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            self.CNO.append(row[0])
            self.CNAME.append(row[1])
            self.CCREDIT.append(row[2])
            self.CTEACHER.append(row[3])
        db.close()  # 关闭数据库连接

        #将数据显示在表格中
        self.window = Tk()  # 初始框的声明
        self.window.title('查询课程学生信息')
        self.tree = ttk.Treeview(self.window, columns=("CNO", "CNAME", "CCREDIT", "CTEACHER"), show="headings")
        self.tree.heading("CNO", text="课程号")
        self.tree.heading("CNAME", text="课程名")
        self.tree.heading("CCREDIT", text="学分")
        self.tree.heading("CTEACHER", text="教师")
        self.tree.pack()
        for i in range(len(self.CNO)):
            self.tree.insert("", i, values=(self.CNO[i], self.CNAME[i], self.CCREDIT[i], self.CTEACHER[i]))

        # 点击左上角关闭后，返回上一级
        Button(self.window, text="返回上一级", width=16, font=tkFont.Font(size=20), command=self.back).pack(pady=20)


    def back(self):
        TeaSelect(self.window,self.tea_id)

# 教师操作界面2
class TeaManage2:
    def __init__(self, parent_window,tea_id):
        parent_window.destroy()
        self.tea_id = tea_id

        self.SNO= []
        self.name = []
        self.CNO = []
        self.GRADE = []
        db = pymysql.connect(host='localhost', port=3306, db=database, user='root', password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标

        sql = "SELECT s_course.SNO,student_k.`name`,s_course.CNO,s_course.GRADE  FROM s_course,student_k WHERE CNO in (SELECT CNO FROM course WHERE CTEACHER=(SELECT tea_name FROM teacher_k WHERE tea_id='%s')) AND s_course.SNO=student_k.id" % (self.tea_id)  # SQL 查询语句
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            self.SNO.append(row[0])
            self.name.append(row[1])
            self.CNO.append(row[2])
            self.GRADE.append(row[3])
        db.close()  # 关闭数据库连接

        #将数据显示在表格中
        self.window = Tk()  # 初始框的声明
        self.window.title('查询课程学生信息')
        self.tree = ttk.Treeview(self.window, columns=("SNO", "name", "CNO", "GRADE"), show="headings")
        self.tree.heading("SNO", text="学号")
        self.tree.heading("name", text="姓名")
        self.tree.heading("CNO", text="课程号")
        self.tree.heading("GRADE", text="成绩")
        self.tree.pack()
        for i in range(len(self.CNO)):
            self.tree.insert("", i, values=(self.SNO[i], self.name[i], self.CNO[i], self.GRADE[i]))

        # 点击左上角关闭后，返回上一级
        Button(self.window, text="返回上一级", width=16, font=tkFont.Font(size=20), command=self.back).pack(pady=20)

    def back(self):
        TeaSelect(self.window,self.tea_id)

# 教师操作界面3 录入学生成绩
class TeaManage3:
    def __init__(self, parent_window,tea_id):
        parent_window.destroy()
        self.tea_id = tea_id

        self.SNO= []
        self.name = []
        self.CNO = []
        self.GRADE = []
        db = pymysql.connect(host='localhost', port=3306, db=database, user='root', password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标

        sql = "SELECT s_course.SNO,student_k.`name`,s_course.CNO,s_course.GRADE  FROM s_course,student_k WHERE CNO in (SELECT CNO FROM course WHERE CTEACHER=(SELECT tea_name FROM teacher_k WHERE tea_id='%s')) AND s_course.SNO=student_k.id" % (self.tea_id)  # SQL 查询语句
        cursor.execute(sql)

        results = cursor.fetchall()
        for row in results:
            self.SNO.append(row[0])
            self.name.append(row[1])
            self.CNO.append(row[2])
            self.GRADE.append(row[3])
        db.close()  # 关闭数据库连接

        #将数据显示在表格中
        self.window = Tk()  # 初始框的声明
        self.window.title('查询课程学生信息')

        self.frame_top = tk.Frame(width=500, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 上方框
        self.var_id = StringVar()  # 声明学号
        self.class_num = StringVar()  # 声明课程号
        self.score1 = IntVar()  # 声明分数
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.right_top_id_label = Label(self.frame_top, text="请输入要修改的学生学号", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        self.class_number = Label(self.frame_top, text="请输入课程号", font=('Verdana', 15))
        self.class_number1 = Entry(self.frame_top, textvariable=self.class_num, font=('Verdana', 15))
        self.class_number.grid(row=2, column=0)  # 位置设置
        self.class_number1.grid(row=2, column=1)
        self.score = Label(self.frame_top, text="请输入学生的分数", font=('Verdana', 15))
        self.score_entry = Entry(self.frame_top, textvariable=self.score1, font=('Verdana', 15))
        self.score.grid(row=3, column=0)  # 位置设置
        self.score_entry.grid(row=3, column=1)


        self.bottom=Button(self.frame_top, text="确定", width=16, font=tkFont.Font(size=20), command=self.change_credit)
        self.bottom.grid(row=4, column=1)
        # 下面表格
        self.tree = ttk.Treeview(self.frame_center, columns=("SNO", "name", "CNO", "GRADE"), show="headings")
        self.tree.heading("SNO", text="学号")
        self.tree.heading("name", text="姓名")
        self.tree.heading("CNO", text="课程号")
        self.tree.heading("GRADE", text="成绩")
        self.tree.pack()
        for i in range(len(self.CNO)):
            self.tree.insert("", i, values=(self.SNO[i], self.name[i], self.CNO[i], self.GRADE[i]))

        # 点击左上角关闭后，返回上一级
        Button(self.frame_bottom, text="返回上一级", width=16, font=tkFont.Font(size=20), command=self.back).pack(pady=20)


        # 整体定位
        self.frame_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_center.grid(row=1, column=0, padx=2, pady=5)
        self.frame_bottom.grid(row=2, column=0)

        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单


        self.window.mainloop()

    def change_credit(self):
        print(self.var_id.get())
        print(self.score1.get())
        print(self.class_num.get())
        db = pymysql.connect(host='localhost', port=3306, db=database, user='root', password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标

        sql = "UPDATE s_course SET GRADE='%d' WHERE SNO='%s' AND CNO='%s'" % (self.score1.get(),self.var_id.get(),self.class_num.get())  # SQL 查询语句
        cursor.execute(sql)
        db.commit()
        sql = "SELECT s_course.SNO,student_k.`name`,s_course.CNO,s_course.GRADE  FROM s_course,student_k WHERE CNO in (SELECT CNO FROM course WHERE CTEACHER=(SELECT tea_name FROM teacher_k WHERE tea_id='%s')) AND s_course.SNO=student_k.id" % (
            self.tea_id)  # SQL 查询语句
        cursor.execute(sql)
        results = cursor.fetchall()
        self.SNO = []
        self.name = []
        self.CNO = []
        self.GRADE = []
        for row in results:
            self.SNO.append(row[0])
            self.name.append(row[1])
            self.CNO.append(row[2])
            self.GRADE.append(row[3])
        db.close()  # 关闭数据库连接
        self.tree.delete(*self.tree.get_children())
        for i in range(len(self.CNO)):
            self.tree.insert("", i, values=(self.SNO[i], self.name[i], self.CNO[i], self.GRADE[i]))
    def back(self):
        TeaSelect(self.window,self.tea_id)

# 教师操作界面4
class TeaManage4:
    def __init__(self, parent_window,tea_id):
        parent_window.destroy()
        self.tea_id = tea_id



        db = pymysql.connect(host='localhost', port=3306, db=database, user='root', password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标

        sql = "SELECT * FROM teacher_k,tea_login_k WHERE teacher_k.tea_id=tea_login_k.tea_id AND teacher_k.tea_id='%s'" % (self.tea_id)  # SQL 查询语句

        cursor.execute(sql)

        results = cursor.fetchall()
        for row in results:
            self.tea_id = row[0]
            self.tea_name = row[1]
            self.gender = row[2]
            self.age = row[3]
            self.depthead = row[4]
            self.password = row[6]
        db.close()  # 关闭数据库连接

        #将数据显示在表格中
        self.window = Tk()  # 初始框的声明
        self.window.title('查询课程学生信息')


        # 上方框

        self.tea_name_label = Label(self.window, text="姓名", font=('Verdana', 15))
        self.tea_name_entry = Entry(self.window, textvariable=self.tea_name, font=('Verdana', 15))
        self.tea_name_entry.insert(0, self.tea_name)
        self.tea_name_label.grid(row=1, column=0)  # 位置设置
        self.tea_name_entry.grid(row=1, column=1)

        self.gender_label = Label(self.window, text="性别", font=('Verdana', 15))
        self.gender_entry = Entry(self.window, textvariable=self.gender, font=('Verdana', 15))
        self.gender_entry.insert(0, self.gender)
        self.gender_label.grid(row=2, column=0)  # 位置设置
        self.gender_entry.grid(row=2, column=1)  # 位置设置

        self.age_label = Label(self.window, text="年龄", font=('Verdana', 15))
        self.age_entry = Entry(self.window, textvariable=self.age, font=('Verdana', 15))
        self.age_entry.insert(0, self.age)
        self.age_label.grid(row=3, column=0)  # 位置设置
        self.age_entry.grid(row=3, column=1)  # 位置设置

        self.depthead_label = Label(self.window, text="所属院系", font=('Verdana', 15))
        self.depthead_entry = Entry(self.window, textvariable=self.depthead, font=('Verdana', 15))
        self.depthead_entry.insert(0, self.depthead)
        self.depthead_label.grid(row=4, column=0)  # 位置设置
        self.depthead_entry.grid(row=4, column=1)  # 位置设置

        self.password_label = Label(self.window, text="密码", font=('Verdana', 15))
        self.password_entry = Entry(self.window, textvariable=self.password, font=('Verdana', 15))
        self.password_entry.insert(0, self.password)
        self.password_label.grid(row=5, column=0)  # 位置设置
        self.password_entry.grid(row=5, column=1)  # 位置设置

        self.button1 = Button(self.window, text='修改', font=('Verdana', 15), command=self.update)
        self.button1.grid(row=6, column=0, padx=10, pady=5)

        self.button2 = Button(self.window, text='返回', font=('Verdana', 15), command=self.back)
        self.button2.grid(row=6, column=1, padx=10, pady=5)


        self.window.mainloop()

    def update(self):
        print("ok")
        self.tea_name_changed = self.tea_name_entry.get()
        self.gender = self.gender_entry.get()
        self.age = self.age_entry.get()
        self.depthead = self.depthead_entry.get()
        self.password = self.password_entry.get()

        db = pymysql.connect(host='localhost', port=3306, db=database, user='root', password=keypass)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        try:
            # 开始事务
            db.begin()

            sql = "UPDATE teacher_k SET tea_name = '%s',tea_gender = '%s',tea_age = '%s',tea_dept = '%s' WHERE tea_id = '19001'" % (self.tea_name_changed,self.gender,self.age,self.depthead)
            cursor.execute(sql)
            sql = "UPDATE tea_login_k SET tea_pass = '%s' WHERE tea_id = '19001'" % (self.password)
            cursor.execute(sql)
            sql = "UPDATE course SET CTEACHER = '%s' WHERE CTEACHER = '%s' AND CTEACHER NOT IN (SELECT tea_id FROM teacher_k WHERE tea_id = '%s')" %(self.tea_name_changed,self.tea_name,self.tea_name_changed)
            cursor.execute(sql)

            #提交事务
            db.commit()
        except Exception as e:

            # 回滚事务
            db.rollback()
            messagebox.showinfo("提示", "修改失败！")
        finally:
            db.close()  # 关闭数据库连接
            messagebox.showinfo("提示", "修改成功！")

    def back(self):
        TeaSelect(self.window,self.tea_id)


if __name__ == '__main__':
    try:
        # 打开数据库连接 连接测试
        db = pymysql.connect(host='localhost', port=3306, db=database, user=account, password=keypass)
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        print("********数据库连接成功*********")
        # 连接成功后的后续操作可以放在这里

        # 关闭数据库连接
        db.close()

        # 实例化Application
        window = tk.Tk()
        app = StartPage(window)
        window.mainloop()
        #StartPage(window)
    except:
        #messagebox.showinfo('错误！', '连接数据库失败！')
        pass