# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fantasy_Cricket.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from Evaluate_Team import Ui_MainWindow as evaluateTeam
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox, simpledialog



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 505)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(775, 0))
        self.frame.setAutoFillBackground(True)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.l1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.horizontalLayout_5.addWidget(self.l1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.l2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.horizontalLayout_5.addWidget(self.l2)
        self.label_9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.l3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.horizontalLayout_5.addWidget(self.l3)
        self.label_13 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.l4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.horizontalLayout_5.addWidget(self.l4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(5, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.l5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l5.setFont(font)
        self.l5.setObjectName("l5")
        self.horizontalLayout_2.addWidget(self.l5)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.r1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.r1.setFont(font)
        self.r1.setObjectName("r1")
        self.horizontalLayout_6.addWidget(self.r1)
        self.r2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.r2.setFont(font)
        self.r2.setObjectName("r2")
        self.horizontalLayout_6.addWidget(self.r2)
        self.r3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.r3.setFont(font)
        self.r3.setObjectName("r3")
        self.horizontalLayout_6.addWidget(self.r3)
        self.r3_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.r3_2.setFont(font)
        self.r3_2.setObjectName("r3_2")
        self.horizontalLayout_6.addWidget(self.r3_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setObjectName("list1")
        self.verticalLayout_2.addWidget(self.list1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.l6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l6.setFont(font)
        self.l6.setObjectName("l6")
        self.horizontalLayout_3.addWidget(self.l6)
        spacerItem4 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.l7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l7.setFont(font)
        self.l7.setObjectName("l7")
        self.horizontalLayout_7.addWidget(self.l7)
        spacerItem6 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setObjectName("list2")
        self.verticalLayout_3.addWidget(self.list2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.menuManage_Teams.setFont(font)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.actionNEW_team.setFont(font)
        self.actionNEW_team.setObjectName("actionNEW_team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.actionOPEN_Team.setFont(font)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.actionSAVE_Team.setFont(font)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.actionEVALUATE_Team.setFont(font)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.list1.itemDoubleClicked.connect(self.removelist1)

        self.r1.setDisabled(1)
        self.r2.setDisabled(1)
        self.r3.setDisabled(1)
        self.r3_2.setDisabled(1)
        self.r1.clicked.connect(lambda:self.find("BAT"))
        self.r2.clicked.connect(lambda:self.find("BWL"))
        self.r3.clicked.connect(lambda:self.find("AR"))
        self.r3_2.clicked.connect(lambda:self.find("WK"))
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#5e5e5e;\">Your Selections:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.l1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#3e92ff;\">##</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.l2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#3e92ff;\">##</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "All Rounders(AR)"))
        self.l3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#3e92ff;\">##</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.l4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#3e92ff;\">##</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Points Available"))
        self.l5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#3e92ff;\">####</span></p></body></html>"))
        self.r1.setText(_translate("MainWindow", "BAT"))
        self.r2.setText(_translate("MainWindow", "BOW"))
        self.r3.setText(_translate("MainWindow", "AR"))
        self.r3_2.setText(_translate("MainWindow", "WK"))
        self.label_11.setText(_translate("MainWindow", ">"))
        self.label_12.setText(_translate("MainWindow", "Points Used"))
        self.l6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#3e92ff;\">####</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Team Name"))
        self.l7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#3e92ff;\">Displayed Here</span></p></body></html>"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEVALUATE_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))
    global count,players
    count=0
    players=[]
    
    def menufunction(self, action):
        
        txt= (action.text())
        if txt =='NEW Team':
            s = simpledialog.askstring("Input Box" , "Enter Name Of Team")
            

            if(s!=None):
                self.r1.setDisabled(0)
                self.r2.setDisabled(0)
                self.r3.setDisabled(0)
                self.r3_2.setDisabled(0)    
                self.l7.setText(s)
                self.l1.setText("0")
                self.l2.setText("0")
                self.l3.setText("0")
                self.l4.setText("0")
                self.l5.setText("1000")
                self.l6.setText("0")
                self.list1.clear()
                self.list2.clear()
                self.list1.setDisabled(0)
                global count,players
                count=0
                players=[]

                
        if txt =='OPEN Team':
            s = simpledialog.askstring("Input Box" , "Enter Name Of The Team You Want To Open:")
            self.list2.clear()
            import sqlite3
            Fantasy_Cricket = sqlite3.connect('Fantasy_Cricket.db')
            curs_player=Fantasy_Cricket.cursor()
            sql_main="SELECT Name FROM Composition"
            sql1="SELECT * FROM Composition WHERE Name='"+s+"';"
            sql="SELECT Players FROM Teams WHERE Name='"+s+"' AND Matches='Matches1';"
            sql2="SELECT * FROM Teams WHERE Name='"+s+"' AND Matches='Matches1';"
            curs_player=Fantasy_Cricket.cursor()
            curs_player.execute(sql_main)
            record_main=curs_player.fetchall()
            recordmain=[]
            print (record_main)
            for i in record_main:
                str1 = ''.join(i)
                recordmain.append(str1)
            print (recordmain)
            
            if s in recordmain:
                curs_player.execute(sql1)
                record=curs_player.fetchone()
                self.l1.setText(str(record[1]))
                self.l2.setText(str(record[2]))
                self.l3.setText(str(record[3]))
                self.l4.setText(str(record[4]))
                self.l7.setText(s)
                curs_player.execute(sql2)
                record2=curs_player.fetchone()
                self.l6.setText(str(record2[2]))
                self.l5.setText(str(1000-int(record2[2])))
                curs_player.execute(sql)
                records=curs_player.fetchall()
                for i in records:
                    str1 = ''.join(i)
                    print (str1)
                    self.list2.addItem(str1)
                self.r1.setDisabled(1)
                self.r2.setDisabled(1)
                self.r3.setDisabled(1)
                self.r3_2.setDisabled(1)  
                self.list1.setDisabled(1)
            else:
                messagebox.showerror("Note","No such team found!")

                    
                
        if txt =='SAVE Team':
            name=self.l7.text()          
            val = self.l6.text()
            bat=self.l1.text()
            bwl=self.l2.text()
            ar=self.l3.text()
            wk=self.l4.text()
            import sqlite3
            Fantasy_Cricket = sqlite3.connect('Fantasy_Cricket.db')
            curs_player=Fantasy_Cricket.cursor()
            team_list=[]
            sql1="INSERT INTO Composition (Name, Bat, Bwl,AR,WK) VALUES('"+name+"','"+str(bat)+"','"+str(bwl)+"','"+str(ar)+"','"+str(wk)+"');"
            sql_main="SELECT Name FROM Composition"
            curs_player.execute(sql_main)
            record_main=curs_player.fetchall()
            recordmain=[]
            print (record_main)
            for i in record_main:
                str1 = ''.join(i)
                recordmain.append(str1)
            if name not in recordmain: 
                try:
                    curs_player=Fantasy_Cricket.cursor()
                    curs_player.execute(sql1)            
                    Fantasy_Cricket.commit()
                    print("one record added successfully")
                except:
                    Fantasy_Cricket.rollback()
                    print("Error in adding the record")

            curs_player.execute("SELECT Matches FROM Teams WHERE Name='" + name + "'")
            datas = curs_player.fetchall()
            print (datas)
            if len(datas) != 0:
                match = datas[len(datas)-1][0]
                print (match)
                a = match.split(match[len(match)-1])
                print(a)
                b = match.split('Matches')
                print(b)
                b[1] = int(b[1])+1
                matches = a[0]+str(b[1])
                print (matches) 
            else:
                matches = 'Matches1'
            for item in range(self.list2.count()):
                team_list.append(self.list2.item(item).text())
            
            for i in team_list:
                curs_player.execute("SELECT Points FROM Match WHERE Player='" + i + "'")
                sql_points=(curs_player.fetchone())
                print(sql_points[0])
                sql="INSERT INTO Teams (Name, Players, Value,Matches,Points) VALUES('"+name+"','"+i+"','"+str(val)+"','"+matches+"','"+str(sql_points[0])+"');"
                try:
                    curs_player=Fantasy_Cricket.cursor()
                    curs_player.execute(sql)            
                    Fantasy_Cricket.commit()
                    print("one record added successfully")
                except:
                    Fantasy_Cricket.rollback()
                    print("Error in adding the record")
            
        
        if txt=='EVALUATE Team':
            self.evaluate_team = QtWidgets.QMainWindow()
            self.evaluate_screen = evaluateTeam()
            self.evaluate_screen.setupUi(self.evaluate_team)
            self.evaluate_team.show()


    def find(self,ctg):
        self.list1.clear()
        self.ctg=ctg
        import sqlite3
        Fantasy_Cricket = sqlite3.connect('Fantasy_Cricket.db')
        curs_player=Fantasy_Cricket.cursor()
        sql="SELECT Player FROM Stats WHERE ctg='"+self.ctg+"';"
        curs_player=Fantasy_Cricket.cursor()
        curs_player.execute(sql)
        record=curs_player.fetchall()
        for i in record:
            str1 = ''.join(i)
            print (str1)
            self.list1.addItem(str1)
    def removelist1(self, item):
        global count
        if count<11:
            points_Availible=int(self.l5.text())
            points_used=int(self.l6.text())
            import sqlite3
            Fantasy_Cricket = sqlite3.connect('Fantasy_Cricket.db')
            curs_player=Fantasy_Cricket.cursor()
            sql="SELECT * FROM Stats WHERE Player='"+item.text()+"';"
            curs_player=Fantasy_Cricket.cursor()
            curs_player.execute(sql)
            record=curs_player.fetchone()
            self.value=int(record[5])
            if points_Availible-self.value>=0:
                if self.r1.isChecked()==True:
                    self.l5.setText(str(points_Availible-self.value))
                    self.l6.setText(str(points_used+self.value))
                    self.list1.takeItem(self.list1.row(item))
                    self.list2.addItem(item.text())
                    self.l1.setText(str(int(self.l1.text())+1))
                    count=count+1
                    players.append(item.text())
                if self.r2.isChecked()==True:
                    self.l5.setText(str(points_Availible-self.value))
                    self.l6.setText(str(points_used+self.value))
                    self.list1.takeItem(self.list1.row(item))
                    self.list2.addItem(item.text())
                    self.l2.setText(str(int(self.l2.text())+1))
                    count=count+1
                    players.append(item.text())
                if self.r3.isChecked()==True:
                    self.l5.setText(str(points_Availible-self.value))
                    self.l6.setText(str(points_used+self.value))
                    self.list1.takeItem(self.list1.row(item))
                    self.list2.addItem(item.text())
                    self.l3.setText(str(int(self.l3.text())+1))
                    count=count+1
                    players.append(item.text())
                if self.r3_2.isChecked()==True:
                    if int(self.l4.text())<1:
                        self.l5.setText(str(points_Availible-self.value))
                        self.l6.setText(str(points_used+self.value))
                        self.list1.takeItem(self.list1.row(item))
                        self.list2.addItem(item.text())
                        self.l4.setText(str(int(self.l4.text())+1))
                        count=count+1
                        players.append(item.text())
                    else:
                        messagebox.showerror("Warning","You can not select more than one wicket keeper")
            else:
                messagebox.showerror("Warning","You don't have enough points Availible")
        else:
            messagebox.showerror("Warning","You can not select more than 11 players")                





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
