#####################################
# OTHELLO GAME V1.0 by Edan_Zoung
#####################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import sys
import sqlite3
import multitimer

import time
import datetime

class PREDATOR(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=1000
      self.height=1000
      # this will hide the title bar
      #self.setWindowFlag(Qt.FramelessWindowHint)
      self.offset = None
      self.setGeometry(100,100,self.width,self.height)
      self.setWindowTitle('PY-PREDATOR GAME')
      self.setStyleSheet("""
                        QMainWindow{ background-color:#000;color:#fff;
                             background-image: url("images/back.jpg");
                             background-repeat: no-repeat;
                             background-position: center;}
                          QMessageBox{ background-color:#fff}
                         """)
      #self.setFixedSize(self.width,self.height)
      self.setWindowOpacity(1)

      self.direction='Right'
      self.new_direction='Right'
      self.speed=40

      self.value1=0
      self.value2=0
      self.value3=0
      self.value4=0
      self.value5=0
      self.value6=0
      self.value7=0
      self.value8=0
      self.value9=0
      self.value10=0
      self.value11=0
      self.value12=0
      self.value13=0
      self.value14=0
      self.value15=0
      self.value16=0
      self.value17=0
      self.value18=0
      self.value19=0
      self.value20=0
      self.value21=0
      self.value22=0
      self.value23=0
      self.value24=0
      self.value25=0
      self.value26=0
      self.value27=0
      self.value28=0
      self.value29=0
      self.value30=0
      self.value31=0
      self.value32=0
      self.value33=0
      self.value34=0
      self.value35=0
      self.value36=0
      self.value37=0
      self.value38=0
      self.value39=0
      self.value40=0
      self.value41=0
      self.value42=0
      self.value43=0
      self.value44=0
      self.value45=0
      self.value46=0
      self.value47=0
      self.value48=0
      self.value49=0
      self.value50=0
      self.value51=0
      self.value52=0
      self.value53=0
      self.value54=0
      self.value55=0
      self.value56=0
      self.value57=0
      self.value58=0
      self.value59=0
      self.value60=0
      self.value61=0
      self.value62=0
      self.value63=0
      self.value64=0
      self.value65=0
      self.value66=0
      self.value67=0
      self.value68=0
      self.value69=0
      self.value70=0
      self.value71=0
      self.value72=0
      self.value73=0
      self.value74=0
      self.value75=0
      self.value76=0
      self.value77=0
      self.value78=0
      self.value79=0
      self.value80=0
      self.value81=0
      self.value82=0
      self.value83=0
      self.value84=0
      self.value85=0
      self.value86=0
      self.value87=0
      self.value88=0
      self.value89=0
      self.value90=0
      self.value91=0
      self.value92=0
      self.value93=0
      self.value94=0
      self.value95=0
      self.value96=0
      self.value97=0
      self.value98=0
      self.value99=0
      self.value100=0
      self.value101=0
      self.value102=0
      self.value103=0
      self.value104=0
      self.value105=0
      self.value106=0
      self.value107=0
      self.value108=0
      self.value109=0
      self.value110=0
      self.value111=0
      self.value112=0
      self.value113=0
      self.value114=0
      self.value115=0
      self.value116=0
      self.value117=0
      self.value118=0
      self.value119=0
      self.value120=0
      self.value121=0
      self.value122=0
      self.value123=0
      self.value124=0
      self.value125=0
      self.value126=0
      self.value127=0
      self.value128=0
      self.value129=0
      self.value130=0
      self.value131=0
      self.value132=0
      self.value133=0
      self.value134=0
      self.value135=0
      self.value136=0
      self.value137=0
      self.value138=0
      self.value139=0
      self.value140=0
      self.value141=0
      self.value142=0
      self.value143=0
      self.value144=0
      self.value145=0
      self.value146=0
      self.value147=0
      self.value148=0
      self.value149=0
      self.value150=0
      self.value151=0
      self.value152=0
      self.value153=0
      self.value154=0
      self.value155=0
      self.value156=0
      self.value157=0
      self.value158=0
      self.value159=0
      self.value160=0
      self.value161=0
      self.value162=0
      self.value163=0
      self.value164=0
      self.value165=0
      self.value166=0
      self.value167=0
      self.value168=0
      self.value169=0
      self.value170=0
      self.value171=0
      self.value172=0
      self.value173=0
      self.value174=0
      self.value175=0
      self.value176=0
      self.value177=0
      self.value178=0
      self.value179=0
      self.value180=0
      self.value181=0
      self.value182=0
      self.value183=0
      self.value184=0
      self.value185=0
      self.value186=0
      self.value187=0
      self.value188=0
      self.value189=0
      self.value190=0
      self.value191=0
      self.value192=0
      self.value193=0
      self.value194=0
      self.value195=0
      self.value196=0
      self.value197=0
      self.value198=0
      self.value199=0
      self.value200=0
      self.value201=0
      self.value202=0
      self.value203=0
      self.value204=0
      self.value205=0
      self.value206=0
      self.value207=0
      self.value208=0
      self.value209=0
      self.value210=0
      self.value211=0
      self.value212=0
      self.value213=0
      self.value214=0
      self.value215=0
      self.value216=0
      self.value217=0
      self.value218=0
      self.value219=0
      self.value220=0
      self.value221=0
      self.value222=0
      self.value223=0
      self.value224=0
      self.value225=0
      self.value226=0
      self.value227=0
      self.value228=0
      self.value229=0
      self.value230=0
      self.value231=0
      self.value232=0
      self.value233=0
      self.value234=0
      self.value235=0
      self.value236=0
      self.value237=0
      self.value238=0
      self.value239=0
      self.value240=0
      self.value241=0
      self.value242=0
      self.value243=0
      self.value244=0
      self.value245=0
      self.value246=0
      self.value247=0
      self.value248=0
      self.value249=0
      self.value250=0
      self.value251=0
      self.value252=0
      self.value253=0
      self.value254=0
      self.value255=0
      self.value256=0

      self.board=[]

      self.pion1='images/pion1.svg'
      self.pion2='images/pion2.svg'

      # Block gap size between them
      self.gap = 50
      
      self.x=3
      self.y=3
      self.icon_size=100
      self.color1="#666"
      self.color2="#666"
      self.select_color="#555"
      self.focus_color="#31947e"
      self.hover_color="#610dba"
      self.border_color="#31947e"
      self.icon_size=80
      self.app_name="PY PREDATOR"
      

      self.button_case={}
      self.Zone_game()
      self.Design()
      self.showMaximized()
      self.database()
      self.refresh_data()
      
   def Zone_game(self):
      #================================================================================================#
      #================================================================================================#
      #========================================== ZONE GAME ===========================================#
      #================================================================================================#

      #_______TITLE GAME
      self.lab_title=QLabel(self)
      self.lab_title.setStyleSheet("""background-color:transparent;color:#fff;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.lab_title.setCursor(QCursor(Qt.PointingHandCursor))
      self.lab_title.resize(500,100)
      self.pixmap = QPixmap('images/title-game.svg').scaled(500,300)
      self.lab_title.setPixmap(self.pixmap)
      self.lab_title.move(250,5)      

      #_________________________________________RESET GAME

      self.btn_reset=QPushButton('RESET GAME',self)
      self.btn_reset.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::hover{border-style:solid;border-width:1px;border-color:#6600ff;
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_reset.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_reset.clicked.connect(self.reset)
      self.btn_reset.move(1000,100)
      self.btn_reset.resize(200,50)


      #_______SCORE PANEL
      self.score_panel=QLabel(self)
      self.score_panel.setStyleSheet("""background-color:transparent;color:#fff;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.score_panel.setCursor(QCursor(Qt.PointingHandCursor))
      self.score_panel.resize(300,300)
      self.pixmap1 = QPixmap('images/score.png').scaled(300,200)
      self.score_panel.setPixmap(self.pixmap1)
      self.score_panel.move(950,200)

      #_______SCORE VALUE
      self.score_value=QLabel("0000",self)
      self.score_value.setStyleSheet("""background-color:transparent;color:#fff;font-style:italic; font-size:60pt;
                                font-weight:bold;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.score_value.setCursor(QCursor(Qt.PointingHandCursor))
      self.score_value.resize(500,100)
      self.score_value.move(990,300)

      #_______High SCORE RIBBON
      self.hi_score_ribbon=QLabel(self)
      self.hi_score_ribbon.setStyleSheet("""background-color:transparent;color:#fff;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.hi_score_ribbon.setCursor(QCursor(Qt.PointingHandCursor))
      self.hi_score_ribbon.resize(100,100)
      self.pixmap2 = QPixmap('images/high_score.svg').scaled(95,90)
      self.hi_score_ribbon.setPixmap(self.pixmap2)
      self.hi_score_ribbon.move(950,500)

      #_______High SCORE LABEL
      self.hi_score_label=QLabel("High SCORE",self)
      self.hi_score_label.setStyleSheet("""background-color:transparent;color:#fff;font-style:italic; font-size:20pt;
                                font-weight:bold;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.hi_score_label.setCursor(QCursor(Qt.PointingHandCursor))
      self.hi_score_label.resize(500,100)
      self.hi_score_label.move(1050,500)

      #_______High SCORE VALUE
      self.hi_score_value=QLabel("0000",self)
      self.hi_score_value.setStyleSheet("""background-color:transparent;color:#f0f;font-style:italic; font-size:80pt;
                                font-weight:bold;
                    background-repeat: no-repeat; 
                    background-position: center""")
      self.hi_score_value.setCursor(QCursor(Qt.PointingHandCursor))
      self.hi_score_value.resize(500,100)
      self.hi_score_value.move(950,600)

      #______FRAME ZONE
      self.zone_frame=QFrame(self)
      self.zone_frame.setStyleSheet(""" background-color:#000;font-family:Time; font-style:italic; font-size:8pt;
                                font-weight:bold; border-color:#fff; border-style:solid; border-width:3px;
                                border-top-left-radius:0px; border-radius:10px """)

      self.zone_frame.move(100,100)
      self.zone_frame.resize(806,806)

      
      for i in range(16):
         for j in range(16):
            self.button_case[(i,j)]=QToolButton(self.zone_frame)
            self.button_case[(i,j)].setStyleSheet("""
                                  QToolButton::pressed{background-color :#03fcb1;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::focus{background-color :#1b1b1c;color:#fff;border-style:solid;
                                  border-width:2px;border-color:"""+self.border_color+""";font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::hover{background-color :#1b1b1c;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                  
                                """)
            #self.button_case[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            self.button_case[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
            self.button_case[(i,j)].resize(50,50)
            #self.button_case[(i,j)].setFocus(False)


      ###############################################################################
      ################################ FROM 0 TO 7 ##################################

      self.button_case[(0,0)].move(self.x,self.y)
      self.button_case[(0,1)].move(self.x+(self.gap*1),self.y)
      self.button_case[(0,2)].move(self.x+(self.gap*2),self.y)
      self.button_case[(0,3)].move(self.x+(self.gap*3),self.y)
      self.button_case[(0,4)].move(self.x+(self.gap*4),self.y)
      self.button_case[(0,5)].move(self.x+(self.gap*5),self.y)
      self.button_case[(0,6)].move(self.x+(self.gap*6),self.y)
      self.button_case[(0,7)].move(self.x+(self.gap*7),self.y)
      self.button_case[(0,8)].move(self.x+(self.gap*8),self.y)
      self.button_case[(0,9)].move(self.x+(self.gap*9),self.y)
      self.button_case[(0,10)].move(self.x+(self.gap*10),self.y)
      self.button_case[(0,11)].move(self.x+(self.gap*11),self.y)
      self.button_case[(0,12)].move(self.x+(self.gap*12),self.y)
      self.button_case[(0,13)].move(self.x+(self.gap*13),self.y)
      self.button_case[(0,14)].move(self.x+(self.gap*14),self.y)
      self.button_case[(0,15)].move(self.x+(self.gap*15),self.y)
      
      self.button_case[(1,0)].move(self.x,self.y+(self.gap*1))
      self.button_case[(1,1)].move(self.x+(self.gap*1),self.y+(self.gap*1))
      self.button_case[(1,2)].move(self.x+(self.gap*2),self.y+(self.gap*1))
      self.button_case[(1,3)].move(self.x+(self.gap*3),self.y+(self.gap*1))
      self.button_case[(1,4)].move(self.x+(self.gap*4),self.y+(self.gap*1))
      self.button_case[(1,5)].move(self.x+(self.gap*5),self.y+(self.gap*1))
      self.button_case[(1,6)].move(self.x+(self.gap*6),self.y+(self.gap*1))
      self.button_case[(1,7)].move(self.x+(self.gap*7),self.y+(self.gap*1))
      self.button_case[(1,8)].move(self.x+(self.gap*8),self.y+(self.gap*1))
      self.button_case[(1,9)].move(self.x+(self.gap*9),self.y+(self.gap*1))
      self.button_case[(1,10)].move(self.x+(self.gap*10),self.y+(self.gap*1))
      self.button_case[(1,11)].move(self.x+(self.gap*11),self.y+(self.gap*1))
      self.button_case[(1,12)].move(self.x+(self.gap*12),self.y+(self.gap*1))
      self.button_case[(1,13)].move(self.x+(self.gap*13),self.y+(self.gap*1))
      self.button_case[(1,14)].move(self.x+(self.gap*14),self.y+(self.gap*1))
      self.button_case[(1,15)].move(self.x+(self.gap*15),self.y+(self.gap*1))

      
      self.button_case[(2,0)].move(self.x,self.y+(self.gap*2))
      self.button_case[(2,1)].move(self.x+(self.gap*1),self.y+(self.gap*2))
      self.button_case[(2,2)].move(self.x+(self.gap*2),self.y+(self.gap*2))
      self.button_case[(2,3)].move(self.x+(self.gap*3),self.y+(self.gap*2))
      self.button_case[(2,4)].move(self.x+(self.gap*4),self.y+(self.gap*2))
      self.button_case[(2,5)].move(self.x+(self.gap*5),self.y+(self.gap*2))
      self.button_case[(2,6)].move(self.x+(self.gap*6),self.y+(self.gap*2))
      self.button_case[(2,7)].move(self.x+(self.gap*7),self.y+(self.gap*2))
      self.button_case[(2,8)].move(self.x+(self.gap*8),self.y+(self.gap*2))
      self.button_case[(2,9)].move(self.x+(self.gap*9),self.y+(self.gap*2))
      self.button_case[(2,10)].move(self.x+(self.gap*10),self.y+(self.gap*2))
      self.button_case[(2,11)].move(self.x+(self.gap*11),self.y+(self.gap*2))
      self.button_case[(2,12)].move(self.x+(self.gap*12),self.y+(self.gap*2))
      self.button_case[(2,13)].move(self.x+(self.gap*13),self.y+(self.gap*2))
      self.button_case[(2,14)].move(self.x+(self.gap*14),self.y+(self.gap*2))
      self.button_case[(2,15)].move(self.x+(self.gap*15),self.y+(self.gap*2))

      
      self.button_case[(3,0)].move(self.x,self.y+(self.gap*3))
      self.button_case[(3,1)].move(self.x+(self.gap*1),self.y+(self.gap*3))
      self.button_case[(3,2)].move(self.x+(self.gap*2),self.y+(self.gap*3))
      self.button_case[(3,3)].move(self.x+(self.gap*3),self.y+(self.gap*3))
      self.button_case[(3,4)].move(self.x+(self.gap*4),self.y+(self.gap*3))
      self.button_case[(3,5)].move(self.x+(self.gap*5),self.y+(self.gap*3))
      self.button_case[(3,6)].move(self.x+(self.gap*6),self.y+(self.gap*3))
      self.button_case[(3,7)].move(self.x+(self.gap*7),self.y+(self.gap*3))
      self.button_case[(3,8)].move(self.x+(self.gap*8),self.y+(self.gap*3))
      self.button_case[(3,9)].move(self.x+(self.gap*9),self.y+(self.gap*3))
      self.button_case[(3,10)].move(self.x+(self.gap*10),self.y+(self.gap*3))
      self.button_case[(3,11)].move(self.x+(self.gap*11),self.y+(self.gap*3))
      self.button_case[(3,12)].move(self.x+(self.gap*12),self.y+(self.gap*3))
      self.button_case[(3,13)].move(self.x+(self.gap*13),self.y+(self.gap*3))
      self.button_case[(3,14)].move(self.x+(self.gap*14),self.y+(self.gap*3))
      self.button_case[(3,15)].move(self.x+(self.gap*15),self.y+(self.gap*3))

      self.button_case[(4,0)].move(self.x,self.y+(self.gap*4))
      self.button_case[(4,1)].move(self.x+(self.gap*1),self.y+(self.gap*4))
      self.button_case[(4,2)].move(self.x+(self.gap*2),self.y+(self.gap*4))
      self.button_case[(4,3)].move(self.x+(self.gap*3),self.y+(self.gap*4))
      self.button_case[(4,4)].move(self.x+(self.gap*4),self.y+(self.gap*4))
      self.button_case[(4,5)].move(self.x+(self.gap*5),self.y+(self.gap*4))
      self.button_case[(4,6)].move(self.x+(self.gap*6),self.y+(self.gap*4))
      self.button_case[(4,7)].move(self.x+(self.gap*7),self.y+(self.gap*4))
      self.button_case[(4,8)].move(self.x+(self.gap*8),self.y+(self.gap*4))
      self.button_case[(4,9)].move(self.x+(self.gap*9),self.y+(self.gap*4))
      self.button_case[(4,10)].move(self.x+(self.gap*10),self.y+(self.gap*4))
      self.button_case[(4,11)].move(self.x+(self.gap*11),self.y+(self.gap*4))
      self.button_case[(4,12)].move(self.x+(self.gap*12),self.y+(self.gap*4))
      self.button_case[(4,13)].move(self.x+(self.gap*13),self.y+(self.gap*4))
      self.button_case[(4,14)].move(self.x+(self.gap*14),self.y+(self.gap*4))
      self.button_case[(4,15)].move(self.x+(self.gap*15),self.y+(self.gap*4))

      
      self.button_case[(5,0)].move(self.x,self.y+(self.gap*5))
      self.button_case[(5,1)].move(self.x+(self.gap*1),self.y+(self.gap*5))
      self.button_case[(5,2)].move(self.x+(self.gap*2),self.y+(self.gap*5))
      self.button_case[(5,3)].move(self.x+(self.gap*3),self.y+(self.gap*5))
      self.button_case[(5,4)].move(self.x+(self.gap*4),self.y+(self.gap*5))
      self.button_case[(5,5)].move(self.x+(self.gap*5),self.y+(self.gap*5))
      self.button_case[(5,6)].move(self.x+(self.gap*6),self.y+(self.gap*5))
      self.button_case[(5,7)].move(self.x+(self.gap*7),self.y+(self.gap*5))
      self.button_case[(5,8)].move(self.x+(self.gap*8),self.y+(self.gap*5))
      self.button_case[(5,9)].move(self.x+(self.gap*9),self.y+(self.gap*5))
      self.button_case[(5,10)].move(self.x+(self.gap*10),self.y+(self.gap*5))
      self.button_case[(5,11)].move(self.x+(self.gap*11),self.y+(self.gap*5))
      self.button_case[(5,12)].move(self.x+(self.gap*12),self.y+(self.gap*5))
      self.button_case[(5,13)].move(self.x+(self.gap*13),self.y+(self.gap*5))
      self.button_case[(5,14)].move(self.x+(self.gap*14),self.y+(self.gap*5))
      self.button_case[(5,15)].move(self.x+(self.gap*15),self.y+(self.gap*5))

      
      self.button_case[(6,0)].move(self.x,self.y+(self.gap*6))
      self.button_case[(6,1)].move(self.x+(self.gap*1),self.y+(self.gap*6))
      self.button_case[(6,2)].move(self.x+(self.gap*2),self.y+(self.gap*6))
      self.button_case[(6,3)].move(self.x+(self.gap*3),self.y+(self.gap*6))
      self.button_case[(6,4)].move(self.x+(self.gap*4),self.y+(self.gap*6))
      self.button_case[(6,5)].move(self.x+(self.gap*5),self.y+(self.gap*6))
      self.button_case[(6,6)].move(self.x+(self.gap*6),self.y+(self.gap*6))
      self.button_case[(6,7)].move(self.x+(self.gap*7),self.y+(self.gap*6))
      self.button_case[(6,8)].move(self.x+(self.gap*8),self.y+(self.gap*6))
      self.button_case[(6,9)].move(self.x+(self.gap*9),self.y+(self.gap*6))
      self.button_case[(6,10)].move(self.x+(self.gap*10),self.y+(self.gap*6))
      self.button_case[(6,11)].move(self.x+(self.gap*11),self.y+(self.gap*6))
      self.button_case[(6,12)].move(self.x+(self.gap*12),self.y+(self.gap*6))
      self.button_case[(6,13)].move(self.x+(self.gap*13),self.y+(self.gap*6))
      self.button_case[(6,14)].move(self.x+(self.gap*14),self.y+(self.gap*6))
      self.button_case[(6,15)].move(self.x+(self.gap*15),self.y+(self.gap*6))

      
      self.button_case[(7,0)].move(self.x,self.y+(self.gap*7))
      self.button_case[(7,1)].move(self.x+(self.gap*1),self.y+(self.gap*7))
      self.button_case[(7,2)].move(self.x+(self.gap*2),self.y+(self.gap*7))
      self.button_case[(7,3)].move(self.x+(self.gap*3),self.y+(self.gap*7))
      self.button_case[(7,4)].move(self.x+(self.gap*4),self.y+(self.gap*7))
      self.button_case[(7,5)].move(self.x+(self.gap*5),self.y+(self.gap*7))
      self.button_case[(7,6)].move(self.x+(self.gap*6),self.y+(self.gap*7))
      self.button_case[(7,7)].move(self.x+(self.gap*7),self.y+(self.gap*7))
      self.button_case[(7,8)].move(self.x+(self.gap*8),self.y+(self.gap*7))
      self.button_case[(7,9)].move(self.x+(self.gap*9),self.y+(self.gap*7))
      self.button_case[(7,10)].move(self.x+(self.gap*10),self.y+(self.gap*7))
      self.button_case[(7,11)].move(self.x+(self.gap*11),self.y+(self.gap*7))
      self.button_case[(7,12)].move(self.x+(self.gap*12),self.y+(self.gap*7))
      self.button_case[(7,13)].move(self.x+(self.gap*13),self.y+(self.gap*7))
      self.button_case[(7,14)].move(self.x+(self.gap*14),self.y+(self.gap*7))
      self.button_case[(7,15)].move(self.x+(self.gap*15),self.y+(self.gap*7))


      ###############################################################################
      ################################ FROM 8 TO 15 #################################


      self.button_case[(8,0)].move(self.x,self.y+(self.gap*8))
      self.button_case[(8,1)].move(self.x+(self.gap*1),self.y+(self.gap*8))
      self.button_case[(8,2)].move(self.x+(self.gap*2),self.y+(self.gap*8))
      self.button_case[(8,3)].move(self.x+(self.gap*3),self.y+(self.gap*8))
      self.button_case[(8,4)].move(self.x+(self.gap*4),self.y+(self.gap*8))
      self.button_case[(8,5)].move(self.x+(self.gap*5),self.y+(self.gap*8))
      self.button_case[(8,6)].move(self.x+(self.gap*6),self.y+(self.gap*8))
      self.button_case[(8,7)].move(self.x+(self.gap*7),self.y+(self.gap*8))
      self.button_case[(8,8)].move(self.x+(self.gap*8),self.y+(self.gap*8))
      self.button_case[(8,9)].move(self.x+(self.gap*9),self.y+(self.gap*8))
      self.button_case[(8,10)].move(self.x+(self.gap*10),self.y+(self.gap*8))
      self.button_case[(8,11)].move(self.x+(self.gap*11),self.y+(self.gap*8))
      self.button_case[(8,12)].move(self.x+(self.gap*12),self.y+(self.gap*8))
      self.button_case[(8,13)].move(self.x+(self.gap*13),self.y+(self.gap*8))
      self.button_case[(8,14)].move(self.x+(self.gap*14),self.y+(self.gap*8))
      self.button_case[(8,15)].move(self.x+(self.gap*15),self.y+(self.gap*8))

      
      self.button_case[(9,0)].move(self.x,self.y+(self.gap*9))
      self.button_case[(9,1)].move(self.x+(self.gap*1),self.y+(self.gap*9))
      self.button_case[(9,2)].move(self.x+(self.gap*2),self.y+(self.gap*9))
      self.button_case[(9,3)].move(self.x+(self.gap*3),self.y+(self.gap*9))
      self.button_case[(9,4)].move(self.x+(self.gap*4),self.y+(self.gap*9))
      self.button_case[(9,5)].move(self.x+(self.gap*5),self.y+(self.gap*9))
      self.button_case[(9,6)].move(self.x+(self.gap*6),self.y+(self.gap*9))
      self.button_case[(9,7)].move(self.x+(self.gap*7),self.y+(self.gap*9))
      self.button_case[(9,8)].move(self.x+(self.gap*8),self.y+(self.gap*9))
      self.button_case[(9,9)].move(self.x+(self.gap*9),self.y+(self.gap*9))
      self.button_case[(9,10)].move(self.x+(self.gap*10),self.y+(self.gap*9))
      self.button_case[(9,11)].move(self.x+(self.gap*11),self.y+(self.gap*9))
      self.button_case[(9,12)].move(self.x+(self.gap*12),self.y+(self.gap*9))
      self.button_case[(9,13)].move(self.x+(self.gap*13),self.y+(self.gap*9))
      self.button_case[(9,14)].move(self.x+(self.gap*14),self.y+(self.gap*9))
      self.button_case[(9,15)].move(self.x+(self.gap*15),self.y+(self.gap*9))

      
      self.button_case[(10,0)].move(self.x,self.y+(self.gap*10))
      self.button_case[(10,1)].move(self.x+(self.gap*1),self.y+(self.gap*10))
      self.button_case[(10,2)].move(self.x+(self.gap*2),self.y+(self.gap*10))
      self.button_case[(10,3)].move(self.x+(self.gap*3),self.y+(self.gap*10))
      self.button_case[(10,4)].move(self.x+(self.gap*4),self.y+(self.gap*10))
      self.button_case[(10,5)].move(self.x+(self.gap*5),self.y+(self.gap*10))
      self.button_case[(10,6)].move(self.x+(self.gap*6),self.y+(self.gap*10))
      self.button_case[(10,7)].move(self.x+(self.gap*7),self.y+(self.gap*10))
      self.button_case[(10,8)].move(self.x+(self.gap*8),self.y+(self.gap*10))
      self.button_case[(10,9)].move(self.x+(self.gap*9),self.y+(self.gap*10))
      self.button_case[(10,10)].move(self.x+(self.gap*10),self.y+(self.gap*10))
      self.button_case[(10,11)].move(self.x+(self.gap*11),self.y+(self.gap*10))
      self.button_case[(10,12)].move(self.x+(self.gap*12),self.y+(self.gap*10))
      self.button_case[(10,13)].move(self.x+(self.gap*13),self.y+(self.gap*10))
      self.button_case[(10,14)].move(self.x+(self.gap*14),self.y+(self.gap*10))
      self.button_case[(10,15)].move(self.x+(self.gap*15),self.y+(self.gap*10))

      self.button_case[(11,0)].move(self.x,self.y+(self.gap*11))
      self.button_case[(11,1)].move(self.x+(self.gap*1),self.y+(self.gap*11))
      self.button_case[(11,2)].move(self.x+(self.gap*2),self.y+(self.gap*11))
      self.button_case[(11,3)].move(self.x+(self.gap*3),self.y+(self.gap*11))
      self.button_case[(11,4)].move(self.x+(self.gap*4),self.y+(self.gap*11))
      self.button_case[(11,5)].move(self.x+(self.gap*5),self.y+(self.gap*11))
      self.button_case[(11,6)].move(self.x+(self.gap*6),self.y+(self.gap*11))
      self.button_case[(11,7)].move(self.x+(self.gap*7),self.y+(self.gap*11))
      self.button_case[(11,8)].move(self.x+(self.gap*8),self.y+(self.gap*11))
      self.button_case[(11,9)].move(self.x+(self.gap*9),self.y+(self.gap*11))
      self.button_case[(11,10)].move(self.x+(self.gap*10),self.y+(self.gap*11))
      self.button_case[(11,11)].move(self.x+(self.gap*11),self.y+(self.gap*11))
      self.button_case[(11,12)].move(self.x+(self.gap*12),self.y+(self.gap*11))
      self.button_case[(11,13)].move(self.x+(self.gap*13),self.y+(self.gap*11))
      self.button_case[(11,14)].move(self.x+(self.gap*14),self.y+(self.gap*11))
      self.button_case[(11,15)].move(self.x+(self.gap*15),self.y+(self.gap*11))

      
      self.button_case[(12,0)].move(self.x,self.y+(self.gap*12))
      self.button_case[(12,1)].move(self.x+(self.gap*1),self.y+(self.gap*12))
      self.button_case[(12,2)].move(self.x+(self.gap*2),self.y+(self.gap*12))
      self.button_case[(12,3)].move(self.x+(self.gap*3),self.y+(self.gap*12))
      self.button_case[(12,4)].move(self.x+(self.gap*4),self.y+(self.gap*12))
      self.button_case[(12,5)].move(self.x+(self.gap*5),self.y+(self.gap*12))
      self.button_case[(12,6)].move(self.x+(self.gap*6),self.y+(self.gap*12))
      self.button_case[(12,7)].move(self.x+(self.gap*7),self.y+(self.gap*12))
      self.button_case[(12,8)].move(self.x+(self.gap*8),self.y+(self.gap*12))
      self.button_case[(12,9)].move(self.x+(self.gap*9),self.y+(self.gap*12))
      self.button_case[(12,10)].move(self.x+(self.gap*10),self.y+(self.gap*12))
      self.button_case[(12,11)].move(self.x+(self.gap*11),self.y+(self.gap*12))
      self.button_case[(12,12)].move(self.x+(self.gap*12),self.y+(self.gap*12))
      self.button_case[(12,13)].move(self.x+(self.gap*13),self.y+(self.gap*12))
      self.button_case[(12,14)].move(self.x+(self.gap*14),self.y+(self.gap*12))
      self.button_case[(12,15)].move(self.x+(self.gap*15),self.y+(self.gap*12))

      
      self.button_case[(13,0)].move(self.x,self.y+(self.gap*13))
      self.button_case[(13,1)].move(self.x+(self.gap*1),self.y+(self.gap*13))
      self.button_case[(13,2)].move(self.x+(self.gap*2),self.y+(self.gap*13))
      self.button_case[(13,3)].move(self.x+(self.gap*3),self.y+(self.gap*13))
      self.button_case[(13,4)].move(self.x+(self.gap*4),self.y+(self.gap*13))
      self.button_case[(13,5)].move(self.x+(self.gap*5),self.y+(self.gap*13))
      self.button_case[(13,6)].move(self.x+(self.gap*6),self.y+(self.gap*13))
      self.button_case[(13,7)].move(self.x+(self.gap*7),self.y+(self.gap*13))
      self.button_case[(13,8)].move(self.x+(self.gap*8),self.y+(self.gap*13))
      self.button_case[(13,9)].move(self.x+(self.gap*9),self.y+(self.gap*13))
      self.button_case[(13,10)].move(self.x+(self.gap*10),self.y+(self.gap*13))
      self.button_case[(13,11)].move(self.x+(self.gap*11),self.y+(self.gap*13))
      self.button_case[(13,12)].move(self.x+(self.gap*12),self.y+(self.gap*13))
      self.button_case[(13,13)].move(self.x+(self.gap*13),self.y+(self.gap*13))
      self.button_case[(13,14)].move(self.x+(self.gap*14),self.y+(self.gap*13))
      self.button_case[(13,15)].move(self.x+(self.gap*15),self.y+(self.gap*13))

      
      self.button_case[(14,0)].move(self.x,self.y+(self.gap*14))
      self.button_case[(14,1)].move(self.x+(self.gap*1),self.y+(self.gap*14))
      self.button_case[(14,2)].move(self.x+(self.gap*2),self.y+(self.gap*14))
      self.button_case[(14,3)].move(self.x+(self.gap*3),self.y+(self.gap*14))
      self.button_case[(14,4)].move(self.x+(self.gap*4),self.y+(self.gap*14))
      self.button_case[(14,5)].move(self.x+(self.gap*5),self.y+(self.gap*14))
      self.button_case[(14,6)].move(self.x+(self.gap*6),self.y+(self.gap*14))
      self.button_case[(14,7)].move(self.x+(self.gap*7),self.y+(self.gap*14))
      self.button_case[(14,8)].move(self.x+(self.gap*8),self.y+(self.gap*14))
      self.button_case[(14,9)].move(self.x+(self.gap*9),self.y+(self.gap*14))
      self.button_case[(14,10)].move(self.x+(self.gap*10),self.y+(self.gap*14))
      self.button_case[(14,11)].move(self.x+(self.gap*11),self.y+(self.gap*14))
      self.button_case[(14,12)].move(self.x+(self.gap*12),self.y+(self.gap*14))
      self.button_case[(14,13)].move(self.x+(self.gap*13),self.y+(self.gap*14))
      self.button_case[(14,14)].move(self.x+(self.gap*14),self.y+(self.gap*14))
      self.button_case[(14,15)].move(self.x+(self.gap*15),self.y+(self.gap*14))


      self.button_case[(15,0)].move(self.x,self.y+(self.gap*15))
      self.button_case[(15,1)].move(self.x+(self.gap*1),self.y+(self.gap*15))
      self.button_case[(15,2)].move(self.x+(self.gap*2),self.y+(self.gap*15))
      self.button_case[(15,3)].move(self.x+(self.gap*3),self.y+(self.gap*15))
      self.button_case[(15,4)].move(self.x+(self.gap*4),self.y+(self.gap*15))
      self.button_case[(15,5)].move(self.x+(self.gap*5),self.y+(self.gap*15))
      self.button_case[(15,6)].move(self.x+(self.gap*6),self.y+(self.gap*15))
      self.button_case[(15,7)].move(self.x+(self.gap*7),self.y+(self.gap*15))
      self.button_case[(15,8)].move(self.x+(self.gap*8),self.y+(self.gap*15))
      self.button_case[(15,9)].move(self.x+(self.gap*9),self.y+(self.gap*15))
      self.button_case[(15,10)].move(self.x+(self.gap*10),self.y+(self.gap*15))
      self.button_case[(15,11)].move(self.x+(self.gap*11),self.y+(self.gap*15))
      self.button_case[(15,12)].move(self.x+(self.gap*12),self.y+(self.gap*15))
      self.button_case[(15,13)].move(self.x+(self.gap*13),self.y+(self.gap*15))
      self.button_case[(15,14)].move(self.x+(self.gap*14),self.y+(self.gap*15))
      self.button_case[(15,15)].move(self.x+(self.gap*15),self.y+(self.gap*15))
      #================================================================================================#
      #================================================================================================#
      #========================================== ZONE GAME ===========================================#
      #================================================================================================#

   def Design(self):
      self.button_case[(0,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(0,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(0,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(0,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(0,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(0,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(1,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(1,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(1,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(1,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(1,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(1,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(2,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(2,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(2,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(2,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(2,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(2,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(3,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(3,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(3,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(3,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(3,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(3,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(4,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(4,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(4,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(4,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(4,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(4,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(5,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(5,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(5,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(5,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(5,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(5,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(6,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(6,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(6,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(6,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(6,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(6,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(7,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(7,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(7,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(7,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(7,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(7,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(8,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(8,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(8,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(8,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(8,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(8,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(9,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(9,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(9,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(9,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(9,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(9,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(10,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(10,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(10,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(10,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(10,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(10,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(11,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(11,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(11,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(11,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(11,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(11,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(12,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(12,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(12,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(12,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(12,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(12,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(13,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(13,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(13,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(13,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(13,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(13,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(14,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(14,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(14,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(14,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(14,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(14,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(15,0)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}
                                               
                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,1)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,2)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,3)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,4)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,5)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,6)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,7)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(15,8)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,9)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(15,10)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,11)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(15,12)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,13)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")

      self.button_case[(15,14)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color2+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")
      
      self.button_case[(15,15)].setStyleSheet("""QToolButton::!pressed{background-color:"""+self.color1+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::pressed{background-color:"""+self.select_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::focus{background-color:"""+self.focus_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:10px}

                                               QToolButton::hover{background-color:"""+self.hover_color+""";
                                               border-style:solid;border-width:3px;border-color:"""+self.border_color+""";
                                               font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;border-radius:30px}""")


   def database(self):
      
      record_game=[ (1,0,""), (2,0,""), (3,0,""), (4,0,""), (5,0,""), (6,0,""), (7,0,""), (8,0,""),
                    (9,0,""), (10,0,""), (11,0,""), (12,0,""), (13,0,""), (14,0,""), (15,0,""), (16,0,""),
                    (17,0,""), (18,0,""), (19,0,""), (20,0,""), (21,0,""), (22,0,""), (23,0,""), (24,0,""),
                    (25,0,""), (26,0,""), (27,0,""), (28,0,""), (29,0,""), (30,0,""), (31,0,""), (32,0,""),
                    (33,0,""), (34,0,""), (35,0,""), (36,0,""), (37,0,""), (38,0,""), (39,0,""), (40,0,""),
                    (41,0,""), (42,0,""), (43,0,""), (44,0,""), (45,0,""), (46,0,""), (47,0,""), (48,0,""),
                    (49,0,""), (50,0,""), (51,0,""), (52,0,""), (53,0,""), (54,0,""), (55,0,""), (56,0,""),
                    (57,0,""), (58,0,""), (59,0,""), (60,0,""), (61,0,""), (62,0,""), (63,0,""), (64,0,""),
                    (65,0,""), (66,0,""), (67,0,""), (68,0,""), (69,0,""), (70,0,""), (71,0,""), (72,0,""),
                    (73,0,""), (74,0,""), (75,0,""), (76,0,""), (77,0,""), (78,0,""), (79,0,""), (80,0,""),
                    (81,0,""), (82,0,""), (83,0,""), (84,0,""), (85,0,""), (86,0,""), (87,0,""), (88,0,""),
                    (89,0,""), (90,0,""), (91,0,""), (92,0,""), (93,0,""), (94,0,""), (95,0,""), (96,0,""),
                    (97,0,""), (98,0,""), (99,0,""), (100,0,""), (101,0,""), (102,0,""), (103,0,""), (104,0,""),
                    (105,0,""), (106,0,""), (107,0,""), (108,0,""), (109,0,""), (110,0,""), (111,0,""), (112,0,""),
                    (113,0,""), (114,0,""), (115,0,""), (116,0,""), (117,0,""), (118,0,""), (119,0,""), (120,0,""),
                    (121,0,""), (122,0,""), (123,0,""), (124,0,""), (125,0,""), (126,0,""), (127,0,""), (128,0,""),
                    (129,0,""), (130,0,""), (131,0,""), (132,0,""), (133,0,""), (134,0,""), (135,0,""), (136,0,""),
                    (137,0,""), (138,0,""), (139,0,""), (140,0,""), (141,0,""), (142,0,""), (143,0,""), (144,0,""),
                    (145,0,""), (146,0,""), (147,0,""), (148,0,""), (149,0,""), (150,0,""), (151,0,""), (152,0,""),
                    (153,0,""), (154,0,""), (155,0,""), (156,0,""), (157,0,""), (158,0,""), (159,0,""), (160,0,""),
                    (161,0,""), (162,0,""), (163,0,""), (164,0,""), (165,0,""), (166,0,""), (167,0,""), (168,0,""),
                    (169,0,""), (170,0,""), (171,0,""), (172,0,""), (173,0,""), (174,0,""), (175,0,""), (176,0,""),
                    (177,0,""), (178,0,""), (179,0,""), (180,0,""), (181,0,""), (182,0,""), (183,0,""), (184,0,""),
                    (185,0,""), (186,0,""), (187,0,""), (188,0,""), (189,0,""), (190,0,""), (191,0,""), (192,0,""),
                    (193,0,""), (194,0,""), (195,0,""), (196,0,""), (197,0,""), (198,0,""), (199,0,""), (200,0,""),
                    (201,0,""), (202,0,""), (203,0,""), (204,0,""), (205,0,""), (206,0,""), (207,0,""), (208,0,""),
                    (209,0,""), (210,0,""), (211,0,""), (212,0,""), (213,0,""), (214,0,""), (215,0,""), (216,0,""),
                    (217,0,""), (218,0,""), (219,0,""), (220,0,""), (221,0,""), (222,0,""), (223,0,""), (224,0,""),
                    (225,0,""), (226,0,""), (227,0,""), (228,0,""), (229,0,""), (230,0,""), (231,0,""), (232,0,""),
                    (233,0,""), (234,0,""), (235,0,""), (236,0,""), (237,0,""), (238,0,""), (239,0,""), (240,0,""),
                    (241,1,"images/pion1.svg"), (242,1,"images/pion1.svg"), (243,1,"images/pion1.svg"), (244,1,"images/pion1.svg"),
                    (245,2,"images/pion2.svg"), (246,0,""), (247,0,""), (248,0,""),
                    (249,0,""), (250,0,""), (251,0,""), (252,0,""), (253,0,""), (254,0,""), (255,0,""), (256,0,"")]
      
      if not os.path.exists('predator.bd') and not os.path.isfile('predator.bd'):
         try:
            self.bdd=sqlite3.connect('predator.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,self.app_name,e,QMessageBox.Ok)
         finally:
            if self.bdd:

               # GAME TABLE
               self.cursor=self.bdd.cursor()
               self.cursor.execute("""
                                   CREATE TABLE IF NOT EXISTS game (
                                   id integer primary key,
                                   value integer,
                                   image text)""")
               
               self.cursor.executemany("""INSERT INTO game (id,value,image)
                                      VALUES (?,?,?)""",record_game)
               # SCORE TABLE
               self.cursor.execute("""
                                   CREATE TABLE IF NOT EXISTS score (
                                   id integer primary key,
                                   value integer)""")
               
               self.cursor.execute("""INSERT INTO score (id,value)
                                      VALUES (?,?)""",(1,0))
               # HIGH SCORE TABLE
               self.cursor.execute("""
                                   CREATE TABLE IF NOT EXISTS hi_score (
                                   id integer primary key,
                                   value integer)""")
               
               self.cursor.execute("""INSERT INTO hi_score (id,value)
                                      VALUES (?,?)""",(1,0))
               
               self.bdd.commit()
               self.bdd.close()

            else:
               self.bdd.rollback()
               QMessageBox.information(self,self.app_name,"BASE DE DONNEE NON CREEE \nUNE ERREUR S'EST PRODUITE ",QMessageBox.Ok)
      else:
         pass

   def refresh_data(self):
      if os.path.exists('predator.bd') and os.path.isfile('predator.bd'):
         try:
            self.bdd=sqlite3.connect('predator.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,"PREDATOR",e)
         finally:
            self.cursor=self.bdd.cursor()
            
            #________DATA
            self.block=self.cursor.execute("SELECT value,image FROM game")
            self.data = self.block.fetchall()

            ########################### LINE 1
            if int(self.data[0][0])==1:
               self.button_case[(0,0)].setIcon(QIcon(self.data[0][1]))
               self.button_case[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[1][0])==1:
               self.button_case[(0,1)].setIcon(QIcon(self.data[1][1]))
               self.button_case[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[2][0])==1:
               self.button_case[(0,2)].setIcon(QIcon(self.data[2][1]))
               self.button_case[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[3][0])==1:
               self.button_case[(0,3)].setIcon(QIcon(self.data[3][1]))
               self.button_case[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[4][0])==1:
               self.button_case[(0,4)].setIcon(QIcon(self.data[4][1]))
               self.button_case[(0,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[5][0])==1:
               self.button_case[(0,5)].setIcon(QIcon(self.data[5][1]))
               self.button_case[(0,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[6][0])==1:
               self.button_case[(0,6)].setIcon(QIcon(self.data[6][1]))
               self.button_case[(0,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[7][0])==1:
               self.button_case[(0,7)].setIcon(QIcon(self.data[7][1]))
               self.button_case[(0,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[8][0])==1:
               self.button_case[(0,8)].setIcon(QIcon(self.data[8][1]))
               self.button_case[(0,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[9][0])==1:
               self.button_case[(0,9)].setIcon(QIcon(self.data[9][1]))
               self.button_case[(0,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[10][0])==1:
               self.button_case[(0,10)].setIcon(QIcon(self.data[10][1]))
               self.button_case[(0,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[11][0])==1:
               self.button_case[(0,11)].setIcon(QIcon(self.data[11][1]))
               self.button_case[(0,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[12][0])==1:
               self.button_case[(0,12)].setIcon(QIcon(self.data[12][1]))
               self.button_case[(0,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[13][0])==1:
               self.button_case[(0,13)].setIcon(QIcon(self.data[13][1]))
               self.button_case[(0,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[14][0])==1:
               self.button_case[(0,14)].setIcon(QIcon(self.data[14][1]))
               self.button_case[(0,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[15][0])==1:
               self.button_case[(0,15)].setIcon(QIcon(self.data[15][1]))
               self.button_case[(0,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 2
            if int(self.data[16][0])==1:
               self.button_case[(1,0)].setIcon(QIcon(self.data[16][1]))
               self.button_case[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[17][0])==1:
               self.button_case[(1,1)].setIcon(QIcon(self.data[17][1]))
               self.button_case[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[18][0])==1:
               self.button_case[(1,2)].setIcon(QIcon(self.data[18][1]))
               self.button_case[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[19][0])==1:
               self.button_case[(1,3)].setIcon(QIcon(self.data[19][1]))
               self.button_case[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[20][0])==1:
               self.button_case[(1,4)].setIcon(QIcon(self.data[20][1]))
               self.button_case[(1,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[21][0])==1:
               self.button_case[(1,5)].setIcon(QIcon(self.data[21][1]))
               self.button_case[(1,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[22][0])==1:
               self.button_case[(1,6)].setIcon(QIcon(self.data[22][1]))
               self.button_case[(1,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[23][0])==1:
               self.button_case[(1,7)].setIcon(QIcon(self.data[23][1]))
               self.button_case[(1,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[24][0])==1:
               self.button_case[(1,8)].setIcon(QIcon(self.data[24][1]))
               self.button_case[(1,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[25][0])==1:
               self.button_case[(1,9)].setIcon(QIcon(self.data[25][1]))
               self.button_case[(1,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[26][0])==1:
               self.button_case[(1,10)].setIcon(QIcon(self.data[26][1]))
               self.button_case[(1,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[27][0])==1:
               self.button_case[(1,11)].setIcon(QIcon(self.data[27][1]))
               self.button_case[(1,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[28][0])==1:
               self.button_case[(1,12)].setIcon(QIcon(self.data[28][1]))
               self.button_case[(1,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[29][0])==1:
               self.button_case[(1,13)].setIcon(QIcon(self.data[29][1]))
               self.button_case[(1,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[30][0])==1:
               self.button_case[(1,14)].setIcon(QIcon(self.data[30][1]))
               self.button_case[(1,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[31][0])==1:
               self.button_case[(1,15)].setIcon(QIcon(self.data[31][1]))
               self.button_case[(1,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 3
            if int(self.data[32][0])==1:
               self.button_case[(2,0)].setIcon(QIcon(self.data[32][1]))
               self.button_case[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[33][0])==1:
               self.button_case[(2,1)].setIcon(QIcon(self.data[33][1]))
               self.button_case[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[34][0])==1:
               self.button_case[(2,2)].setIcon(QIcon(self.data[34][1]))
               self.button_case[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[35][0])==1:
               self.button_case[(2,3)].setIcon(QIcon(self.data[35][1]))
               self.button_case[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[36][0])==1:
               self.button_case[(2,4)].setIcon(QIcon(self.data[36][1]))
               self.button_case[(2,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[37][0])==1:
               self.button_case[(2,5)].setIcon(QIcon(self.data[37][1]))
               self.button_case[(2,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[38][0])==1:
               self.button_case[(2,6)].setIcon(QIcon(self.data[38][1]))
               self.button_case[(2,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[39][0])==1:
               self.button_case[(2,7)].setIcon(QIcon(self.data[39][1]))
               self.button_case[(2,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[40][0])==1:
               self.button_case[(2,8)].setIcon(QIcon(self.data[40][1]))
               self.button_case[(2,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[41][0])==1:
               self.button_case[(2,9)].setIcon(QIcon(self.data[41][1]))
               self.button_case[(2,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[42][0])==1:
               self.button_case[(2,10)].setIcon(QIcon(self.data[42][1]))
               self.button_case[(2,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[43][0])==1:
               self.button_case[(2,11)].setIcon(QIcon(self.data[43][1]))
               self.button_case[(2,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[44][0])==1:
               self.button_case[(2,12)].setIcon(QIcon(self.data[44][1]))
               self.button_case[(2,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[45][0])==1:
               self.button_case[(2,13)].setIcon(QIcon(self.data[45][1]))
               self.button_case[(2,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[46][0])==1:
               self.button_case[(2,14)].setIcon(QIcon(self.data[46][1]))
               self.button_case[(2,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[47][0])==1:
               self.button_case[(2,15)].setIcon(QIcon(self.data[47][1]))
               self.button_case[(2,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 4
            if int(self.data[48][0])==1:
               self.button_case[(3,0)].setIcon(QIcon(self.data[48][1]))
               self.button_case[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[49][0])==1:
               self.button_case[(3,1)].setIcon(QIcon(self.data[49][1]))
               self.button_case[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[50][0])==1:
               self.button_case[(3,2)].setIcon(QIcon(self.data[50][1]))
               self.button_case[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[51][0])==1:
               self.button_case[(3,3)].setIcon(QIcon(self.data[51][1]))
               self.button_case[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[52][0])==1:
               self.button_case[(3,4)].setIcon(QIcon(self.data[52][1]))
               self.button_case[(3,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[53][0])==1:
               self.button_case[(3,5)].setIcon(QIcon(self.data[53][1]))
               self.button_case[(3,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[54][0])==1:
               self.button_case[(3,6)].setIcon(QIcon(self.data[54][1]))
               self.button_case[(3,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[55][0])==1:
               self.button_case[(3,7)].setIcon(QIcon(self.data[55][1]))
               self.button_case[(3,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[56][0])==1:
               self.button_case[(3,8)].setIcon(QIcon(self.data[56][1]))
               self.button_case[(3,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[57][0])==1:
               self.button_case[(3,9)].setIcon(QIcon(self.data[57][1]))
               self.button_case[(3,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[58][0])==1:
               self.button_case[(3,10)].setIcon(QIcon(self.data[58][1]))
               self.button_case[(3,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[59][0])==1:
               self.button_case[(3,11)].setIcon(QIcon(self.data[59][1]))
               self.button_case[(3,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[60][0])==1:
               self.button_case[(3,12)].setIcon(QIcon(self.data[60][1]))
               self.button_case[(3,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[61][0])==1:
               self.button_case[(3,13)].setIcon(QIcon(self.data[61][1]))
               self.button_case[(3,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[62][0])==1:
               self.button_case[(3,14)].setIcon(QIcon(self.data[62][1]))
               self.button_case[(3,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[63][0])==1:
               self.button_case[(3,15)].setIcon(QIcon(self.data[63][1]))
               self.button_case[(3,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 5
            if int(self.data[64][0])==1:
               self.button_case[(4,0)].setIcon(QIcon(self.data[64][1]))
               self.button_case[(4,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[65][0])==1:
               self.button_case[(4,1)].setIcon(QIcon(self.data[65][1]))
               self.button_case[(4,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[66][0])==1:
               self.button_case[(4,2)].setIcon(QIcon(self.data[66][1]))
               self.button_case[(4,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[67][0])==1:
               self.button_case[(4,3)].setIcon(QIcon(self.data[67][1]))
               self.button_case[(4,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[68][0])==1:
               self.button_case[(4,4)].setIcon(QIcon(self.data[68][1]))
               self.button_case[(4,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[69][0])==1:
               self.button_case[(4,5)].setIcon(QIcon(self.data[69][1]))
               self.button_case[(4,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[70][0])==1:
               self.button_case[(4,6)].setIcon(QIcon(self.data[70][1]))
               self.button_case[(4,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[71][0])==1:
               self.button_case[(4,7)].setIcon(QIcon(self.data[71][1]))
               self.button_case[(4,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[72][0])==1:
               self.button_case[(4,8)].setIcon(QIcon(self.data[72][1]))
               self.button_case[(4,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[73][0])==1:
               self.button_case[(4,9)].setIcon(QIcon(self.data[73][1]))
               self.button_case[(4,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[74][0])==1:
               self.button_case[(4,10)].setIcon(QIcon(self.data[74][1]))
               self.button_case[(4,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[75][0])==1:
               self.button_case[(4,11)].setIcon(QIcon(self.data[75][1]))
               self.button_case[(4,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[76][0])==1:
               self.button_case[(4,12)].setIcon(QIcon(self.data[76][1]))
               self.button_case[(4,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[77][0])==1:
               self.button_case[(4,13)].setIcon(QIcon(self.data[77][1]))
               self.button_case[(4,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[78][0])==1:
               self.button_case[(4,14)].setIcon(QIcon(self.data[78][1]))
               self.button_case[(4,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[79][0])==1:
               self.button_case[(4,15)].setIcon(QIcon(self.data[79][1]))
               self.button_case[(4,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 6
            if int(self.data[80][0])==1:
               self.button_case[(5,0)].setIcon(QIcon(self.data[80][1]))
               self.button_case[(5,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[81][0])==1:
               self.button_case[(5,1)].setIcon(QIcon(self.data[81][1]))
               self.button_case[(5,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[82][0])==1:
               self.button_case[(5,2)].setIcon(QIcon(self.data[82][1]))
               self.button_case[(5,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[83][0])==1:
               self.button_case[(5,3)].setIcon(QIcon(self.data[83][1]))
               self.button_case[(5,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[84][0])==1:
               self.button_case[(5,4)].setIcon(QIcon(self.data[84][1]))
               self.button_case[(5,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[85][0])==1:
               self.button_case[(5,5)].setIcon(QIcon(self.data[85][1]))
               self.button_case[(5,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[86][0])==1:
               self.button_case[(5,6)].setIcon(QIcon(self.data[86][1]))
               self.button_case[(5,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[87][0])==1:
               self.button_case[(5,7)].setIcon(QIcon(self.data[87][1]))
               self.button_case[(5,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[88][0])==1:
               self.button_case[(5,8)].setIcon(QIcon(self.data[88][1]))
               self.button_case[(5,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[89][0])==1:
               self.button_case[(5,9)].setIcon(QIcon(self.data[89][1]))
               self.button_case[(5,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[90][0])==1:
               self.button_case[(5,10)].setIcon(QIcon(self.data[90][1]))
               self.button_case[(5,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[91][0])==1:
               self.button_case[(5,11)].setIcon(QIcon(self.data[91][1]))
               self.button_case[(5,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[92][0])==1:
               self.button_case[(5,12)].setIcon(QIcon(self.data[92][1]))
               self.button_case[(5,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[93][0])==1:
               self.button_case[(5,13)].setIcon(QIcon(self.data[93][1]))
               self.button_case[(5,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[94][0])==1:
               self.button_case[(5,14)].setIcon(QIcon(self.data[94][1]))
               self.button_case[(5,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[95][0])==1:
               self.button_case[(5,15)].setIcon(QIcon(self.data[95][1]))
               self.button_case[(5,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 7
            if int(self.data[96][0])==1:
               self.button_case[(6,0)].setIcon(QIcon(self.data[96][1]))
               self.button_case[(6,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[97][0])==1:
               self.button_case[(6,1)].setIcon(QIcon(self.data[97][1]))
               self.button_case[(6,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[98][0])==1:
               self.button_case[(6,2)].setIcon(QIcon(self.data[98][1]))
               self.button_case[(6,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[99][0])==1:
               self.button_case[(6,3)].setIcon(QIcon(self.data[99][1]))
               self.button_case[(6,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[100][0])==1:
               self.button_case[(6,4)].setIcon(QIcon(self.data[100][1]))
               self.button_case[(6,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[101][0])==1:
               self.button_case[(6,5)].setIcon(QIcon(self.data[101][1]))
               self.button_case[(6,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[102][0])==1:
               self.button_case[(6,6)].setIcon(QIcon(self.data[102][1]))
               self.button_case[(6,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[103][0])==1:
               self.button_case[(6,7)].setIcon(QIcon(self.data[103][1]))
               self.button_case[(6,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[104][0])==1:
               self.button_case[(6,8)].setIcon(QIcon(self.data[104][1]))
               self.button_case[(6,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[105][0])==1:
               self.button_case[(6,9)].setIcon(QIcon(self.data[105][1]))
               self.button_case[(6,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[106][0])==1:
               self.button_case[(6,10)].setIcon(QIcon(self.data[106][1]))
               self.button_case[(6,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[107][0])==1:
               self.button_case[(6,11)].setIcon(QIcon(self.data[107][1]))
               self.button_case[(6,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[108][0])==1:
               self.button_case[(6,12)].setIcon(QIcon(self.data[108][1]))
               self.button_case[(6,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[109][0])==1:
               self.button_case[(6,13)].setIcon(QIcon(self.data[109][1]))
               self.button_case[(6,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[110][0])==1:
               self.button_case[(6,14)].setIcon(QIcon(self.data[110][1]))
               self.button_case[(6,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[111][0])==1:
               self.button_case[(6,15)].setIcon(QIcon(self.data[111][1]))
               self.button_case[(6,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 8
            if int(self.data[112][0])==1:
               self.button_case[(7,0)].setIcon(QIcon(self.data[112][1]))
               self.button_case[(7,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[113][0])==1:
               self.button_case[(7,1)].setIcon(QIcon(self.data[113][1]))
               self.button_case[(7,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[114][0])==1:
               self.button_case[(7,2)].setIcon(QIcon(self.data[114][1]))
               self.button_case[(7,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[115][0])==1:
               self.button_case[(7,3)].setIcon(QIcon(self.data[115][1]))
               self.button_case[(7,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[116][0])==1:
               self.button_case[(7,4)].setIcon(QIcon(self.data[116][1]))
               self.button_case[(7,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[117][0])==1:
               self.button_case[(7,5)].setIcon(QIcon(self.data[117][1]))
               self.button_case[(7,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[118][0])==1:
               self.button_case[(7,6)].setIcon(QIcon(self.data[118][1]))
               self.button_case[(7,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[119][0])==1:
               self.button_case[(7,7)].setIcon(QIcon(self.data[119][1]))
               self.button_case[(7,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[120][0])==1:
               self.button_case[(7,8)].setIcon(QIcon(self.data[120][1]))
               self.button_case[(7,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[121][0])==1:
               self.button_case[(7,9)].setIcon(QIcon(self.data[121][1]))
               self.button_case[(7,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[122][0])==1:
               self.button_case[(7,10)].setIcon(QIcon(self.data[122][1]))
               self.button_case[(7,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[123][0])==1:
               self.button_case[(7,11)].setIcon(QIcon(self.data[123][1]))
               self.button_case[(7,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[124][0])==1:
               self.button_case[(7,12)].setIcon(QIcon(self.data[124][1]))
               self.button_case[(7,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[125][0])==1:
               self.button_case[(7,13)].setIcon(QIcon(self.data[125][1]))
               self.button_case[(7,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[126][0])==1:
               self.button_case[(7,14)].setIcon(QIcon(self.data[126][1]))
               self.button_case[(7,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[127][0])==1:
               self.button_case[(7,15)].setIcon(QIcon(self.data[127][1]))
               self.button_case[(7,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 9
            if int(self.data[128][0])==1:
               self.button_case[(8,0)].setIcon(QIcon(self.data[128][1]))
               self.button_case[(8,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[129][0])==1:
               self.button_case[(8,1)].setIcon(QIcon(self.data[129][1]))
               self.button_case[(8,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[130][0])==1:
               self.button_case[(8,2)].setIcon(QIcon(self.data[130][1]))
               self.button_case[(8,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[131][0])==1:
               self.button_case[(8,3)].setIcon(QIcon(self.data[131][1]))
               self.button_case[(8,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[132][0])==1:
               self.button_case[(8,4)].setIcon(QIcon(self.data[132][1]))
               self.button_case[(8,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[133][0])==1:
               self.button_case[(8,5)].setIcon(QIcon(self.data[133][1]))
               self.button_case[(8,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[134][0])==1:
               self.button_case[(8,6)].setIcon(QIcon(self.data[134][1]))
               self.button_case[(8,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[135][0])==1:
               self.button_case[(8,7)].setIcon(QIcon(self.data[135][1]))
               self.button_case[(8,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[136][0])==1:
               self.button_case[(8,8)].setIcon(QIcon(self.data[136][1]))
               self.button_case[(8,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[137][0])==1:
               self.button_case[(8,9)].setIcon(QIcon(self.data[137][1]))
               self.button_case[(8,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[138][0])==1:
               self.button_case[(8,10)].setIcon(QIcon(self.data[138][1]))
               self.button_case[(8,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[139][0])==1:
               self.button_case[(8,11)].setIcon(QIcon(self.data[139][1]))
               self.button_case[(8,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[140][0])==1:
               self.button_case[(8,12)].setIcon(QIcon(self.data[140][1]))
               self.button_case[(8,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[141][0])==1:
               self.button_case[(8,13)].setIcon(QIcon(self.data[141][1]))
               self.button_case[(8,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[142][0])==1:
               self.button_case[(8,14)].setIcon(QIcon(self.data[142][1]))
               self.button_case[(8,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[143][0])==1:
               self.button_case[(8,15)].setIcon(QIcon(self.data[143][1]))
               self.button_case[(8,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 10
            if int(self.data[144][0])==1:
               self.button_case[(9,0)].setIcon(QIcon(self.data[144][1]))
               self.button_case[(9,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[145][0])==1:
               self.button_case[(9,1)].setIcon(QIcon(self.data[145][1]))
               self.button_case[(9,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[146][0])==1:
               self.button_case[(9,2)].setIcon(QIcon(self.data[146][1]))
               self.button_case[(9,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[147][0])==1:
               self.button_case[(9,3)].setIcon(QIcon(self.data[147][1]))
               self.button_case[(9,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[148][0])==1:
               self.button_case[(9,4)].setIcon(QIcon(self.data[148][1]))
               self.button_case[(9,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[149][0])==1:
               self.button_case[(9,5)].setIcon(QIcon(self.data[149][1]))
               self.button_case[(9,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[150][0])==1:
               self.button_case[(9,6)].setIcon(QIcon(self.data[150][1]))
               self.button_case[(9,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[151][0])==1:
               self.button_case[(9,7)].setIcon(QIcon(self.data[151][1]))
               self.button_case[(9,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[152][0])==1:
               self.button_case[(9,8)].setIcon(QIcon(self.data[152][1]))
               self.button_case[(9,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[153][0])==1:
               self.button_case[(9,9)].setIcon(QIcon(self.data[153][1]))
               self.button_case[(9,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[154][0])==1:
               self.button_case[(9,10)].setIcon(QIcon(self.data[154][1]))
               self.button_case[(9,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[155][0])==1:
               self.button_case[(9,11)].setIcon(QIcon(self.data[155][1]))
               self.button_case[(9,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[156][0])==1:
               self.button_case[(9,12)].setIcon(QIcon(self.data[156][1]))
               self.button_case[(9,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[157][0])==1:
               self.button_case[(9,13)].setIcon(QIcon(self.data[157][1]))
               self.button_case[(9,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[158][0])==1:
               self.button_case[(9,14)].setIcon(QIcon(self.data[158][1]))
               self.button_case[(9,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[159][0])==1:
               self.button_case[(9,15)].setIcon(QIcon(self.data[159][1]))
               self.button_case[(9,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 11
            if int(self.data[160][0])==1:
               self.button_case[(10,0)].setIcon(QIcon(self.data[160][1]))
               self.button_case[(10,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[161][0])==1:
               self.button_case[(10,1)].setIcon(QIcon(self.data[161][1]))
               self.button_case[(10,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[162][0])==1:
               self.button_case[(10,2)].setIcon(QIcon(self.data[162][1]))
               self.button_case[(10,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[163][0])==1:
               self.button_case[(10,3)].setIcon(QIcon(self.data[163][1]))
               self.button_case[(10,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[164][0])==1:
               self.button_case[(10,4)].setIcon(QIcon(self.data[164][1]))
               self.button_case[(10,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[165][0])==1:
               self.button_case[(10,5)].setIcon(QIcon(self.data[165][1]))
               self.button_case[(10,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[166][0])==1:
               self.button_case[(10,6)].setIcon(QIcon(self.data[166][1]))
               self.button_case[(10,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[167][0])==1:
               self.button_case[(10,7)].setIcon(QIcon(self.data[167][1]))
               self.button_case[(10,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[168][0])==1:
               self.button_case[(10,8)].setIcon(QIcon(self.data[168][1]))
               self.button_case[(10,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[169][0])==1:
               self.button_case[(10,9)].setIcon(QIcon(self.data[169][1]))
               self.button_case[(10,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[170][0])==1:
               self.button_case[(10,10)].setIcon(QIcon(self.data[170][1]))
               self.button_case[(10,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[171][0])==1:
               self.button_case[(10,11)].setIcon(QIcon(self.data[171][1]))
               self.button_case[(10,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[172][0])==1:
               self.button_case[(10,12)].setIcon(QIcon(self.data[172][1]))
               self.button_case[(10,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[173][0])==1:
               self.button_case[(10,13)].setIcon(QIcon(self.data[173][1]))
               self.button_case[(10,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[174][0])==1:
               self.button_case[(10,14)].setIcon(QIcon(self.data[174][1]))
               self.button_case[(10,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[175][0])==1:
               self.button_case[(10,15)].setIcon(QIcon(self.data[175][1]))
               self.button_case[(10,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 12
            if int(self.data[176][0])==1:
               self.button_case[(11,0)].setIcon(QIcon(self.data[176][1]))
               self.button_case[(11,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[177][0])==1:
               self.button_case[(11,1)].setIcon(QIcon(self.data[177][1]))
               self.button_case[(11,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[178][0])==1:
               self.button_case[(11,2)].setIcon(QIcon(self.data[178][1]))
               self.button_case[(11,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[179][0])==1:
               self.button_case[(11,3)].setIcon(QIcon(self.data[179][1]))
               self.button_case[(11,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[180][0])==1:
               self.button_case[(11,4)].setIcon(QIcon(self.data[180][1]))
               self.button_case[(11,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[181][0])==1:
               self.button_case[(11,5)].setIcon(QIcon(self.data[181][1]))
               self.button_case[(11,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[182][0])==1:
               self.button_case[(11,6)].setIcon(QIcon(self.data[182][1]))
               self.button_case[(11,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[183][0])==1:
               self.button_case[(11,7)].setIcon(QIcon(self.data[183][1]))
               self.button_case[(11,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[184][0])==1:
               self.button_case[(11,8)].setIcon(QIcon(self.data[184][1]))
               self.button_case[(11,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[185][0])==1:
               self.button_case[(11,9)].setIcon(QIcon(self.data[185][1]))
               self.button_case[(11,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[186][0])==1:
               self.button_case[(11,10)].setIcon(QIcon(self.data[186][1]))
               self.button_case[(11,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[187][0])==1:
               self.button_case[(11,11)].setIcon(QIcon(self.data[187][1]))
               self.button_case[(11,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[188][0])==1:
               self.button_case[(11,12)].setIcon(QIcon(self.data[188][1]))
               self.button_case[(11,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[189][0])==1:
               self.button_case[(11,13)].setIcon(QIcon(self.data[189][1]))
               self.button_case[(11,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[190][0])==1:
               self.button_case[(11,14)].setIcon(QIcon(self.data[190][1]))
               self.button_case[(11,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[191][0])==1:
               self.button_case[(11,15)].setIcon(QIcon(self.data[191][1]))
               self.button_case[(11,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 13
            if int(self.data[192][0])==1:
               self.button_case[(12,0)].setIcon(QIcon(self.data[192][1]))
               self.button_case[(12,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[193][0])==1:
               self.button_case[(12,1)].setIcon(QIcon(self.data[193][1]))
               self.button_case[(12,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[194][0])==1:
               self.button_case[(12,2)].setIcon(QIcon(self.data[194][1]))
               self.button_case[(12,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[195][0])==1:
               self.button_case[(12,3)].setIcon(QIcon(self.data[195][1]))
               self.button_case[(12,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[196][0])==1:
               self.button_case[(12,4)].setIcon(QIcon(self.data[196][1]))
               self.button_case[(12,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[197][0])==1:
               self.button_case[(12,5)].setIcon(QIcon(self.data[197][1]))
               self.button_case[(12,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[198][0])==1:
               self.button_case[(12,6)].setIcon(QIcon(self.data[198][1]))
               self.button_case[(12,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[199][0])==1:
               self.button_case[(12,7)].setIcon(QIcon(self.data[199][1]))
               self.button_case[(12,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[200][0])==1:
               self.button_case[(12,8)].setIcon(QIcon(self.data[200][1]))
               self.button_case[(12,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[201][0])==1:
               self.button_case[(12,9)].setIcon(QIcon(self.data[201][1]))
               self.button_case[(12,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[202][0])==1:
               self.button_case[(12,10)].setIcon(QIcon(self.data[202][1]))
               self.button_case[(12,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[203][0])==1:
               self.button_case[(12,11)].setIcon(QIcon(self.data[203][1]))
               self.button_case[(12,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[204][0])==1:
               self.button_case[(12,12)].setIcon(QIcon(self.data[204][1]))
               self.button_case[(12,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[205][0])==1:
               self.button_case[(12,13)].setIcon(QIcon(self.data[205][1]))
               self.button_case[(12,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[206][0])==1:
               self.button_case[(12,14)].setIcon(QIcon(self.data[206][1]))
               self.button_case[(12,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[207][0])==1:
               self.button_case[(12,15)].setIcon(QIcon(self.data[207][1]))
               self.button_case[(12,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 14
            if int(self.data[208][0])==1:
               self.button_case[(13,0)].setIcon(QIcon(self.data[208][1]))
               self.button_case[(13,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[209][0])==1:
               self.button_case[(13,1)].setIcon(QIcon(self.data[209][1]))
               self.button_case[(13,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[210][0])==1:
               self.button_case[(13,2)].setIcon(QIcon(self.data[210][1]))
               self.button_case[(13,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[211][0])==1:
               self.button_case[(13,3)].setIcon(QIcon(self.data[211][1]))
               self.button_case[(13,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[212][0])==1:
               self.button_case[(13,4)].setIcon(QIcon(self.data[212][1]))
               self.button_case[(13,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[213][0])==1:
               self.button_case[(13,5)].setIcon(QIcon(self.data[213][1]))
               self.button_case[(13,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[214][0])==1:
               self.button_case[(13,6)].setIcon(QIcon(self.data[214][1]))
               self.button_case[(13,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[215][0])==1:
               self.button_case[(13,7)].setIcon(QIcon(self.data[215][1]))
               self.button_case[(13,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[216][0])==1:
               self.button_case[(13,8)].setIcon(QIcon(self.data[216][1]))
               self.button_case[(13,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[217][0])==1:
               self.button_case[(13,9)].setIcon(QIcon(self.data[217][1]))
               self.button_case[(13,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[218][0])==1:
               self.button_case[(13,10)].setIcon(QIcon(self.data[218][1]))
               self.button_case[(13,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[219][0])==1:
               self.button_case[(13,11)].setIcon(QIcon(self.data[219][1]))
               self.button_case[(13,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[220][0])==1:
               self.button_case[(13,12)].setIcon(QIcon(self.data[220][1]))
               self.button_case[(13,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[221][0])==1:
               self.button_case[(13,13)].setIcon(QIcon(self.data[221][1]))
               self.button_case[(13,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[222][0])==1:
               self.button_case[(13,14)].setIcon(QIcon(self.data[222][1]))
               self.button_case[(13,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[223][0])==1:
               self.button_case[(13,15)].setIcon(QIcon(self.data[223][1]))
               self.button_case[(13,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 15
            if int(self.data[224][0])==1:
               self.button_case[(14,0)].setIcon(QIcon(self.data[224][1]))
               self.button_case[(14,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[225][0])==1:
               self.button_case[(14,1)].setIcon(QIcon(self.data[225][1]))
               self.button_case[(14,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[226][0])==1:
               self.button_case[(14,2)].setIcon(QIcon(self.data[226][1]))
               self.button_case[(14,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[227][0])==1:
               self.button_case[(14,3)].setIcon(QIcon(self.data[227][1]))
               self.button_case[(14,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[228][0])==1:
               self.button_case[(14,4)].setIcon(QIcon(self.data[228][1]))
               self.button_case[(14,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[229][0])==1:
               self.button_case[(14,5)].setIcon(QIcon(self.data[229][1]))
               self.button_case[(14,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[230][0])==1:
               self.button_case[(14,6)].setIcon(QIcon(self.data[230][1]))
               self.button_case[(14,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[231][0])==1:
               self.button_case[(14,7)].setIcon(QIcon(self.data[231][1]))
               self.button_case[(14,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[232][0])==1:
               self.button_case[(14,8)].setIcon(QIcon(self.data[232][1]))
               self.button_case[(14,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[233][0])==1:
               self.button_case[(14,9)].setIcon(QIcon(self.data[233][1]))
               self.button_case[(14,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[234][0])==1:
               self.button_case[(14,10)].setIcon(QIcon(self.data[234][1]))
               self.button_case[(14,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[235][0])==1:
               self.button_case[(14,11)].setIcon(QIcon(self.data[235][1]))
               self.button_case[(14,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[236][0])==1:
               self.button_case[(14,12)].setIcon(QIcon(self.data[236][1]))
               self.button_case[(14,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[237][0])==1:
               self.button_case[(14,13)].setIcon(QIcon(self.data[237][1]))
               self.button_case[(14,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[238][0])==1:
               self.button_case[(14,14)].setIcon(QIcon(self.data[238][1]))
               self.button_case[(14,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[239][0])==1:
               self.button_case[(14,15)].setIcon(QIcon(self.data[239][1]))
               self.button_case[(14,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 16
            if int(self.data[240][0])==1:
               self.button_case[(15,0)].setIcon(QIcon(self.data[240][1]))
               self.button_case[(15,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[241][0])==1:
               self.button_case[(15,1)].setIcon(QIcon(self.data[241][1]))
               self.button_case[(15,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[242][0])==1:
               self.button_case[(15,2)].setIcon(QIcon(self.data[242][1]))
               self.button_case[(15,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[243][0])==1:
               self.button_case[(15,3)].setIcon(QIcon(self.data[243][1]))
               self.button_case[(15,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[244][0])==1:
               self.button_case[(15,4)].setIcon(QIcon(self.data[244][1]))
               self.button_case[(15,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[245][0])==1:
               self.button_case[(15,5)].setIcon(QIcon(self.data[245][1]))
               self.button_case[(15,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[246][0])==1:
               self.button_case[(15,6)].setIcon(QIcon(self.data[246][1]))
               self.button_case[(15,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[247][0])==1:
               self.button_case[(15,7)].setIcon(QIcon(self.data[247][1]))
               self.button_case[(15,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[248][0])==1:
               self.button_case[(15,8)].setIcon(QIcon(self.data[248][1]))
               self.button_case[(15,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[249][0])==1:
               self.button_case[(15,9)].setIcon(QIcon(self.data[249][1]))
               self.button_case[(15,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[250][0])==1:
               self.button_case[(15,10)].setIcon(QIcon(self.data[250][1]))
               self.button_case[(15,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[251][0])==1:
               self.button_case[(15,11)].setIcon(QIcon(self.data[251][1]))
               self.button_case[(15,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[252][0])==1:
               self.button_case[(15,12)].setIcon(QIcon(self.data[252][1]))
               self.button_case[(15,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[253][0])==1:
               self.button_case[(15,13)].setIcon(QIcon(self.data[253][1]))
               self.button_case[(15,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[254][0])==1:
               self.button_case[(15,14)].setIcon(QIcon(self.data[254][1]))
               self.button_case[(15,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[255][0])==1:
               self.button_case[(15,15)].setIcon(QIcon(self.data[255][1]))
               self.button_case[(15,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 1
            if int(self.data[0][0])==2:
               self.button_case[(0,0)].setIcon(QIcon(self.data[0][1]))
               self.button_case[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[1][0])==2:
               self.button_case[(0,1)].setIcon(QIcon(self.data[1][1]))
               self.button_case[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[2][0])==2:
               self.button_case[(0,2)].setIcon(QIcon(self.data[2][1]))
               self.button_case[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[3][0])==2:
               self.button_case[(0,3)].setIcon(QIcon(self.data[3][1]))
               self.button_case[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[4][0])==2:
               self.button_case[(0,4)].setIcon(QIcon(self.data[4][1]))
               self.button_case[(0,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[5][0])==2:
               self.button_case[(0,5)].setIcon(QIcon(self.data[5][1]))
               self.button_case[(0,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[6][0])==2:
               self.button_case[(0,6)].setIcon(QIcon(self.data[6][1]))
               self.button_case[(0,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[7][0])==2:
               self.button_case[(0,7)].setIcon(QIcon(self.data[7][1]))
               self.button_case[(0,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[8][0])==2:
               self.button_case[(0,8)].setIcon(QIcon(self.data[8][1]))
               self.button_case[(0,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[9][0])==2:
               self.button_case[(0,9)].setIcon(QIcon(self.data[9][1]))
               self.button_case[(0,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[10][0])==2:
               self.button_case[(0,10)].setIcon(QIcon(self.data[10][1]))
               self.button_case[(0,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[11][0])==2:
               self.button_case[(0,11)].setIcon(QIcon(self.data[11][1]))
               self.button_case[(0,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[12][0])==2:
               self.button_case[(0,12)].setIcon(QIcon(self.data[12][1]))
               self.button_case[(0,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[13][0])==2:
               self.button_case[(0,13)].setIcon(QIcon(self.data[13][1]))
               self.button_case[(0,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[14][0])==2:
               self.button_case[(0,14)].setIcon(QIcon(self.data[14][1]))
               self.button_case[(0,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[15][0])==2:
               self.button_case[(0,15)].setIcon(QIcon(self.data[15][1]))
               self.button_case[(0,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 2
            if int(self.data[16][0])==2:
               self.button_case[(1,0)].setIcon(QIcon(self.data[16][1]))
               self.button_case[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[17][0])==2:
               self.button_case[(1,1)].setIcon(QIcon(self.data[17][1]))
               self.button_case[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[18][0])==2:
               self.button_case[(1,2)].setIcon(QIcon(self.data[18][1]))
               self.button_case[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[19][0])==2:
               self.button_case[(1,3)].setIcon(QIcon(self.data[19][1]))
               self.button_case[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[20][0])==2:
               self.button_case[(1,4)].setIcon(QIcon(self.data[20][1]))
               self.button_case[(1,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[21][0])==2:
               self.button_case[(1,5)].setIcon(QIcon(self.data[21][1]))
               self.button_case[(1,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[22][0])==2:
               self.button_case[(1,6)].setIcon(QIcon(self.data[22][1]))
               self.button_case[(1,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[23][0])==2:
               self.button_case[(1,7)].setIcon(QIcon(self.data[23][1]))
               self.button_case[(1,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[24][0])==2:
               self.button_case[(1,8)].setIcon(QIcon(self.data[24][1]))
               self.button_case[(1,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[25][0])==2:
               self.button_case[(1,9)].setIcon(QIcon(self.data[25][1]))
               self.button_case[(1,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[26][0])==2:
               self.button_case[(1,10)].setIcon(QIcon(self.data[26][1]))
               self.button_case[(1,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[27][0])==2:
               self.button_case[(1,11)].setIcon(QIcon(self.data[27][1]))
               self.button_case[(1,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[28][0])==2:
               self.button_case[(1,12)].setIcon(QIcon(self.data[28][1]))
               self.button_case[(1,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[29][0])==2:
               self.button_case[(1,13)].setIcon(QIcon(self.data[29][1]))
               self.button_case[(1,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[30][0])==2:
               self.button_case[(1,14)].setIcon(QIcon(self.data[30][1]))
               self.button_case[(1,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[31][0])==2:
               self.button_case[(1,15)].setIcon(QIcon(self.data[31][1]))
               self.button_case[(1,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 3
            if int(self.data[32][0])==2:
               self.button_case[(2,0)].setIcon(QIcon(self.data[32][1]))
               self.button_case[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[33][0])==2:
               self.button_case[(2,1)].setIcon(QIcon(self.data[33][1]))
               self.button_case[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[34][0])==2:
               self.button_case[(2,2)].setIcon(QIcon(self.data[34][1]))
               self.button_case[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[35][0])==2:
               self.button_case[(2,3)].setIcon(QIcon(self.data[35][1]))
               self.button_case[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[36][0])==2:
               self.button_case[(2,4)].setIcon(QIcon(self.data[36][1]))
               self.button_case[(2,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[37][0])==2:
               self.button_case[(2,5)].setIcon(QIcon(self.data[37][1]))
               self.button_case[(2,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[38][0])==2:
               self.button_case[(2,6)].setIcon(QIcon(self.data[38][1]))
               self.button_case[(2,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[39][0])==2:
               self.button_case[(2,7)].setIcon(QIcon(self.data[39][1]))
               self.button_case[(2,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[40][0])==2:
               self.button_case[(2,8)].setIcon(QIcon(self.data[40][1]))
               self.button_case[(2,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[41][0])==2:
               self.button_case[(2,9)].setIcon(QIcon(self.data[41][1]))
               self.button_case[(2,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[42][0])==2:
               self.button_case[(2,10)].setIcon(QIcon(self.data[42][1]))
               self.button_case[(2,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[43][0])==2:
               self.button_case[(2,11)].setIcon(QIcon(self.data[43][1]))
               self.button_case[(2,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[44][0])==2:
               self.button_case[(2,12)].setIcon(QIcon(self.data[44][1]))
               self.button_case[(2,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[45][0])==2:
               self.button_case[(2,13)].setIcon(QIcon(self.data[45][1]))
               self.button_case[(2,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[46][0])==2:
               self.button_case[(2,14)].setIcon(QIcon(self.data[46][1]))
               self.button_case[(2,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[47][0])==2:
               self.button_case[(2,15)].setIcon(QIcon(self.data[47][1]))
               self.button_case[(2,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 4
            if int(self.data[48][0])==2:
               self.button_case[(3,0)].setIcon(QIcon(self.data[48][1]))
               self.button_case[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[49][0])==2:
               self.button_case[(3,1)].setIcon(QIcon(self.data[49][1]))
               self.button_case[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[50][0])==2:
               self.button_case[(3,2)].setIcon(QIcon(self.data[50][1]))
               self.button_case[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[51][0])==2:
               self.button_case[(3,3)].setIcon(QIcon(self.data[51][1]))
               self.button_case[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[52][0])==2:
               self.button_case[(3,4)].setIcon(QIcon(self.data[52][1]))
               self.button_case[(3,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[53][0])==2:
               self.button_case[(3,5)].setIcon(QIcon(self.data[53][1]))
               self.button_case[(3,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[54][0])==2:
               self.button_case[(3,6)].setIcon(QIcon(self.data[54][1]))
               self.button_case[(3,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[55][0])==2:
               self.button_case[(3,7)].setIcon(QIcon(self.data[55][1]))
               self.button_case[(3,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[56][0])==2:
               self.button_case[(3,8)].setIcon(QIcon(self.data[56][1]))
               self.button_case[(3,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[57][0])==2:
               self.button_case[(3,9)].setIcon(QIcon(self.data[57][1]))
               self.button_case[(3,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[58][0])==2:
               self.button_case[(3,10)].setIcon(QIcon(self.data[58][1]))
               self.button_case[(3,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[59][0])==2:
               self.button_case[(3,11)].setIcon(QIcon(self.data[59][1]))
               self.button_case[(3,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[60][0])==2:
               self.button_case[(3,12)].setIcon(QIcon(self.data[60][1]))
               self.button_case[(3,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[61][0])==2:
               self.button_case[(3,13)].setIcon(QIcon(self.data[61][1]))
               self.button_case[(3,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[62][0])==2:
               self.button_case[(3,14)].setIcon(QIcon(self.data[62][1]))
               self.button_case[(3,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[63][0])==2:
               self.button_case[(3,15)].setIcon(QIcon(self.data[63][1]))
               self.button_case[(3,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 5
            if int(self.data[64][0])==2:
               self.button_case[(4,0)].setIcon(QIcon(self.data[64][1]))
               self.button_case[(4,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[65][0])==2:
               self.button_case[(4,1)].setIcon(QIcon(self.data[65][1]))
               self.button_case[(4,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[66][0])==2:
               self.button_case[(4,2)].setIcon(QIcon(self.data[66][1]))
               self.button_case[(4,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[67][0])==2:
               self.button_case[(4,3)].setIcon(QIcon(self.data[67][1]))
               self.button_case[(4,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[68][0])==2:
               self.button_case[(4,4)].setIcon(QIcon(self.data[68][1]))
               self.button_case[(4,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[69][0])==2:
               self.button_case[(4,5)].setIcon(QIcon(self.data[69][1]))
               self.button_case[(4,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[70][0])==2:
               self.button_case[(4,6)].setIcon(QIcon(self.data[70][1]))
               self.button_case[(4,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[71][0])==2:
               self.button_case[(4,7)].setIcon(QIcon(self.data[71][1]))
               self.button_case[(4,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[72][0])==2:
               self.button_case[(4,8)].setIcon(QIcon(self.data[72][1]))
               self.button_case[(4,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[73][0])==2:
               self.button_case[(4,9)].setIcon(QIcon(self.data[73][1]))
               self.button_case[(4,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[74][0])==2:
               self.button_case[(4,10)].setIcon(QIcon(self.data[74][1]))
               self.button_case[(4,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[75][0])==2:
               self.button_case[(4,11)].setIcon(QIcon(self.data[75][1]))
               self.button_case[(4,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[76][0])==2:
               self.button_case[(4,12)].setIcon(QIcon(self.data[76][1]))
               self.button_case[(4,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[77][0])==2:
               self.button_case[(4,13)].setIcon(QIcon(self.data[77][1]))
               self.button_case[(4,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[78][0])==2:
               self.button_case[(4,14)].setIcon(QIcon(self.data[78][1]))
               self.button_case[(4,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[79][0])==2:
               self.button_case[(4,15)].setIcon(QIcon(self.data[79][1]))
               self.button_case[(4,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 6
            if int(self.data[80][0])==2:
               self.button_case[(5,0)].setIcon(QIcon(self.data[80][1]))
               self.button_case[(5,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[81][0])==2:
               self.button_case[(5,1)].setIcon(QIcon(self.data[81][1]))
               self.button_case[(5,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[82][0])==2:
               self.button_case[(5,2)].setIcon(QIcon(self.data[82][1]))
               self.button_case[(5,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[83][0])==2:
               self.button_case[(5,3)].setIcon(QIcon(self.data[83][1]))
               self.button_case[(5,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[84][0])==2:
               self.button_case[(5,4)].setIcon(QIcon(self.data[84][1]))
               self.button_case[(5,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[85][0])==2:
               self.button_case[(5,5)].setIcon(QIcon(self.data[85][1]))
               self.button_case[(5,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[86][0])==2:
               self.button_case[(5,6)].setIcon(QIcon(self.data[86][1]))
               self.button_case[(5,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[87][0])==2:
               self.button_case[(5,7)].setIcon(QIcon(self.data[87][1]))
               self.button_case[(5,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[88][0])==2:
               self.button_case[(5,8)].setIcon(QIcon(self.data[88][1]))
               self.button_case[(5,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[89][0])==2:
               self.button_case[(5,9)].setIcon(QIcon(self.data[89][1]))
               self.button_case[(5,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[90][0])==2:
               self.button_case[(5,10)].setIcon(QIcon(self.data[90][1]))
               self.button_case[(5,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[91][0])==2:
               self.button_case[(5,11)].setIcon(QIcon(self.data[91][1]))
               self.button_case[(5,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[92][0])==2:
               self.button_case[(5,12)].setIcon(QIcon(self.data[92][1]))
               self.button_case[(5,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[93][0])==2:
               self.button_case[(5,13)].setIcon(QIcon(self.data[93][1]))
               self.button_case[(5,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[94][0])==2:
               self.button_case[(5,14)].setIcon(QIcon(self.data[94][1]))
               self.button_case[(5,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[95][0])==2:
               self.button_case[(5,15)].setIcon(QIcon(self.data[95][1]))
               self.button_case[(5,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 7
            if int(self.data[96][0])==2:
               self.button_case[(6,0)].setIcon(QIcon(self.data[96][1]))
               self.button_case[(6,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[97][0])==2:
               self.button_case[(6,1)].setIcon(QIcon(self.data[97][1]))
               self.button_case[(6,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[98][0])==2:
               self.button_case[(6,2)].setIcon(QIcon(self.data[98][1]))
               self.button_case[(6,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[99][0])==2:
               self.button_case[(6,3)].setIcon(QIcon(self.data[99][1]))
               self.button_case[(6,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[100][0])==2:
               self.button_case[(6,4)].setIcon(QIcon(self.data[100][1]))
               self.button_case[(6,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[101][0])==2:
               self.button_case[(6,5)].setIcon(QIcon(self.data[101][1]))
               self.button_case[(6,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[102][0])==2:
               self.button_case[(6,6)].setIcon(QIcon(self.data[102][1]))
               self.button_case[(6,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[103][0])==2:
               self.button_case[(6,7)].setIcon(QIcon(self.data[103][1]))
               self.button_case[(6,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[104][0])==2:
               self.button_case[(6,8)].setIcon(QIcon(self.data[104][1]))
               self.button_case[(6,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[105][0])==2:
               self.button_case[(6,9)].setIcon(QIcon(self.data[105][1]))
               self.button_case[(6,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[106][0])==2:
               self.button_case[(6,10)].setIcon(QIcon(self.data[106][1]))
               self.button_case[(6,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[107][0])==2:
               self.button_case[(6,11)].setIcon(QIcon(self.data[107][1]))
               self.button_case[(6,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[108][0])==2:
               self.button_case[(6,12)].setIcon(QIcon(self.data[108][1]))
               self.button_case[(6,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[109][0])==2:
               self.button_case[(6,13)].setIcon(QIcon(self.data[109][1]))
               self.button_case[(6,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[110][0])==2:
               self.button_case[(6,14)].setIcon(QIcon(self.data[110][1]))
               self.button_case[(6,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[111][0])==2:
               self.button_case[(6,15)].setIcon(QIcon(self.data[111][1]))
               self.button_case[(6,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 8
            if int(self.data[112][0])==2:
               self.button_case[(7,0)].setIcon(QIcon(self.data[112][1]))
               self.button_case[(7,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[113][0])==2:
               self.button_case[(7,1)].setIcon(QIcon(self.data[113][1]))
               self.button_case[(7,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[114][0])==2:
               self.button_case[(7,2)].setIcon(QIcon(self.data[114][1]))
               self.button_case[(7,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[115][0])==2:
               self.button_case[(7,3)].setIcon(QIcon(self.data[115][1]))
               self.button_case[(7,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[116][0])==2:
               self.button_case[(7,4)].setIcon(QIcon(self.data[116][1]))
               self.button_case[(7,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[117][0])==2:
               self.button_case[(7,5)].setIcon(QIcon(self.data[117][1]))
               self.button_case[(7,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[118][0])==2:
               self.button_case[(7,6)].setIcon(QIcon(self.data[118][1]))
               self.button_case[(7,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[119][0])==2:
               self.button_case[(7,7)].setIcon(QIcon(self.data[119][1]))
               self.button_case[(7,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[120][0])==2:
               self.button_case[(7,8)].setIcon(QIcon(self.data[120][1]))
               self.button_case[(7,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[121][0])==2:
               self.button_case[(7,9)].setIcon(QIcon(self.data[121][1]))
               self.button_case[(7,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[122][0])==2:
               self.button_case[(7,10)].setIcon(QIcon(self.data[122][1]))
               self.button_case[(7,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[123][0])==2:
               self.button_case[(7,11)].setIcon(QIcon(self.data[123][1]))
               self.button_case[(7,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[124][0])==2:
               self.button_case[(7,12)].setIcon(QIcon(self.data[124][1]))
               self.button_case[(7,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[125][0])==2:
               self.button_case[(7,13)].setIcon(QIcon(self.data[125][1]))
               self.button_case[(7,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[126][0])==2:
               self.button_case[(7,14)].setIcon(QIcon(self.data[126][1]))
               self.button_case[(7,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[127][0])==2:
               self.button_case[(7,15)].setIcon(QIcon(self.data[127][1]))
               self.button_case[(7,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 9
            if int(self.data[128][0])==2:
               self.button_case[(8,0)].setIcon(QIcon(self.data[128][1]))
               self.button_case[(8,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[129][0])==2:
               self.button_case[(8,1)].setIcon(QIcon(self.data[129][1]))
               self.button_case[(8,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[130][0])==2:
               self.button_case[(8,2)].setIcon(QIcon(self.data[130][1]))
               self.button_case[(8,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[131][0])==2:
               self.button_case[(8,3)].setIcon(QIcon(self.data[131][1]))
               self.button_case[(8,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[132][0])==2:
               self.button_case[(8,4)].setIcon(QIcon(self.data[132][1]))
               self.button_case[(8,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[133][0])==2:
               self.button_case[(8,5)].setIcon(QIcon(self.data[133][1]))
               self.button_case[(8,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[134][0])==2:
               self.button_case[(8,6)].setIcon(QIcon(self.data[134][1]))
               self.button_case[(8,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[135][0])==2:
               self.button_case[(8,7)].setIcon(QIcon(self.data[135][1]))
               self.button_case[(8,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[136][0])==2:
               self.button_case[(8,8)].setIcon(QIcon(self.data[136][1]))
               self.button_case[(8,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[137][0])==2:
               self.button_case[(8,9)].setIcon(QIcon(self.data[137][1]))
               self.button_case[(8,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[138][0])==2:
               self.button_case[(8,10)].setIcon(QIcon(self.data[138][1]))
               self.button_case[(8,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[139][0])==2:
               self.button_case[(8,11)].setIcon(QIcon(self.data[139][1]))
               self.button_case[(8,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[140][0])==2:
               self.button_case[(8,12)].setIcon(QIcon(self.data[140][1]))
               self.button_case[(8,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[141][0])==2:
               self.button_case[(8,13)].setIcon(QIcon(self.data[141][1]))
               self.button_case[(8,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[142][0])==2:
               self.button_case[(8,14)].setIcon(QIcon(self.data[142][1]))
               self.button_case[(8,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[143][0])==2:
               self.button_case[(8,15)].setIcon(QIcon(self.data[143][1]))
               self.button_case[(8,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 10
            if int(self.data[144][0])==2:
               self.button_case[(9,0)].setIcon(QIcon(self.data[144][1]))
               self.button_case[(9,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[145][0])==2:
               self.button_case[(9,1)].setIcon(QIcon(self.data[145][1]))
               self.button_case[(9,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[146][0])==2:
               self.button_case[(9,2)].setIcon(QIcon(self.data[146][1]))
               self.button_case[(9,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[147][0])==2:
               self.button_case[(9,3)].setIcon(QIcon(self.data[147][1]))
               self.button_case[(9,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[148][0])==2:
               self.button_case[(9,4)].setIcon(QIcon(self.data[148][1]))
               self.button_case[(9,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[149][0])==2:
               self.button_case[(9,5)].setIcon(QIcon(self.data[149][1]))
               self.button_case[(9,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[150][0])==2:
               self.button_case[(9,6)].setIcon(QIcon(self.data[150][1]))
               self.button_case[(9,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[151][0])==2:
               self.button_case[(9,7)].setIcon(QIcon(self.data[151][1]))
               self.button_case[(9,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[152][0])==2:
               self.button_case[(9,8)].setIcon(QIcon(self.data[152][1]))
               self.button_case[(9,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[153][0])==2:
               self.button_case[(9,9)].setIcon(QIcon(self.data[153][1]))
               self.button_case[(9,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[154][0])==2:
               self.button_case[(9,10)].setIcon(QIcon(self.data[154][1]))
               self.button_case[(9,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[155][0])==2:
               self.button_case[(9,11)].setIcon(QIcon(self.data[155][1]))
               self.button_case[(9,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[156][0])==2:
               self.button_case[(9,12)].setIcon(QIcon(self.data[156][1]))
               self.button_case[(9,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[157][0])==2:
               self.button_case[(9,13)].setIcon(QIcon(self.data[157][1]))
               self.button_case[(9,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[158][0])==2:
               self.button_case[(9,14)].setIcon(QIcon(self.data[158][1]))
               self.button_case[(9,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[159][0])==2:
               self.button_case[(9,15)].setIcon(QIcon(self.data[159][1]))
               self.button_case[(9,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 11
            if int(self.data[160][0])==2:
               self.button_case[(10,0)].setIcon(QIcon(self.data[160][1]))
               self.button_case[(10,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[161][0])==2:
               self.button_case[(10,1)].setIcon(QIcon(self.data[161][1]))
               self.button_case[(10,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[162][0])==2:
               self.button_case[(10,2)].setIcon(QIcon(self.data[162][1]))
               self.button_case[(10,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[163][0])==2:
               self.button_case[(10,3)].setIcon(QIcon(self.data[163][1]))
               self.button_case[(10,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[164][0])==2:
               self.button_case[(10,4)].setIcon(QIcon(self.data[164][1]))
               self.button_case[(10,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[165][0])==2:
               self.button_case[(10,5)].setIcon(QIcon(self.data[165][1]))
               self.button_case[(10,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[166][0])==2:
               self.button_case[(10,6)].setIcon(QIcon(self.data[166][1]))
               self.button_case[(10,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[167][0])==2:
               self.button_case[(10,7)].setIcon(QIcon(self.data[167][1]))
               self.button_case[(10,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[168][0])==2:
               self.button_case[(10,8)].setIcon(QIcon(self.data[168][1]))
               self.button_case[(10,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[169][0])==2:
               self.button_case[(10,9)].setIcon(QIcon(self.data[169][1]))
               self.button_case[(10,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[170][0])==2:
               self.button_case[(10,10)].setIcon(QIcon(self.data[170][1]))
               self.button_case[(10,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[171][0])==2:
               self.button_case[(10,11)].setIcon(QIcon(self.data[171][1]))
               self.button_case[(10,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[172][0])==2:
               self.button_case[(10,12)].setIcon(QIcon(self.data[172][1]))
               self.button_case[(10,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[173][0])==2:
               self.button_case[(10,13)].setIcon(QIcon(self.data[173][1]))
               self.button_case[(10,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[174][0])==2:
               self.button_case[(10,14)].setIcon(QIcon(self.data[174][1]))
               self.button_case[(10,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[175][0])==2:
               self.button_case[(10,15)].setIcon(QIcon(self.data[175][1]))
               self.button_case[(10,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 12
            if int(self.data[176][0])==2:
               self.button_case[(11,0)].setIcon(QIcon(self.data[176][1]))
               self.button_case[(11,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[177][0])==2:
               self.button_case[(11,1)].setIcon(QIcon(self.data[177][1]))
               self.button_case[(11,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[178][0])==2:
               self.button_case[(11,2)].setIcon(QIcon(self.data[178][1]))
               self.button_case[(11,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[179][0])==2:
               self.button_case[(11,3)].setIcon(QIcon(self.data[179][1]))
               self.button_case[(11,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[180][0])==2:
               self.button_case[(11,4)].setIcon(QIcon(self.data[180][1]))
               self.button_case[(11,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[181][0])==2:
               self.button_case[(11,5)].setIcon(QIcon(self.data[181][1]))
               self.button_case[(11,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[182][0])==2:
               self.button_case[(11,6)].setIcon(QIcon(self.data[182][1]))
               self.button_case[(11,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[183][0])==2:
               self.button_case[(11,7)].setIcon(QIcon(self.data[183][1]))
               self.button_case[(11,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[184][0])==2:
               self.button_case[(11,8)].setIcon(QIcon(self.data[184][1]))
               self.button_case[(11,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[185][0])==2:
               self.button_case[(11,9)].setIcon(QIcon(self.data[185][1]))
               self.button_case[(11,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[186][0])==2:
               self.button_case[(11,10)].setIcon(QIcon(self.data[186][1]))
               self.button_case[(11,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[187][0])==2:
               self.button_case[(11,11)].setIcon(QIcon(self.data[187][1]))
               self.button_case[(11,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[188][0])==2:
               self.button_case[(11,12)].setIcon(QIcon(self.data[188][1]))
               self.button_case[(11,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[189][0])==2:
               self.button_case[(11,13)].setIcon(QIcon(self.data[189][1]))
               self.button_case[(11,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[190][0])==2:
               self.button_case[(11,14)].setIcon(QIcon(self.data[190][1]))
               self.button_case[(11,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[191][0])==2:
               self.button_case[(11,15)].setIcon(QIcon(self.data[191][1]))
               self.button_case[(11,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 13
            if int(self.data[192][0])==2:
               self.button_case[(12,0)].setIcon(QIcon(self.data[192][1]))
               self.button_case[(12,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[193][0])==2:
               self.button_case[(12,1)].setIcon(QIcon(self.data[193][1]))
               self.button_case[(12,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[194][0])==2:
               self.button_case[(12,2)].setIcon(QIcon(self.data[194][1]))
               self.button_case[(12,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[195][0])==2:
               self.button_case[(12,3)].setIcon(QIcon(self.data[195][1]))
               self.button_case[(12,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[196][0])==2:
               self.button_case[(12,4)].setIcon(QIcon(self.data[196][1]))
               self.button_case[(12,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[197][0])==2:
               self.button_case[(12,5)].setIcon(QIcon(self.data[197][1]))
               self.button_case[(12,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[198][0])==2:
               self.button_case[(12,6)].setIcon(QIcon(self.data[198][1]))
               self.button_case[(12,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[199][0])==2:
               self.button_case[(12,7)].setIcon(QIcon(self.data[199][1]))
               self.button_case[(12,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[200][0])==2:
               self.button_case[(12,8)].setIcon(QIcon(self.data[200][1]))
               self.button_case[(12,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[201][0])==2:
               self.button_case[(12,9)].setIcon(QIcon(self.data[201][1]))
               self.button_case[(12,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[202][0])==2:
               self.button_case[(12,10)].setIcon(QIcon(self.data[202][1]))
               self.button_case[(12,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[203][0])==2:
               self.button_case[(12,11)].setIcon(QIcon(self.data[203][1]))
               self.button_case[(12,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[204][0])==2:
               self.button_case[(12,12)].setIcon(QIcon(self.data[204][1]))
               self.button_case[(12,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[205][0])==2:
               self.button_case[(12,13)].setIcon(QIcon(self.data[205][1]))
               self.button_case[(12,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[206][0])==2:
               self.button_case[(12,14)].setIcon(QIcon(self.data[206][1]))
               self.button_case[(12,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[207][0])==2:
               self.button_case[(12,15)].setIcon(QIcon(self.data[207][1]))
               self.button_case[(12,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 14
            if int(self.data[208][0])==2:
               self.button_case[(13,0)].setIcon(QIcon(self.data[208][1]))
               self.button_case[(13,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[209][0])==2:
               self.button_case[(13,1)].setIcon(QIcon(self.data[209][1]))
               self.button_case[(13,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[210][0])==2:
               self.button_case[(13,2)].setIcon(QIcon(self.data[210][1]))
               self.button_case[(13,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[211][0])==2:
               self.button_case[(13,3)].setIcon(QIcon(self.data[211][1]))
               self.button_case[(13,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[212][0])==2:
               self.button_case[(13,4)].setIcon(QIcon(self.data[212][1]))
               self.button_case[(13,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[213][0])==2:
               self.button_case[(13,5)].setIcon(QIcon(self.data[213][1]))
               self.button_case[(13,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[214][0])==2:
               self.button_case[(13,6)].setIcon(QIcon(self.data[214][1]))
               self.button_case[(13,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[215][0])==2:
               self.button_case[(13,7)].setIcon(QIcon(self.data[215][1]))
               self.button_case[(13,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[216][0])==2:
               self.button_case[(13,8)].setIcon(QIcon(self.data[216][1]))
               self.button_case[(13,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[217][0])==2:
               self.button_case[(13,9)].setIcon(QIcon(self.data[217][1]))
               self.button_case[(13,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[218][0])==2:
               self.button_case[(13,10)].setIcon(QIcon(self.data[218][1]))
               self.button_case[(13,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[219][0])==2:
               self.button_case[(13,11)].setIcon(QIcon(self.data[219][1]))
               self.button_case[(13,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[220][0])==2:
               self.button_case[(13,12)].setIcon(QIcon(self.data[220][1]))
               self.button_case[(13,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[221][0])==2:
               self.button_case[(13,13)].setIcon(QIcon(self.data[221][1]))
               self.button_case[(13,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[222][0])==2:
               self.button_case[(13,14)].setIcon(QIcon(self.data[222][1]))
               self.button_case[(13,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[223][0])==2:
               self.button_case[(13,15)].setIcon(QIcon(self.data[223][1]))
               self.button_case[(13,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 15
            if int(self.data[224][0])==2:
               self.button_case[(14,0)].setIcon(QIcon(self.data[224][1]))
               self.button_case[(14,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[225][0])==2:
               self.button_case[(14,1)].setIcon(QIcon(self.data[225][1]))
               self.button_case[(14,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[226][0])==2:
               self.button_case[(14,2)].setIcon(QIcon(self.data[226][1]))
               self.button_case[(14,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[227][0])==2:
               self.button_case[(14,3)].setIcon(QIcon(self.data[227][1]))
               self.button_case[(14,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[228][0])==2:
               self.button_case[(14,4)].setIcon(QIcon(self.data[228][1]))
               self.button_case[(14,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[229][0])==2:
               self.button_case[(14,5)].setIcon(QIcon(self.data[229][1]))
               self.button_case[(14,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[230][0])==2:
               self.button_case[(14,6)].setIcon(QIcon(self.data[230][1]))
               self.button_case[(14,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[231][0])==2:
               self.button_case[(14,7)].setIcon(QIcon(self.data[231][1]))
               self.button_case[(14,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[232][0])==2:
               self.button_case[(14,8)].setIcon(QIcon(self.data[232][1]))
               self.button_case[(14,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[233][0])==2:
               self.button_case[(14,9)].setIcon(QIcon(self.data[233][1]))
               self.button_case[(14,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[234][0])==2:
               self.button_case[(14,10)].setIcon(QIcon(self.data[234][1]))
               self.button_case[(14,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[235][0])==2:
               self.button_case[(14,11)].setIcon(QIcon(self.data[235][1]))
               self.button_case[(14,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[236][0])==2:
               self.button_case[(14,12)].setIcon(QIcon(self.data[236][1]))
               self.button_case[(14,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[237][0])==2:
               self.button_case[(14,13)].setIcon(QIcon(self.data[237][1]))
               self.button_case[(14,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[238][0])==2:
               self.button_case[(14,14)].setIcon(QIcon(self.data[238][1]))
               self.button_case[(14,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[239][0])==2:
               self.button_case[(14,15)].setIcon(QIcon(self.data[239][1]))
               self.button_case[(14,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 16
            if int(self.data[240][0])==2:
               self.button_case[(15,0)].setIcon(QIcon(self.data[240][1]))
               self.button_case[(15,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[241][0])==2:
               self.button_case[(15,1)].setIcon(QIcon(self.data[241][1]))
               self.button_case[(15,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[242][0])==2:
               self.button_case[(15,2)].setIcon(QIcon(self.data[242][1]))
               self.button_case[(15,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[243][0])==2:
               self.button_case[(15,3)].setIcon(QIcon(self.data[243][1]))
               self.button_case[(15,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[244][0])==2:
               self.button_case[(15,4)].setIcon(QIcon(self.data[244][1]))
               self.button_case[(15,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[245][0])==2:
               self.button_case[(15,5)].setIcon(QIcon(self.data[245][1]))
               self.button_case[(15,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[246][0])==2:
               self.button_case[(15,6)].setIcon(QIcon(self.data[246][1]))
               self.button_case[(15,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[247][0])==2:
               self.button_case[(15,7)].setIcon(QIcon(self.data[247][1]))
               self.button_case[(15,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[248][0])==2:
               self.button_case[(15,8)].setIcon(QIcon(self.data[248][1]))
               self.button_case[(15,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[249][0])==2:
               self.button_case[(15,9)].setIcon(QIcon(self.data[249][1]))
               self.button_case[(15,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[250][0])==2:
               self.button_case[(15,10)].setIcon(QIcon(self.data[250][1]))
               self.button_case[(15,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[251][0])==2:
               self.button_case[(15,11)].setIcon(QIcon(self.data[251][1]))
               self.button_case[(15,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[252][0])==2:
               self.button_case[(15,12)].setIcon(QIcon(self.data[252][1]))
               self.button_case[(15,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[253][0])==2:
               self.button_case[(15,13)].setIcon(QIcon(self.data[253][1]))
               self.button_case[(15,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[254][0])==2:
               self.button_case[(15,14)].setIcon(QIcon(self.data[254][1]))
               self.button_case[(15,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[255][0])==2:
               self.button_case[(15,15)].setIcon(QIcon(self.data[255][1]))
               self.button_case[(15,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 1
            if int(self.data[0][0])==0:
               self.button_case[(0,0)].setIcon(QIcon(""))
               self.button_case[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[1][0])==0:
               self.button_case[(0,1)].setIcon(QIcon(""))
               self.button_case[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[2][0])==0:
               self.button_case[(0,2)].setIcon(QIcon(""))
               self.button_case[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[3][0])==0:
               self.button_case[(0,3)].setIcon(QIcon(""))
               self.button_case[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[4][0])==0:
               self.button_case[(0,4)].setIcon(QIcon(""))
               self.button_case[(0,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[5][0])==0:
               self.button_case[(0,5)].setIcon(QIcon(""))
               self.button_case[(0,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[6][0])==0:
               self.button_case[(0,6)].setIcon(QIcon(""))
               self.button_case[(0,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[7][0])==0:
               self.button_case[(0,7)].setIcon(QIcon(""))
               self.button_case[(0,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[8][0])==0:
               self.button_case[(0,8)].setIcon(QIcon(""))
               self.button_case[(0,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[9][0])==0:
               self.button_case[(0,9)].setIcon(QIcon(""))
               self.button_case[(0,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[10][0])==0:
               self.button_case[(0,10)].setIcon(QIcon(""))
               self.button_case[(0,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[11][0])==0:
               self.button_case[(0,11)].setIcon(QIcon(""))
               self.button_case[(0,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[12][0])==0:
               self.button_case[(0,12)].setIcon(QIcon(""))
               self.button_case[(0,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[13][0])==0:
               self.button_case[(0,13)].setIcon(QIcon(""))
               self.button_case[(0,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[14][0])==0:
               self.button_case[(0,14)].setIcon(QIcon(""))
               self.button_case[(0,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[15][0])==0:
               self.button_case[(0,15)].setIcon(QIcon(""))
               self.button_case[(0,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 2
            if int(self.data[16][0])==0:
               self.button_case[(1,0)].setIcon(QIcon(""))
               self.button_case[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[17][0])==0:
               self.button_case[(1,1)].setIcon(QIcon(""))
               self.button_case[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[18][0])==0:
               self.button_case[(1,2)].setIcon(QIcon(""))
               self.button_case[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[19][0])==0:
               self.button_case[(1,3)].setIcon(QIcon(""))
               self.button_case[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[20][0])==0:
               self.button_case[(1,4)].setIcon(QIcon(""))
               self.button_case[(1,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[21][0])==0:
               self.button_case[(1,5)].setIcon(QIcon(""))
               self.button_case[(1,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[22][0])==0:
               self.button_case[(1,6)].setIcon(QIcon(""))
               self.button_case[(1,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[23][0])==0:
               self.button_case[(1,7)].setIcon(QIcon(""))
               self.button_case[(1,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[24][0])==0:
               self.button_case[(1,8)].setIcon(QIcon(""))
               self.button_case[(1,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[25][0])==0:
               self.button_case[(1,9)].setIcon(QIcon(""))
               self.button_case[(1,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[26][0])==0:
               self.button_case[(1,10)].setIcon(QIcon(""))
               self.button_case[(1,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[27][0])==0:
               self.button_case[(1,11)].setIcon(QIcon(""))
               self.button_case[(1,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[28][0])==0:
               self.button_case[(1,12)].setIcon(QIcon(""))
               self.button_case[(1,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[29][0])==0:
               self.button_case[(1,13)].setIcon(QIcon(""))
               self.button_case[(1,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[30][0])==0:
               self.button_case[(1,14)].setIcon(QIcon(""))
               self.button_case[(1,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[31][0])==0:
               self.button_case[(1,15)].setIcon(QIcon(""))
               self.button_case[(1,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 3
            if int(self.data[32][0])==0:
               self.button_case[(2,0)].setIcon(QIcon(""))
               self.button_case[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[33][0])==0:
               self.button_case[(2,1)].setIcon(QIcon(""))
               self.button_case[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[34][0])==0:
               self.button_case[(2,2)].setIcon(QIcon(""))
               self.button_case[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[35][0])==0:
               self.button_case[(2,3)].setIcon(QIcon(""))
               self.button_case[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[36][0])==0:
               self.button_case[(2,4)].setIcon(QIcon(""))
               self.button_case[(2,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[37][0])==0:
               self.button_case[(2,5)].setIcon(QIcon(""))
               self.button_case[(2,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[38][0])==0:
               self.button_case[(2,6)].setIcon(QIcon(""))
               self.button_case[(2,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[39][0])==0:
               self.button_case[(2,7)].setIcon(QIcon(""))
               self.button_case[(2,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[40][0])==0:
               self.button_case[(2,8)].setIcon(QIcon(""))
               self.button_case[(2,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[41][0])==0:
               self.button_case[(2,9)].setIcon(QIcon(""))
               self.button_case[(2,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[42][0])==0:
               self.button_case[(2,10)].setIcon(QIcon(""))
               self.button_case[(2,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[43][0])==0:
               self.button_case[(2,11)].setIcon(QIcon(""))
               self.button_case[(2,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[44][0])==0:
               self.button_case[(2,12)].setIcon(QIcon(""))
               self.button_case[(2,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[45][0])==0:
               self.button_case[(2,13)].setIcon(QIcon(""))
               self.button_case[(2,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[46][0])==0:
               self.button_case[(2,14)].setIcon(QIcon(""))
               self.button_case[(2,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[47][0])==0:
               self.button_case[(2,15)].setIcon(QIcon(""))
               self.button_case[(2,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 4
            if int(self.data[48][0])==0:
               self.button_case[(3,0)].setIcon(QIcon(""))
               self.button_case[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[49][0])==0:
               self.button_case[(3,1)].setIcon(QIcon(""))
               self.button_case[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[50][0])==0:
               self.button_case[(3,2)].setIcon(QIcon(""))
               self.button_case[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[51][0])==0:
               self.button_case[(3,3)].setIcon(QIcon(""))
               self.button_case[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[52][0])==0:
               self.button_case[(3,4)].setIcon(QIcon(""))
               self.button_case[(3,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[53][0])==0:
               self.button_case[(3,5)].setIcon(QIcon(""))
               self.button_case[(3,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[54][0])==0:
               self.button_case[(3,6)].setIcon(QIcon(""))
               self.button_case[(3,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[55][0])==0:
               self.button_case[(3,7)].setIcon(QIcon(""))
               self.button_case[(3,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[56][0])==0:
               self.button_case[(3,8)].setIcon(QIcon(""))
               self.button_case[(3,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[57][0])==0:
               self.button_case[(3,9)].setIcon(QIcon(""))
               self.button_case[(3,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[58][0])==0:
               self.button_case[(3,10)].setIcon(QIcon(""))
               self.button_case[(3,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[59][0])==0:
               self.button_case[(3,11)].setIcon(QIcon(""))
               self.button_case[(3,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[60][0])==0:
               self.button_case[(3,12)].setIcon(QIcon(""))
               self.button_case[(3,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[61][0])==0:
               self.button_case[(3,13)].setIcon(QIcon(""))
               self.button_case[(3,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[62][0])==0:
               self.button_case[(3,14)].setIcon(QIcon(""))
               self.button_case[(3,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[63][0])==0:
               self.button_case[(3,15)].setIcon(QIcon(""))
               self.button_case[(3,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 5
            if int(self.data[64][0])==0:
               self.button_case[(4,0)].setIcon(QIcon(""))
               self.button_case[(4,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[65][0])==0:
               self.button_case[(4,1)].setIcon(QIcon(""))
               self.button_case[(4,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[66][0])==0:
               self.button_case[(4,2)].setIcon(QIcon(""))
               self.button_case[(4,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[67][0])==0:
               self.button_case[(4,3)].setIcon(QIcon(""))
               self.button_case[(4,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[68][0])==0:
               self.button_case[(4,4)].setIcon(QIcon(""))
               self.button_case[(4,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[69][0])==0:
               self.button_case[(4,5)].setIcon(QIcon(""))
               self.button_case[(4,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[70][0])==0:
               self.button_case[(4,6)].setIcon(QIcon(""))
               self.button_case[(4,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[71][0])==0:
               self.button_case[(4,7)].setIcon(QIcon(""))
               self.button_case[(4,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[72][0])==0:
               self.button_case[(4,8)].setIcon(QIcon(""))
               self.button_case[(4,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[73][0])==0:
               self.button_case[(4,9)].setIcon(QIcon(""))
               self.button_case[(4,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[74][0])==0:
               self.button_case[(4,10)].setIcon(QIcon(""))
               self.button_case[(4,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[75][0])==0:
               self.button_case[(4,11)].setIcon(QIcon(""))
               self.button_case[(4,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[76][0])==0:
               self.button_case[(4,12)].setIcon(QIcon(""))
               self.button_case[(4,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[77][0])==0:
               self.button_case[(4,13)].setIcon(QIcon(""))
               self.button_case[(4,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[78][0])==0:
               self.button_case[(4,14)].setIcon(QIcon(""))
               self.button_case[(4,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[79][0])==0:
               self.button_case[(4,15)].setIcon(QIcon(""))
               self.button_case[(4,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 6
            if int(self.data[80][0])==0:
               self.button_case[(5,0)].setIcon(QIcon(""))
               self.button_case[(5,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[81][0])==0:
               self.button_case[(5,1)].setIcon(QIcon(""))
               self.button_case[(5,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[82][0])==0:
               self.button_case[(5,2)].setIcon(QIcon(""))
               self.button_case[(5,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[83][0])==0:
               self.button_case[(5,3)].setIcon(QIcon(""))
               self.button_case[(5,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[84][0])==0:
               self.button_case[(5,4)].setIcon(QIcon(""))
               self.button_case[(5,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[85][0])==0:
               self.button_case[(5,5)].setIcon(QIcon(""))
               self.button_case[(5,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[86][0])==0:
               self.button_case[(5,6)].setIcon(QIcon(""))
               self.button_case[(5,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[87][0])==0:
               self.button_case[(5,7)].setIcon(QIcon(""))
               self.button_case[(5,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[88][0])==0:
               self.button_case[(5,8)].setIcon(QIcon(""))
               self.button_case[(5,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[89][0])==0:
               self.button_case[(5,9)].setIcon(QIcon(""))
               self.button_case[(5,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[90][0])==0:
               self.button_case[(5,10)].setIcon(QIcon(""))
               self.button_case[(5,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[91][0])==0:
               self.button_case[(5,11)].setIcon(QIcon(""))
               self.button_case[(5,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[92][0])==0:
               self.button_case[(5,12)].setIcon(QIcon(""))
               self.button_case[(5,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[93][0])==0:
               self.button_case[(5,13)].setIcon(QIcon(""))
               self.button_case[(5,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[94][0])==0:
               self.button_case[(5,14)].setIcon(QIcon(""))
               self.button_case[(5,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[95][0])==0:
               self.button_case[(5,15)].setIcon(QIcon(""))
               self.button_case[(5,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 7
            if int(self.data[96][0])==0:
               self.button_case[(6,0)].setIcon(QIcon(""))
               self.button_case[(6,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[97][0])==0:
               self.button_case[(6,1)].setIcon(QIcon(""))
               self.button_case[(6,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[98][0])==0:
               self.button_case[(6,2)].setIcon(QIcon(""))
               self.button_case[(6,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[99][0])==0:
               self.button_case[(6,3)].setIcon(QIcon(""))
               self.button_case[(6,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[100][0])==0:
               self.button_case[(6,4)].setIcon(QIcon(""))
               self.button_case[(6,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[101][0])==0:
               self.button_case[(6,5)].setIcon(QIcon(""))
               self.button_case[(6,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[102][0])==0:
               self.button_case[(6,6)].setIcon(QIcon(""))
               self.button_case[(6,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[103][0])==0:
               self.button_case[(6,7)].setIcon(QIcon(""))
               self.button_case[(6,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[104][0])==0:
               self.button_case[(6,8)].setIcon(QIcon(""))
               self.button_case[(6,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[105][0])==0:
               self.button_case[(6,9)].setIcon(QIcon(""))
               self.button_case[(6,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[106][0])==0:
               self.button_case[(6,10)].setIcon(QIcon(""))
               self.button_case[(6,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[107][0])==0:
               self.button_case[(6,11)].setIcon(QIcon(""))
               self.button_case[(6,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[108][0])==0:
               self.button_case[(6,12)].setIcon(QIcon(""))
               self.button_case[(6,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[109][0])==0:
               self.button_case[(6,13)].setIcon(QIcon(""))
               self.button_case[(6,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[110][0])==0:
               self.button_case[(6,14)].setIcon(QIcon(""))
               self.button_case[(6,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[111][0])==0:
               self.button_case[(6,15)].setIcon(QIcon(""))
               self.button_case[(6,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 8
            if int(self.data[112][0])==0:
               self.button_case[(7,0)].setIcon(QIcon(""))
               self.button_case[(7,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[113][0])==0:
               self.button_case[(7,1)].setIcon(QIcon(""))
               self.button_case[(7,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[114][0])==0:
               self.button_case[(7,2)].setIcon(QIcon(""))
               self.button_case[(7,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[115][0])==0:
               self.button_case[(7,3)].setIcon(QIcon(""))
               self.button_case[(7,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[116][0])==0:
               self.button_case[(7,4)].setIcon(QIcon(""))
               self.button_case[(7,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[117][0])==0:
               self.button_case[(7,5)].setIcon(QIcon(""))
               self.button_case[(7,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[118][0])==0:
               self.button_case[(7,6)].setIcon(QIcon(""))
               self.button_case[(7,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[119][0])==0:
               self.button_case[(7,7)].setIcon(QIcon(""))
               self.button_case[(7,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[120][0])==0:
               self.button_case[(7,8)].setIcon(QIcon(""))
               self.button_case[(7,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[121][0])==0:
               self.button_case[(7,9)].setIcon(QIcon(""))
               self.button_case[(7,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[122][0])==0:
               self.button_case[(7,10)].setIcon(QIcon(""))
               self.button_case[(7,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[123][0])==0:
               self.button_case[(7,11)].setIcon(QIcon(""))
               self.button_case[(7,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[124][0])==0:
               self.button_case[(7,12)].setIcon(QIcon(""))
               self.button_case[(7,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[125][0])==0:
               self.button_case[(7,13)].setIcon(QIcon(""))
               self.button_case[(7,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[126][0])==0:
               self.button_case[(7,14)].setIcon(QIcon(""))
               self.button_case[(7,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[127][0])==0:
               self.button_case[(7,15)].setIcon(QIcon(""))
               self.button_case[(7,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 9
            if int(self.data[128][0])==0:
               self.button_case[(8,0)].setIcon(QIcon(""))
               self.button_case[(8,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[129][0])==0:
               self.button_case[(8,1)].setIcon(QIcon(""))
               self.button_case[(8,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[130][0])==0:
               self.button_case[(8,2)].setIcon(QIcon(""))
               self.button_case[(8,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[131][0])==0:
               self.button_case[(8,3)].setIcon(QIcon(""))
               self.button_case[(8,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[132][0])==0:
               self.button_case[(8,4)].setIcon(QIcon(""))
               self.button_case[(8,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[133][0])==0:
               self.button_case[(8,5)].setIcon(QIcon(""))
               self.button_case[(8,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[134][0])==0:
               self.button_case[(8,6)].setIcon(QIcon(""))
               self.button_case[(8,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[135][0])==0:
               self.button_case[(8,7)].setIcon(QIcon(""))
               self.button_case[(8,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[136][0])==0:
               self.button_case[(8,8)].setIcon(QIcon(""))
               self.button_case[(8,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[137][0])==0:
               self.button_case[(8,9)].setIcon(QIcon(""))
               self.button_case[(8,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[138][0])==0:
               self.button_case[(8,10)].setIcon(QIcon(""))
               self.button_case[(8,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[139][0])==0:
               self.button_case[(8,11)].setIcon(QIcon(""))
               self.button_case[(8,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[140][0])==0:
               self.button_case[(8,12)].setIcon(QIcon(""))
               self.button_case[(8,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[141][0])==0:
               self.button_case[(8,13)].setIcon(QIcon(""))
               self.button_case[(8,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[142][0])==0:
               self.button_case[(8,14)].setIcon(QIcon(""))
               self.button_case[(8,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[143][0])==0:
               self.button_case[(8,15)].setIcon(QIcon(""))
               self.button_case[(8,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 10
            if int(self.data[144][0])==0:
               self.button_case[(9,0)].setIcon(QIcon(""))
               self.button_case[(9,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[145][0])==0:
               self.button_case[(9,1)].setIcon(QIcon(""))
               self.button_case[(9,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[146][0])==0:
               self.button_case[(9,2)].setIcon(QIcon(""))
               self.button_case[(9,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[147][0])==0:
               self.button_case[(9,3)].setIcon(QIcon(""))
               self.button_case[(9,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[148][0])==0:
               self.button_case[(9,4)].setIcon(QIcon(""))
               self.button_case[(9,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[149][0])==0:
               self.button_case[(9,5)].setIcon(QIcon(""))
               self.button_case[(9,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[150][0])==0:
               self.button_case[(9,6)].setIcon(QIcon(""))
               self.button_case[(9,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[151][0])==0:
               self.button_case[(9,7)].setIcon(QIcon(""))
               self.button_case[(9,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[152][0])==0:
               self.button_case[(9,8)].setIcon(QIcon(""))
               self.button_case[(9,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[153][0])==0:
               self.button_case[(9,9)].setIcon(QIcon(""))
               self.button_case[(9,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[154][0])==0:
               self.button_case[(9,10)].setIcon(QIcon(""))
               self.button_case[(9,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[155][0])==0:
               self.button_case[(9,11)].setIcon(QIcon(""))
               self.button_case[(9,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[156][0])==0:
               self.button_case[(9,12)].setIcon(QIcon(""))
               self.button_case[(9,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[157][0])==0:
               self.button_case[(9,13)].setIcon(QIcon(""))
               self.button_case[(9,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[158][0])==0:
               self.button_case[(9,14)].setIcon(QIcon(""))
               self.button_case[(9,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[159][0])==0:
               self.button_case[(9,15)].setIcon(QIcon(""))
               self.button_case[(9,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 11
            if int(self.data[160][0])==0:
               self.button_case[(10,0)].setIcon(QIcon(""))
               self.button_case[(10,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[161][0])==0:
               self.button_case[(10,1)].setIcon(QIcon(""))
               self.button_case[(10,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[162][0])==0:
               self.button_case[(10,2)].setIcon(QIcon(""))
               self.button_case[(10,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[163][0])==0:
               self.button_case[(10,3)].setIcon(QIcon(""))
               self.button_case[(10,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[164][0])==0:
               self.button_case[(10,4)].setIcon(QIcon(""))
               self.button_case[(10,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[165][0])==0:
               self.button_case[(10,5)].setIcon(QIcon(""))
               self.button_case[(10,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[166][0])==0:
               self.button_case[(10,6)].setIcon(QIcon(""))
               self.button_case[(10,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[167][0])==0:
               self.button_case[(10,7)].setIcon(QIcon(""))
               self.button_case[(10,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[168][0])==0:
               self.button_case[(10,8)].setIcon(QIcon(""))
               self.button_case[(10,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[169][0])==0:
               self.button_case[(10,9)].setIcon(QIcon(""))
               self.button_case[(10,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[170][0])==0:
               self.button_case[(10,10)].setIcon(QIcon(""))
               self.button_case[(10,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[171][0])==0:
               self.button_case[(10,11)].setIcon(QIcon(""))
               self.button_case[(10,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[172][0])==0:
               self.button_case[(10,12)].setIcon(QIcon(""))
               self.button_case[(10,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[173][0])==0:
               self.button_case[(10,13)].setIcon(QIcon(""))
               self.button_case[(10,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[174][0])==0:
               self.button_case[(10,14)].setIcon(QIcon(""))
               self.button_case[(10,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[175][0])==0:
               self.button_case[(10,15)].setIcon(QIcon(""))
               self.button_case[(10,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 12
            if int(self.data[176][0])==0:
               self.button_case[(11,0)].setIcon(QIcon(""))
               self.button_case[(11,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[177][0])==0:
               self.button_case[(11,1)].setIcon(QIcon(""))
               self.button_case[(11,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[178][0])==0:
               self.button_case[(11,2)].setIcon(QIcon(""))
               self.button_case[(11,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[179][0])==0:
               self.button_case[(11,3)].setIcon(QIcon(""))
               self.button_case[(11,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[180][0])==0:
               self.button_case[(11,4)].setIcon(QIcon(""))
               self.button_case[(11,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[181][0])==0:
               self.button_case[(11,5)].setIcon(QIcon(""))
               self.button_case[(11,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[182][0])==0:
               self.button_case[(11,6)].setIcon(QIcon(""))
               self.button_case[(11,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[183][0])==0:
               self.button_case[(11,7)].setIcon(QIcon(""))
               self.button_case[(11,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[184][0])==0:
               self.button_case[(11,8)].setIcon(QIcon(""))
               self.button_case[(11,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[185][0])==0:
               self.button_case[(11,9)].setIcon(QIcon(""))
               self.button_case[(11,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[186][0])==0:
               self.button_case[(11,10)].setIcon(QIcon(""))
               self.button_case[(11,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[187][0])==0:
               self.button_case[(11,11)].setIcon(QIcon(""))
               self.button_case[(11,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[188][0])==0:
               self.button_case[(11,12)].setIcon(QIcon(""))
               self.button_case[(11,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[189][0])==0:
               self.button_case[(11,13)].setIcon(QIcon(""))
               self.button_case[(11,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[190][0])==0:
               self.button_case[(11,14)].setIcon(QIcon(""))
               self.button_case[(11,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[191][0])==0:
               self.button_case[(11,15)].setIcon(QIcon(""))
               self.button_case[(11,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 13
            if int(self.data[192][0])==0:
               self.button_case[(12,0)].setIcon(QIcon(""))
               self.button_case[(12,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[193][0])==0:
               self.button_case[(12,1)].setIcon(QIcon(""))
               self.button_case[(12,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[194][0])==0:
               self.button_case[(12,2)].setIcon(QIcon(""))
               self.button_case[(12,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[195][0])==0:
               self.button_case[(12,3)].setIcon(QIcon(""))
               self.button_case[(12,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[196][0])==0:
               self.button_case[(12,4)].setIcon(QIcon(""))
               self.button_case[(12,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[197][0])==0:
               self.button_case[(12,5)].setIcon(QIcon(""))
               self.button_case[(12,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[198][0])==0:
               self.button_case[(12,6)].setIcon(QIcon(""))
               self.button_case[(12,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[199][0])==0:
               self.button_case[(12,7)].setIcon(QIcon(""))
               self.button_case[(12,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[200][0])==0:
               self.button_case[(12,8)].setIcon(QIcon(""))
               self.button_case[(12,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[201][0])==0:
               self.button_case[(12,9)].setIcon(QIcon(""))
               self.button_case[(12,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[202][0])==0:
               self.button_case[(12,10)].setIcon(QIcon(""))
               self.button_case[(12,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[203][0])==0:
               self.button_case[(12,11)].setIcon(QIcon(""))
               self.button_case[(12,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[204][0])==0:
               self.button_case[(12,12)].setIcon(QIcon(""))
               self.button_case[(12,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[205][0])==0:
               self.button_case[(12,13)].setIcon(QIcon(""))
               self.button_case[(12,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[206][0])==0:
               self.button_case[(12,14)].setIcon(QIcon(""))
               self.button_case[(12,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[207][0])==0:
               self.button_case[(12,15)].setIcon(QIcon(""))
               self.button_case[(12,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 14
            if int(self.data[208][0])==0:
               self.button_case[(13,0)].setIcon(QIcon(""))
               self.button_case[(13,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[209][0])==0:
               self.button_case[(13,1)].setIcon(QIcon(""))
               self.button_case[(13,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[210][0])==0:
               self.button_case[(13,2)].setIcon(QIcon(""))
               self.button_case[(13,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[211][0])==0:
               self.button_case[(13,3)].setIcon(QIcon(""))
               self.button_case[(13,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[212][0])==0:
               self.button_case[(13,4)].setIcon(QIcon(""))
               self.button_case[(13,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[213][0])==0:
               self.button_case[(13,5)].setIcon(QIcon(""))
               self.button_case[(13,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[214][0])==0:
               self.button_case[(13,6)].setIcon(QIcon(""))
               self.button_case[(13,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[215][0])==0:
               self.button_case[(13,7)].setIcon(QIcon(""))
               self.button_case[(13,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[216][0])==0:
               self.button_case[(13,8)].setIcon(QIcon(""))
               self.button_case[(13,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[217][0])==0:
               self.button_case[(13,9)].setIcon(QIcon(""))
               self.button_case[(13,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[218][0])==0:
               self.button_case[(13,10)].setIcon(QIcon(""))
               self.button_case[(13,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[219][0])==0:
               self.button_case[(13,11)].setIcon(QIcon(""))
               self.button_case[(13,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[220][0])==0:
               self.button_case[(13,12)].setIcon(QIcon(""))
               self.button_case[(13,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[221][0])==0:
               self.button_case[(13,13)].setIcon(QIcon(""))
               self.button_case[(13,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[222][0])==0:
               self.button_case[(13,14)].setIcon(QIcon(""))
               self.button_case[(13,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[223][0])==0:
               self.button_case[(13,15)].setIcon(QIcon(""))
               self.button_case[(13,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 15
            if int(self.data[224][0])==0:
               self.button_case[(14,0)].setIcon(QIcon(""))
               self.button_case[(14,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[225][0])==0:
               self.button_case[(14,1)].setIcon(QIcon(""))
               self.button_case[(14,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[226][0])==0:
               self.button_case[(14,2)].setIcon(QIcon(""))
               self.button_case[(14,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[227][0])==0:
               self.button_case[(14,3)].setIcon(QIcon(""))
               self.button_case[(14,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[228][0])==0:
               self.button_case[(14,4)].setIcon(QIcon(""))
               self.button_case[(14,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[229][0])==0:
               self.button_case[(14,5)].setIcon(QIcon(""))
               self.button_case[(14,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[230][0])==0:
               self.button_case[(14,6)].setIcon(QIcon(""))
               self.button_case[(14,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[231][0])==0:
               self.button_case[(14,7)].setIcon(QIcon(""))
               self.button_case[(14,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[232][0])==0:
               self.button_case[(14,8)].setIcon(QIcon(""))
               self.button_case[(14,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[233][0])==0:
               self.button_case[(14,9)].setIcon(QIcon(""))
               self.button_case[(14,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[234][0])==0:
               self.button_case[(14,10)].setIcon(QIcon(""))
               self.button_case[(14,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[235][0])==0:
               self.button_case[(14,11)].setIcon(QIcon(""))
               self.button_case[(14,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[236][0])==0:
               self.button_case[(14,12)].setIcon(QIcon(""))
               self.button_case[(14,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[237][0])==0:
               self.button_case[(14,13)].setIcon(QIcon(""))
               self.button_case[(14,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[238][0])==0:
               self.button_case[(14,14)].setIcon(QIcon(""))
               self.button_case[(14,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[239][0])==0:
               self.button_case[(14,15)].setIcon(QIcon(""))
               self.button_case[(14,15)].setIconSize(QSize(self.icon_size,self.icon_size))
            ########################### LINE 16
            if int(self.data[240][0])==0:
               self.button_case[(15,0)].setIcon(QIcon(""))
               self.button_case[(15,0)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[241][0])==0:
               self.button_case[(15,1)].setIcon(QIcon(""))
               self.button_case[(15,1)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[242][0])==0:
               self.button_case[(15,2)].setIcon(QIcon(""))
               self.button_case[(15,2)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[243][0])==0:
               self.button_case[(15,3)].setIcon(QIcon(""))
               self.button_case[(15,3)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[244][0])==0:
               self.button_case[(15,4)].setIcon(QIcon(""))
               self.button_case[(15,4)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[245][0])==0:
               self.button_case[(15,5)].setIcon(QIcon(""))
               self.button_case[(15,5)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[246][0])==0:
               self.button_case[(15,6)].setIcon(QIcon(""))
               self.button_case[(15,6)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[247][0])==0:
               self.button_case[(15,7)].setIcon(QIcon(""))
               self.button_case[(15,7)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[248][0])==0:
               self.button_case[(15,8)].setIcon(QIcon(""))
               self.button_case[(15,8)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[249][0])==0:
               self.button_case[(15,9)].setIcon(QIcon(""))
               self.button_case[(15,9)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[250][0])==0:
               self.button_case[(15,10)].setIcon(QIcon(""))
               self.button_case[(15,10)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[251][0])==0:
               self.button_case[(15,11)].setIcon(QIcon(""))
               self.button_case[(15,11)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[252][0])==0:
               self.button_case[(15,12)].setIcon(QIcon(""))
               self.button_case[(15,12)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[253][0])==0:
               self.button_case[(15,13)].setIcon(QIcon(""))
               self.button_case[(15,13)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[254][0])==0:
               self.button_case[(15,14)].setIcon(QIcon(""))
               self.button_case[(15,14)].setIconSize(QSize(self.icon_size,self.icon_size))
            if int(self.data[255][0])==0:
               self.button_case[(15,15)].setIcon(QIcon(""))
               self.button_case[(15,15)].setIconSize(QSize(self.icon_size,self.icon_size))

            self.board=[[self.value1,self.value2,self.value3,self.value4,self.value5,self.value6,self.value7,self.value8,
                         self.value9,self.value10,self.value11,self.value12,self.value13,self.value14,self.value15,self.value16],
                        [self.value17,self.value18,self.value19,self.value20,self.value21,self.value22,self.value23,self.value24,
                         self.value25,self.value26,self.value27,self.value28,self.value29,self.value30,self.value31,self.value32],
                        [self.value33,self.value34,self.value35,self.value36,self.value37,self.value38,self.value39,self.value40,
                         self.value41,self.value42,self.value43,self.value44,self.value45,self.value46,self.value47,self.value48],
                        [self.value49,self.value50,self.value51,self.value52,self.value53,self.value54,self.value55,self.value56,
                         self.value57,self.value58,self.value59,self.value60,self.value61,self.value62,self.value63,self.value64],
                        [self.value65,self.value66,self.value67,self.value68,self.value69,self.value70,self.value71,self.value72,
                         self.value73,self.value74,self.value75,self.value76,self.value77,self.value78,self.value79,self.value80],
                        [self.value81,self.value82,self.value83,self.value84,self.value85,self.value86,self.value87,self.value88,
                         self.value89,self.value90,self.value91,self.value92,self.value93,self.value94,self.value95,self.value96],
                        [self.value97,self.value98,self.value99,self.value100,self.value101,self.value102,self.value103,self.value104,
                         self.value105,self.value106,self.value107,self.value108,self.value109,self.value110,self.value111,self.value112],
                        [self.value113,self.value114,self.value115,self.value116,self.value117,self.value118,self.value119,self.value120,
                         self.value121,self.value122,self.value123,self.value124,self.value125,self.value126,self.value127,self.value128],
                        [self.value129,self.value130,self.value131,self.value132,self.value133,self.value134,self.value135,self.value136,
                         self.value137,self.value138,self.value139,self.value140,self.value141,self.value142,self.value143,self.value144],
                        [self.value145,self.value146,self.value147,self.value148,self.value149,self.value150,self.value151,self.value152,
                         self.value153,self.value154,self.value155,self.value156,self.value157,self.value158,self.value159,self.value160],
                        [self.value161,self.value162,self.value163,self.value164,self.value165,self.value166,self.value167,self.value168,
                         self.value169,self.value170,self.value171,self.value172,self.value173,self.value174,self.value175,self.value176],
                        [self.value177,self.value178,self.value179,self.value180,self.value181,self.value182,self.value183,self.value184,
                         self.value185,self.value186,self.value187,self.value188,self.value189,self.value190,self.value191,self.value192],
                        [self.value193,self.value194,self.value195,self.value196,self.value197,self.value198,self.value199,self.value200,
                         self.value201,self.value202,self.value203,self.value204,self.value205,self.value206,self.value207,self.value208],                       
                        [self.value209,self.value210,self.value211,self.value212,self.value213,self.value214,self.value215,self.value216,
                         self.value217,self.value218,self.value219,self.value220,self.value221,self.value222,self.value223,self.value224],
                        [self.value225,self.value226,self.value227,self.value228,self.value229,self.value230,self.value231,self.value232,
                         self.value233,self.value234,self.value235,self.value236,self.value237,self.value238,self.value239,self.value240],
                        [self.value241,self.value242,self.value243,self.value244,self.value245,self.value246,self.value247,self.value248,
                         self.value249,self.value250,self.value251,self.value252,self.value253,self.value254,self.value255,self.value256]]

            
            self.score=self.cursor.execute("SELECT value FROM score WHERE rowid=1")            
            for row in self.score:
               self.score_value.setText(str(row[0]))

            self.high_score=self.cursor.execute("SELECT value FROM hi_score WHERE rowid=1")             
            for row in self.high_score:
               self.hi_score_value.setText(str(row[0]))
            self.Design()

   def reset(self):
      if (os.path.exists('predator.bd') and os.path.isfile('predator.bd')):
         try:
            self.bdd=sqlite3.connect('predator.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,"PREDATOR",e)
         finally:
            self.question=QMessageBox.question(self,"PREDATOR",'CONTINUER ?',QMessageBox.Yes,QMessageBox.No)
            if self.question==QMessageBox.Yes:
               self.cursor=self.bdd.cursor()
               
               record_game=[ (1,0,""), (2,0,""), (3,0,""), (4,0,""), (5,0,""), (6,0,""), (7,0,""), (8,0,""),
                             (9,0,""), (10,0,""), (11,0,""), (12,0,""), (13,0,""), (14,0,""), (15,0,""), (16,0,""),
                             (17,0,""), (18,0,""), (19,0,""), (20,0,""), (21,0,""), (22,0,""), (23,0,""), (24,0,""),
                             (25,0,""), (26,0,""), (27,0,""), (28,0,""), (29,0,""), (30,0,""), (31,0,""), (32,0,""),
                             (33,0,""), (34,0,""), (35,0,""), (36,0,""), (37,0,""), (38,0,""), (39,0,""), (40,0,""),
                             (41,0,""), (42,0,""), (43,0,""), (44,0,""), (45,0,""), (46,0,""), (47,0,""), (48,0,""),
                             (49,0,""), (50,0,""), (51,0,""), (52,0,""), (53,0,""), (54,0,""), (55,0,""), (56,0,""),
                             (57,0,""), (58,0,""), (59,0,""), (60,0,""), (61,0,""), (62,0,""), (63,0,""), (64,0,""),
                             (65,0,""), (66,0,""), (67,0,""), (68,0,""), (69,0,""), (70,0,""), (71,0,""), (72,0,""),
                             (73,0,""), (74,0,""), (75,0,""), (76,0,""), (77,0,""), (78,0,""), (79,0,""), (80,0,""),
                             (81,0,""), (82,0,""), (83,0,""), (84,0,""), (85,0,""), (86,0,""), (87,0,""), (88,0,""),
                             (89,0,""), (90,0,""), (91,0,""), (92,0,""), (93,0,""), (94,0,""), (95,0,""), (96,0,""),
                             (97,0,""), (98,0,""), (99,0,""), (100,0,""), (101,0,""), (102,0,""), (103,0,""), (104,0,""),
                             (105,0,""), (106,0,""), (107,0,""), (108,0,""), (109,0,""), (110,0,""), (111,0,""), (112,0,""),
                             (113,0,""), (114,0,""), (115,0,""), (116,0,""), (117,0,""), (118,0,""), (119,0,""), (120,0,""),
                             (121,0,""), (122,0,""), (123,0,""), (124,0,""), (125,0,""), (126,0,""), (127,0,""), (128,0,""),
                             (129,0,""), (130,0,""), (131,0,""), (132,0,""), (133,0,""), (134,0,""), (135,0,""), (136,0,""),
                             (137,0,""), (138,0,""), (139,0,""), (140,0,""), (141,0,""), (142,0,""), (143,0,""), (144,0,""),
                             (145,0,""), (146,0,""), (147,0,""), (148,0,""), (149,0,""), (150,0,""), (151,0,""), (152,0,""),
                             (153,0,""), (154,0,""), (155,0,""), (156,0,""), (157,0,""), (158,0,""), (159,0,""), (160,0,""),
                             (161,0,""), (162,0,""), (163,0,""), (164,0,""), (165,0,""), (166,0,""), (167,0,""), (168,0,""),
                             (169,0,""), (170,0,""), (171,0,""), (172,0,""), (173,0,""), (174,0,""), (175,0,""), (176,0,""),
                             (177,0,""), (178,0,""), (179,0,""), (180,0,""), (181,0,""), (182,0,""), (183,0,""), (184,0,""),
                             (185,0,""), (186,0,""), (187,0,""), (188,0,""), (189,0,""), (190,0,""), (191,0,""), (192,0,""),
                             (193,0,""), (194,0,""), (195,0,""), (196,0,""), (197,0,""), (198,0,""), (199,0,""), (200,0,""),
                             (201,0,""), (202,0,""), (203,0,""), (204,0,""), (205,0,""), (206,0,""), (207,0,""), (208,0,""),
                             (209,0,""), (210,0,""), (211,0,""), (212,0,""), (213,0,""), (214,0,""), (215,0,""), (216,0,""),
                             (217,0,""), (218,0,""), (219,0,""), (220,0,""), (221,0,""), (222,0,""), (223,0,""), (224,0,""),
                             (225,0,""), (226,0,""), (227,0,""), (228,0,""), (229,0,""), (230,0,""), (231,0,""), (232,0,""),
                             (233,0,""), (234,0,""), (235,0,""), (236,0,""), (237,0,""), (238,0,""), (239,0,""), (240,0,""),
                             (241,1,"images/pion1.svg"), (242,1,"images/pion1.svg"), (243,1,"images/pion1.svg"), (244,1,"images/pion1.svg"),
                             (245,2,"images/pion2.svg"), (246,0,""), (247,0,""), (248,0,""),
                             (249,0,""), (250,0,""), (251,0,""), (252,0,""), (253,0,""), (254,0,""), (255,0,""), (256,0,"")]

               # For Game
               self.cursor.execute("""DELETE FROM game""")
               self.cursor.executemany("""INSERT INTO game (id,value,image) VALUES (?,?,?)""",record_game)
               # For Score
               self.cursor.execute("""DELETE FROM score""")
               self.cursor.execute("""INSERT INTO score (id,value) VALUES (?,?)""",(1,0))
               # For Hi_score
               self.cursor.execute("""DELETE FROM hi_score""")
               self.cursor.execute("""INSERT INTO hi_score (id,value) VALUES (?,?)""",(1,0))
               
               self.bdd.commit()
               self.refresh_data()
               QMessageBox.information(self,"PREDATOR","JEUX REINITIALISE")


   #==== Timer to create a loop for ball move
   #self.timer = multitimer.MultiTimer(interval=0.12,function=self.directions_allowed, count=-1)
   #self.timer.start()
   
   
   def directions_allowed(self,event):
      if event.type() == QEvent.KeyPress:
         self.new_direction = event
         print(self.handle(event))
         self.all_directions = ('Up','Down','Left','Right')
         self.opposites = ({'Up','Down'},{'Left','Right'},{'Down','Up'},{'Right','Left'})
         if ( self.new_direction in self.all_directions and {self.new_direction,self.direction} not in self.opposites ):
             self.direction = self.new_direction

   
               

      
if __name__=='__main__':
   app=QApplication(sys.argv)
   app.setStyle('plastique')
   screen=PREDATOR() 
   screen.show()
   sys.exit(app.exec_())
