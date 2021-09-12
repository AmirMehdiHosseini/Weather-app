import requests
import json
import time
from   window           import *
from   PyQt5.QtWidgets  import *
from   PyQt5.QtCore     import *


api_key = '78392b6773396310bfcef5c2d6967491'


main_url = "http://api.openweathermap.org/data/2.5/weather?"






class Weather(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_Weather()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton_done.clicked.connect(self.weather_info)


        city = self.ui.lineEdit_city.text()


        complete_url = main_url + "appid=" + api_key + "&q=" + city


        res = requests.get(complete_url)


        self.json_info = res.json()








    def mousePressEvent(self,evt):
        self.oldPos = evt.globalPos()


    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x() , self.y() + delta.y())
        self.oldPos = evt.globalPos()



    def weather_info (self):
        if self.json_info['cod'] == '200' :
            print(self.json_info)
            temp       = self.json_info['main']
            min_temp   = int(float(temp['temp_min']) - 273.15)
            max_temp   = int(float(temp['temp_max']) - 273.15)
            temp_now   = int(float(temp['temp']) - 273.15)
            humidity   = str(temp['humidity']) + ' %'
            pressure   = temp['pressure']
            sunrise    = time.strftime('%I:%M:%S' , time.gmtime(self.json_info['sys']['sunrise'] - 21600))
            sunset     = time.strftime('%I:%M:%S' , time.gmtime(self.json_info['sys']['sunset'] - 21600))
            wind_speed = self.json_info['wind']['speed']
            name       = self.json_info['name']
            wtr        = self.json_info['weather']
            condition  = wtr[0]['description']

            self.ui.label_min_temp.setText( "Min temp :            %s"%min_temp)
            self.ui.label_pressure.setText( "Pressure :            %s"%pressure)
            self.ui.label_sunset.setText("Sunset :            %s"%sunset)
            self.ui.label_wind_speed.setText( "Wind speed :            %s"%wind_speed)
            self.ui.label_max_temp.setText( "Max temp :            %s"%max_temp)
            self.ui.label_humidity.setText( "Humidity :            %s" %humidity)
            self.ui.label_sunrise.setText( "Sunrise :            %s" %sunrise)
            self.ui.label_condition.setText( "Condition :            %s" %condition)
            self.ui.label_temp_now.setText( "%ic" %temp_now)
            self.ui.label_city.setText( name )        
        else :
            print(self.json_info['cod'])

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Weather()
    ui.show()
    sys.exit(app.exec_())
