import sys

import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint, choice
from heapq import nlargest

con = sqlite3.connect('dnd_database.db')
cur = con.cursor()

class Ui_ListDesign(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 930)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, -1, 541, 871))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.bonus = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.bonus.setObjectName("bonus")
        self.verticalLayout_2.addWidget(self.bonus)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.speed = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.speed.setObjectName("speed")
        self.verticalLayout_2.addWidget(self.speed)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.passive = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.passive.setObjectName("passive")
        self.verticalLayout_2.addWidget(self.passive)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.race = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.race.setObjectName("race")
        self.verticalLayout_2.addWidget(self.race)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("dndlogo150.png"))
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.background_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.background_name.setObjectName("background_name")
        self.gridLayout.addWidget(self.background_name, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.traits = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.traits.setObjectName("traits")
        self.gridLayout.addWidget(self.traits, 1, 0, 1, 1)
        self.background = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.background.setObjectName("background")
        self.gridLayout.addWidget(self.background, 4, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ch_class = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.ch_class.setObjectName("ch_class")
        self.gridLayout_2.addWidget(self.ch_class, 3, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.skills = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.skills.setObjectName("skills")
        self.verticalLayout.addWidget(self.skills)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.features = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.features.setObjectName("features")
        self.verticalLayout.addWidget(self.features)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.strength = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.strength.setObjectName("strength")
        self.verticalLayout.addWidget(self.strength)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dexterity = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.dexterity.setObjectName("dexterity")
        self.verticalLayout.addWidget(self.dexterity)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.intelligence = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.intelligence.setObjectName("intelligence")
        self.verticalLayout.addWidget(self.intelligence)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.charisma = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.charisma.setObjectName("charisma")
        self.verticalLayout.addWidget(self.charisma)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.wisdom = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.wisdom.setObjectName("wisdom")
        self.verticalLayout.addWidget(self.wisdom)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.constitution = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.constitution.setObjectName("constitution")
        self.verticalLayout.addWidget(self.constitution)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.inventory = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.inventory.setObjectName("inventory")
        self.verticalLayout.addWidget(self.inventory)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 2, 1, 1, 1)
        self.hit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.hit.setObjectName("hit")
        self.gridLayout_5.addWidget(self.hit, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)
        self.dice = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.dice.setObjectName("dice")
        self.gridLayout_5.addWidget(self.dice, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 1, 1, 1)
        self.armorclass = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.armorclass.setObjectName("armorclass")
        self.gridLayout_5.addWidget(self.armorclass, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)
        self.initiative = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.initiative.setObjectName("initiative")
        self.gridLayout_5.addWidget(self.initiative, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loadButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout_2.addWidget(self.loadButton)
        self.saveButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.character_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.character_name.setObjectName("character_name")
        self.horizontalLayout_2.addWidget(self.character_name)
        self.deleteButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.generatebutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.generatebutton.setObjectName("generatebutton")
        self.verticalLayout_5.addWidget(self.generatebutton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtSaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.txtSaveButton.setObjectName("txtSaveButton")
        self.horizontalLayout_3.addWidget(self.txtSaveButton)
        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_3.addWidget(self.backButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лист Персонажа"))
        self.label_20.setText(_translate("MainWindow", "Бонус мастерства"))
        self.label_17.setText(_translate("MainWindow", "Скорость"))
        self.label_18.setText(_translate("MainWindow", "Пассивная внимательность"))
        self.label_21.setText(_translate("MainWindow", "Раса"))
        self.label_19.setText(_translate("MainWindow", "Предыстория"))
        self.label_14.setText(_translate("MainWindow", "Умения/Заклинания"))
        self.label_8.setText(_translate("MainWindow", "Имя"))
        self.label_7.setText(_translate("MainWindow", "Класс"))
        self.label_15.setText(_translate("MainWindow", "Навыки"))
        self.label_16.setText(_translate("MainWindow", "Владения"))
        self.label.setText(_translate("MainWindow", "Сила"))
        self.label_2.setText(_translate("MainWindow", "Ловкость"))
        self.label_3.setText(_translate("MainWindow", "Интеллект"))
        self.label_4.setText(_translate("MainWindow", "Харизма"))
        self.label_5.setText(_translate("MainWindow", "Мудрость"))
        self.label_6.setText(_translate("MainWindow", "Телосложение"))
        self.label_13.setText(_translate("MainWindow", "Снаряжение"))
        self.label_12.setText(_translate("MainWindow", "Инициатива"))
        self.label_10.setText(_translate("MainWindow", "КБ"))
        self.label_11.setText(_translate("MainWindow", "Кости Хитов"))
        self.label_9.setText(_translate("MainWindow", "Хиты"))
        self.loadButton.setText(_translate("MainWindow", "Загрузить"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.character_name.setText(_translate("MainWindow", "Введите имя персонажа"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
        self.generatebutton.setText(_translate("MainWindow", "Сгенерировать персонажа"))
        self.txtSaveButton.setText(_translate("MainWindow", "Сохранить в txt"))
        self.backButton.setText(_translate("MainWindow", "Назад"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 581, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadCharacter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loadCharacter.setObjectName("loadCharacter")
        self.horizontalLayout.addWidget(self.loadCharacter)
        self.createButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.createButton.setObjectName("createButton")
        self.horizontalLayout.addWidget(self.createButton)
        self.character_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.character_name.setObjectName("character_name")
        self.horizontalLayout.addWidget(self.character_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DnD list Designer"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя Персонажа"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Предыстория"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Класс"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Раса"))
        self.loadCharacter.setText(_translate("MainWindow", "Загрузить "))
        self.createButton.setText(_translate("MainWindow", "Создать"))
        self.character_name.setText(_translate("MainWindow", "Введите имя персонажа"))


def randomch():
    num = sum(nlargest(3, [randint(1, 6), randint(1, 6),
                           randint(1, 6), randint(1, 6)]))
    return str(num)


class MyWidget(QMainWindow, Ui_ListDesign):
    def __init__(self, *arg):
        super().__init__()
        self.setupUi(self)
        self.generatebutton.clicked.connect(self.generate)
        self.txtSaveButton.clicked.connect(self.txt_save)
        self.deleteButton.clicked.connect(self.delete_list)
        self.saveButton.clicked.connect(self.save_list)
        self.backButton.clicked.connect(self.back)
        self.loadButton.clicked.connect(self.load_list)
        self.strength.textEdited.connect(self.strength_edit)
        self.dexterity.textEdited.connect(self.dexterity_edit)
        self.intelligence.textEdited.connect(self.intelligence_edit)
        self.charisma.textEdited.connect(self.charisma_edit)
        self.wisdom.textEdited.connect(self.wisdom_edit)
        self.constitution.textEdited.connect(self.constitution_edit)
        self.background.textChanged.connect(self.background_edit)
        self.background_name.textEdited.connect(self.background_name_edit)
        self.features.textChanged.connect(self.features_edit)
        self.skills.textChanged.connect(self.skills_edit)
        self.ch_class.textEdited.connect(self.ch_class_edit)
        self.inventory.textChanged.connect(self.inventory_edit)
        self.traits.textChanged.connect(self.traits_edit)
        self.hit.textEdited.connect(self.hit_edit)
        self.dice.textEdited.connect(self.dice_edit)
        self.initiative.textEdited.connect(self.initiative_edit)
        self.race.textEdited.connect(self.race_edit)
        self.speed.textEdited.connect(self.speed_edit)
        self.passive.textEdited.connect(self.passive_edit)
        self.character_name.textEdited.connect(self.save_name_edit)

        self.st = '-'
        self.load_name = arg
        self.dex = '-'
        self.int = '-'
        self.cha = '-'
        self.wis = '-'
        self.con = '-'
        self.back = ''
        self.back_name = '-'
        self.back_roll = 0
        self.cclass = ''
        self.cclass_roll = 0
        self.ski = ''
        self.feat = ''
        self.tra = ''
        self.bon = ''
        self.inv = ''
        self.cla_ski = ''
        self.hp = ''
        self.hp_dice = ''
        self.ini = ''
        self.ra = ''
        self.race_roll = ''
        self.spe = ''
        self.pas = ''
        self.save_name = 'Введите имя персонажа'

        if self.load_name[1] != '':
            self.save_name = self.load_name[1]
            self.load_list()

    def txt_save(self):
        flag = False

        result = cur.execute("""SELECT title FROM characters""").fetchall()
        for el in result:
            if el[0] == self.save_name:
                print(self.save_name)
                flag = True

        if flag:
            filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if filename:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(f'Имя: {self.save_name} \n')
                    file.write(f'\n')
                    file.write(f'Сила: {self.st} \n')
                    file.write(f'Ловкость: {self.dex} \n')
                    file.write(f'Интеллект: {self.int} \n')
                    file.write(f'Харизма: {self.cha} \n')
                    file.write(f'Мудрость: {self.wis} \n')
                    file.write(f'Телосложение: {self.con} \n')
                    file.write(f'\n')
                    file.write(f'Класс: {self.cclass} \n')
                    file.write(f'Раса: {self.ra} \n')
                    file.write(f'\n')
                    file.write(f'Предыстория: {self.back_name} \n')
                    file.write(f'\n')
                    file.write(f'{self.back} \n')
                    file.write(f'\n')
                    file.write(f'Навыки: {self.ski} \n')
                    file.write(f'Владения: {self.feat} \n')
                    file.write(f'\n')
                    file.write(f'Умения: {self.tra} \n')
                    file.write(f'\n')
                    file.write(f'\n')
                    file.write(f'Бонус мастерства: {self.bon} \n')
                    file.write(f'Хиты: {self.hp} \n')
                    file.write(f'Кость хитов: {self.hp_dice} \n')
                    file.write(f'Инициатива: {self.ini} \n')
                    file.write(f'Скорость: {self.spe} \n')
                    file.write(f'Пассивная внимательность: {self.pas} \n')
                    file.write(f'\n')
                    file.write(f'Снаряжение: {self.inv} \n')
                    file.close()

        else:
            dlg = QMessageBox(self)
            dlg.setText("Персонаж не существует, или его не удалось сохранить.")
            button = dlg.exec()

    def back(self):
        self.close()
        MainWind().show()

    def load_list(self):
        flag = False

        result = cur.execute("""SELECT title FROM characters""").fetchall()
        for el in result:
            if el[0] == self.save_name:
                flag = True
        if flag:
            self.ski = ''
            self.name.setText(self.save_name)
            self.st = cur.execute("""SELECT st FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.dex = cur.execute("""SELECT dex FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.int = cur.execute("""SELECT int FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.cha = cur.execute("""SELECT cha FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.wis = cur.execute("""SELECT wis FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.con = cur.execute("""SELECT con FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]

            self.back = cur.execute("""SELECT back FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.back_name = cur.execute("""SELECT back_name FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.ra = cur.execute("""SELECT ra FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.ski = cur.execute("""SELECT ski FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.cclass = cur.execute("""SELECT cclass FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]

            self.feat = cur.execute("""SELECT feat FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]

            self.tra = cur.execute("""SELECT tra FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]

            self.spe = cur.execute("""SELECT spe FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]

            self.inv = cur.execute("""SELECT inv FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]

            self.hp = cur.execute("""SELECT hp FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.hp_dice = cur.execute("""SELECT hp_dice FROM characters
                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.ini = cur.execute("""SELECT ini FROM characters
                                 WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.pas = cur.execute("""SELECT pas FROM characters
                                         WHERE title = ?""", (self.save_name,)).fetchall()[0][0]
            self.in_ui()

            self.save_name = self.character_name.text()

        else:
            dlg = QMessageBox(self)
            dlg.setText("Персонажа не существует")
            button = dlg.exec()

    def delete_list(self):
        flag = False

        result = cur.execute("""SELECT title FROM characters""").fetchall()

        for el in result:
            if el[0] == self.save_name:
                flag = True
        if flag:

            valid = QMessageBox.question(
                self, 'Подтверждение удаления', "Вы действительно удалить персонажа?",
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                with con:
                    cur.execute('DELETE FROM characters WHERE title = ?', (self.save_name,))
                self.st = '-'
                self.dex = '-'
                self.int = '-'
                self.cha = '-'
                self.wis = '-'
                self.con = '-'
                self.back = ''
                self.back_name = '-'
                self.back_roll = 0
                self.cclass = ''
                self.cclass_roll = 0
                self.ski = ''
                self.feat = ''
                self.tra = ''
                self.bon = ''
                self.inv = ''
                self.cla_ski = ''
                self.hp = ''
                self.hp_dice = ''
                self.ini = ''
                self.ra = ''
                self.race_roll = ''
                self.spe = ''
                self.pas = ''

                self.in_ui()

        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle('Ошибка удаления')
            dlg.setText("Персонажа не существует")
            button = dlg.exec()

    def save_list(self):
        result = cur.execute("""SELECT title FROM characters""").fetchall()
        for el in result:
            if el[0] == self.save_name:
                cur.execute('DELETE FROM characters WHERE title = ?', (self.save_name,))

        with con:
            cur.execute('INSERT INTO characters(st, dex, int, cha, wis, con, back, back_name,'
                        'cclass, ski, feat, tra, bon, inv, hp,'
                        'hp_dice, ini, ra, spe, pas, title)'
                        ' VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
                        , (self.st, self.dex,
                            self.int, self.cha, self.wis,
                            self.con, self.back, self.back_name,
                            self.cclass, self.ski, self.feat,
                            self.tra, self.bon, self.inv,
                            self.hp, self.hp_dice, self.ini, self.ra,
                            self.spe, self.pas, self.save_name))

        dlg = QMessageBox(self)
        dlg.setWindowTitle('Сохранение персонажа')
        dlg.setText("Персонаж сохранен")
        button = dlg.exec()

    def generate(self):
        self.ski = ''
        self.name.setText("-")

        self.st = randomch()
        self.dex = randomch()
        self.int = randomch()
        self.cha = randomch()
        self.wis = randomch()
        self.con = randomch()

        self.cclass_roll = randint(1, 3)
        self.race_roll = randint(1, 6)
        self.back_roll = randint(1, 14)

        self.back = cur.execute("""SELECT background FROM backgrounds
                     WHERE id = ?""", (self.back_roll,)).fetchall()[0][0]
        self.back_name = cur.execute("""SELECT title FROM backgrounds
                             WHERE id = ?""", (self.back_roll,)).fetchall()[0][0]
        self.ra = cur.execute("""SELECT title FROM races
                                     WHERE id = ?""", (self.race_roll,)).fetchall()[0][0]
        self.ski = cur.execute("""SELECT skills FROM backgrounds
             WHERE id = ?""", (self.back_roll,)).fetchall()[0][0]
        self.cclass = cur.execute("""SELECT title FROM classes
                     WHERE id = ?""", (self.cclass_roll,)).fetchall()[0][0]

        self.feat = (cur.execute("""SELECT features FROM classes
                     WHERE id = ?""", (self.cclass_roll,)).fetchall()[0][0] +
                     cur.execute("""SELECT features FROM races
                     WHERE id = ?""", (self.race_roll,)).fetchall()[0][0])

        self.tra = (cur.execute("""SELECT traits FROM classes
                    WHERE id = ?""", (self.cclass_roll,)).fetchall()[0][0] +
                    cur.execute("""SELECT traits FROM races
                    WHERE id = ?""", (self.race_roll,)).fetchall()[0][0])

        self.spe = cur.execute("""SELECT speed FROM races
                                             WHERE id = ?""", (self.race_roll,)).fetchall()[0][0]

        self.inv = cur.execute("""SELECT inventory FROM classes
                             WHERE id = ?""", (self.cclass_roll,)).fetchall()[0][0]
        self.cla_ski = cur.execute("""SELECT inventory FROM classes
                                     WHERE id = ?""", (self.cclass_roll,)).fetchall()
        self.ski += ', ' + self.skill_choice() + '.'

        self.hp = cur.execute("""SELECT hit FROM classes
                                     WHERE id = ?""", (self.cclass_roll,)).fetchall()[0][0]
        self.hp_dice = cur.execute("""SELECT hitdice FROM classes
                                             WHERE id = ?""", (self.cclass_roll,)).fetchall()[0][0]
        self.race_ch_plus()

        self.hp = int(self.hp) + (int(self.con) - 10) // 2
        self.ini = (int(self.dex) - 10) // 2
        self.pas = str(10 + (int(self.wis) - 10) // 2)
        self.save_name = self.character_name.text()

        self.in_ui()

    def save_name_edit(self):
        self.save_name = self.character_name.text()
        print(self.save_name)

    def passive_edit(self):
        self.pas = self.passive.text()
        print(self.spe)

    def speed_edit(self):
        self.spe = self.speed.text()
        print(self.spe)

    def race_edit(self):
        self.ra = self.race.text()
        print(self.ra)

    def initiative_edit(self):
        self.ini = self.initiative.text()
        print(self.ini)

    def dice_edit(self):
        self.hp_dice = self.dice.text()
        print(self.hp_dice)

    def hit_edit(self):
        self.hp = self.hit.text()
        print(self.hp)

    def traits_edit(self):
        self.tra = self.traits.toPlainText()

    def inventory_edit(self):
        self.inv = self.inventory.toPlainText()

    def ch_class_edit(self):
        self.cclass = self.ch_class.text()

    def skills_edit(self):
        self.ski = self.skills.toPlainText()

    def features_edit(self):
        self.feat = self.features.toPlainText()

    def background_edit(self):
        self.back = self.background.toPlainText()

    def background_name_edit(self):
        self.back_name = self.background_name.text()

    def strength_edit(self):
        self.st = self.strength.text()
        print(self.st)

    def dexterity_edit(self):
        self.dex = self.dexterity.text()
        print(self.dex)

    def intelligence_edit(self):
        self.int = self.intelligence.text()
        print(self.int)

    def charisma_edit(self):
        self.cha = self.charisma.text()
        print(self.cha)

    def wisdom_edit(self):
        self.wis = self.wisdom.text()
        print(self.wis)

    def constitution_edit(self):
        self.con = self.constitution.text()
        print(self.con)

    def in_ui(self):
        self.passive.setText(self.pas)
        self.race.setText(self.ra)
        self.speed.setText(self.spe)
        self.strength.setText(self.st)
        self.dexterity.setText(self.dex)
        self.intelligence.setText(self.int)
        self.charisma.setText(self.cha)
        self.wisdom.setText(self.wis)
        self.constitution.setText(self.con)
        self.background.setText(str(self.back))
        self.background_name.setText(str(self.back_name))
        self.features.setText(str(self.feat))
        self.skills.setText(self.ski)
        self.ch_class.setText(self.cclass)
        self.inventory.setText(self.inv)
        self.traits.setText(self.tra)
        self.bonus.setText('2')
        self.hit.setText(str(self.hp))
        self.dice.setText(str(self.hp_dice))
        self.initiative.setText(str(self.ini))
        self.character_name.setText(self.save_name)

    def skill_choice(self):
        class_skill = cur.execute("""SELECT skills FROM classes
                                             WHERE id = ?""", (self.cclass_roll,)).fetchall()
        class_dict = {1: 2, 2: 4, 3: 2}

        list_of_skills_ski = self.ski.split(', ')
        list_of_skills = list()
        while len(list_of_skills) != class_dict[int(self.cclass_roll)]:
            random_skill = choice(class_skill[0][0].split(', '))
            if random_skill not in list_of_skills and random_skill not in list_of_skills_ski:
                list_of_skills.append(random_skill)

        list_of_skills = ', '.join(list_of_skills)
        return list_of_skills

    def race_ch_plus(self):

        bonus_ch = cur.execute("""SELECT bonus_ch FROM races
                             WHERE id = ?""", (self.race_roll,)).fetchall()[0][0]
        bonus_ch = bonus_ch.split()

        for el in bonus_ch:
            if el in bonus_ch:
                if el[:2] == 'st':
                    self.st = str(int(self.st) + int(el[2]))
                elif el[:3] == 'dex':
                    self.dex = str(int(self.dex) + int(el[3]))
                elif el[:3] == 'int':
                    self.int = str(int(self.int) + int(el[3]))
                elif el[:3] == 'cha':
                    self.cha = str(int(self.cha) + int(el[3]))
                elif el[:3] == 'wis':
                    self.wis = str(int(self.wis) + int(el[3]))
                elif el[:3] == 'con':
                    self.con = str(int(self.con) + int(el[3]))


class MainWind(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadCharacter.clicked.connect(self.load_character)
        self.createButton.clicked.connect(self.create_character)
        self.load_name = ''
        self.w2 = MyWidget(self, self.load_name)
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 166)
        self.load_data()
        self.tableWidget.cellClicked.connect(self.cell_click)
        self.tableWidget.cellDoubleClicked.connect(self.cell_double_click)

    def load_data(self):
        class_name = cur.execute("""SELECT cclass, back_name, title, ra FROM characters""").fetchall()
        row = 0
        self.tableWidget.setRowCount(len(class_name))
        for el in class_name:
            self.tableWidget.setItem(row, 2, QTableWidgetItem(el[0]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(el[1]))
            self.tableWidget.setItem(row, 0, QTableWidgetItem(el[2]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(el[3]))
            row += 1

    def cell_click(self, row, column):
        self.load_name = self.tableWidget.item(row, 0).text()
        self.character_name.setText(self.load_name)

    def cell_double_click(self, row, column):
        self.load_name = self.tableWidget.item(row, 0).text()
        self.character_name.setText(self.load_name)
        self.w2 = MyWidget(self, self.load_name)
        self.w2.show()
        self.close()

    def create_character(self):
        self.w2 = MyWidget(self, self.load_name)
        self.w2.show()
        self.close()

    def load_character(self):
        flag = False
        self.load_name = self.character_name.text()
        result = cur.execute("""SELECT title FROM characters""").fetchall()
        for el in result:
            if el[0] == self.load_name:
                flag = True
        if flag:
            self.w2 = MyWidget(self, self.load_name)
            self.w2.show()
            self.close()

        else:
            self.load_name = ''
            question = QMessageBox.question(
                self, 'Ошибка', "Персонажа " + str(self.load_name) + " не существует, cоздать нового?",
                QMessageBox.Yes, QMessageBox.No)
            if question == QMessageBox.Yes:
                self.create_character()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWind()
    ex.show()
    sys.exit(app.exec_())


con.close()
