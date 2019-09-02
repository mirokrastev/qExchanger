from PyQt5 import QtWidgets, QtGui, QtCore
import ccmain, about
import qdarkstyle, requests, sys


class Programa(ccmain.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.signals()
        self.ccshow()
        self.sepdot()
        self.rates()

    def initUI(self):
        self.setupUi(self)
        self.setFixedSize(290, 216)
        self.menuSeparator.setToolTipsVisible(True)
        self.actiontext.setToolTip('By default it\'s Dot')
        self.show()

    def signals(self):
        self.themes.triggered.connect(self.darktheme)
        self.btc.triggered.connect(self.ccshow)
        self.exchange.clicked.connect(self.currencies)
        self.exchange_2.clicked.connect(self.bitcoin)
        self.actionAbout.triggered.connect(self.about)
        self.actionDot.triggered.connect(self.sepdot)
        self.actionComma.triggered.connect(self.sepcomma)
        self.firstCINP.textChanged.connect(self.currencies)
        self.firstCINP_2.textChanged.connect(self.bitcoin)
        self.firstC.currentIndexChanged.connect(self.currencies)
        self.secondC.currentIndexChanged.connect(self.currencies)
        self.secondC_2.currentIndexChanged.connect(self.bitcoin)
        self.actionRates.triggered.connect(self.rates)
        if len(self.firstCINP.text()) == 0:
            self.secondCOUT.clear()
        if len(self.firstCINP_2.text()) == 0:
            self.secondCOUT_2.clear()

    def rates(self):
        try:
            params = {
                'symbols': {
                    "USD",
                    "BGN",
                    "RUB",
                    "HRK",
                    "INR",
                    "NOK",
                    "PLN",
                    "TRY"
                },
            }

            zdr = requests.get('https://api.exchangeratesapi.io/latest', params, timeout=2)
            q = zdr.json()
            self.value = q
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, 'Connection Error',
                                           'There was an network error.'
                                           '\nTry to download the rates manually'
                                           '\nby pressing <Rates> button in <Help> menu'
                                           )
            self.signals()
        except:
            self.signals()

    def btcrates(self):
        try:
            zdr = requests.get('https://blockchain.info/ticker')
            q = zdr.json()
            self.btcvalue = q
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, 'Connection Error',
                                           'There was an network error.'
                                           '\nTry to restart the program'
                                           '\nor download the rates manually.'
                                           )
            self.signals()
        except:
            self.signals()

    def sepdot(self):
        zdr = QtGui.QDoubleValidator(QtCore.QLocale.setDefault(QtCore.QLocale(1)))
        self.firstCINP.setValidator(zdr)
        self.firstCINP.clear()
        self.secondCOUT.clear()
        self.firstCINP_2.setValidator(zdr)
        self.firstCINP_2.clear()
        self.secondCOUT_2.clear()

    def sepcomma(self):
        zdr = QtGui.QDoubleValidator(QtCore.QLocale.setDefault(QtCore.QLocale(22)))
        self.firstCINP.setValidator(zdr)
        self.firstCINP.clear()
        self.secondCOUT.clear()
        self.firstCINP_2.setValidator(zdr)
        self.firstCINP_2.clear()
        self.secondCOUT_2.clear()

    def darktheme(self):
        if self.themes.isChecked():
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        else:
            self.setStyleSheet('WindowsVista')

    def ccshow(self):
        if self.btc.isChecked():
            self.frame_8.show()
            self.line.show()
            self.setFixedSize(290, 397.9)
            self.btcrates()
        else:
            self.frame_8.close()
            self.line.close()
            self.firstCINP_2.clear()
            self.secondCOUT_2.clear()
            self.setFixedSize(290, 216)

    def about(self):
        if self.themes.isChecked():
            self.abt = AboutUi()
            self.abt.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.abt.setFixedSize(398, 280)
            self.abt.line.setGeometry(90, 58, 90, 8)
            self.abt.line_2.setGeometry(90, 109, 90, 8)
            self.abt.text.setGeometry(90, 10, 260, 43)
            self.abt.show()
        else:
            self.abt = AboutUi()
            self.abt.setFixedSize(398, 280)
            self.abt.show()

    def currencies(self):
        try:
            a = str(self.firstCINP.text())
            n = float(a.replace(',', '.'))
            if self.firstC.currentIndex() == 0:
                if self.secondC.currentIndex() == 0:
                    c = round(n * self.value['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = round(n * self.value['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = round(n * self.value['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = round(n * self.value['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = round(n * self.value['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = round(n * self.value['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = round(n * self.value['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = round(n * self.value['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 1:
                if self.secondC.currentIndex() == 0:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n / self.value['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = n * self.value['rates']['BGN']
                    h = round(c / self.value['rates']['USD'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = n * self.value['rates']['RUB']
                    h = round(c / self.value['rates']['USD'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = n * self.value['rates']['HRK']
                    h = round(c / self.value['rates']['USD'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = n * self.value['rates']['INR']
                    h = round(c / self.value['rates']['USD'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = n * self.value['rates']['NOK']
                    h = round(c / self.value['rates']['USD'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = n * self.value['rates']['PLN']
                    h = round(c / self.value['rates']['USD'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = n * self.value['rates']['TRY']
                    h = round(c / self.value['rates']['USD'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 2:
                if self.secondC.currentIndex() == 0:
                    c = n * self.value['rates']['USD']
                    h = round(c / self.value['rates']['BGN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n / self.value['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = n * self.value['rates']['RUB']
                    h = round(c / self.value['rates']['BGN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = n * self.value['rates']['HRK']
                    h = round(c / self.value['rates']['BGN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = n * self.value['rates']['INR']
                    h = round(c / self.value['rates']['BGN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = n * self.value['rates']['NOK']
                    h = round(c / self.value['rates']['BGN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = n * self.value['rates']['PLN']
                    h = round(c / self.value['rates']['BGN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = n * self.value['rates']['TRY']
                    h = round(c / self.value['rates']['BGN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 3:
                if self.secondC.currentIndex() == 0:
                    c = n * self.value['rates']['USD']
                    h = round(c / self.value['rates']['RUB'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n / self.value['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = n * self.value['rates']['BGN']
                    h = round(c / self.value['rates']['RUB'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = n * self.value['rates']['HRK']
                    h = round(c / self.value['rates']['RUB'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = n * self.value['rates']['INR']
                    h = round(c / self.value['rates']['RUB'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = n * self.value['rates']['NOK']
                    h = round(c / self.value['rates']['RUB'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = n * self.value['rates']['PLN']
                    h = round(c / self.value['rates']['RUB'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = n * self.value['rates']['TRY']
                    h = round(c / self.value['rates']['RUB'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 4:
                if self.secondC.currentIndex() == 0:
                    c = n * self.value['rates']['USD']
                    h = round(c / self.value['rates']['HRK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n / self.value['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = n * self.value['rates']['BGN']
                    h = round(c / self.value['rates']['HRK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = n * self.value['rates']['RUB']
                    h = round(c / self.value['rates']['HRK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = n * self.value['rates']['INR']
                    h = round(c / self.value['rates']['HRK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = n * self.value['rates']['NOK']
                    h = round(c / self.value['rates']['HRK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = n * self.value['rates']['PLN']
                    h = round(c / self.value['rates']['HRK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = n * self.value['rates']['TRY']
                    h = round(c / self.value['rates']['HRK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 5:
                if self.secondC.currentIndex() == 0:
                    c = n * self.value['rates']['USD']
                    h = round(c / self.value['rates']['INR'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n / self.value['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = n * self.value['rates']['BGN']
                    h = round(c / self.value['rates']['INR'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = n * self.value['rates']['RUB']
                    h = round(c / self.value['rates']['INR'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = n * self.value['rates']['HRK']
                    h = round(c / self.value['rates']['INR'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = n * self.value['rates']['NOK']
                    h = round(c / self.value['rates']['INR'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = n * self.value['rates']['PLN']
                    h = round(c / self.value['rates']['INR'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = n * self.value['rates']['TRY']
                    h = round(c / self.value['rates']['INR'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 6:
                if self.secondC.currentIndex() == 0:
                    c = n * self.value['rates']['USD']
                    h = round(c / self.value['rates']['NOK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n / self.value['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = n * self.value['rates']['BGN']
                    h = round(c / self.value['rates']['NOK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = n * self.value['rates']['RUB']
                    h = round(c / self.value['rates']['NOK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = n * self.value['rates']['HRK']
                    h = round(c / self.value['rates']['NOK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = n * self.value['rates']['INR']
                    h = round(c / self.value['rates']['NOK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = n * self.value['rates']['PLN']
                    h = round(c / self.value['rates']['NOK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = n * self.value['rates']['TRY']
                    h = round(c / self.value['rates']['NOK'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 7:
                if self.secondC.currentIndex() == 0:
                    c = n * self.value['rates']['USD']
                    h = round(c / self.value['rates']['PLN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n / self.value['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = n * self.value['rates']['BGN']
                    h = round(c / self.value['rates']['PLN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = n * self.value['rates']['RUB']
                    h = round(c / self.value['rates']['PLN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = n * self.value['rates']['HRK']
                    h = round(c / self.value['rates']['PLN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = n * self.value['rates']['INR']
                    h = round(c / self.value['rates']['PLN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = n * self.value['rates']['NOK']
                    h = round(c / self.value['rates']['PLN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = n * self.value['rates']['TRY']
                    h = round(c / self.value['rates']['PLN'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 8:
                if self.secondC.currentIndex() == 0:
                    c = n * self.value['rates']['USD']
                    h = round(c / self.value['rates']['TRY'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n / self.value['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = n * self.value['rates']['BGN']
                    h = round(c / self.value['rates']['TRY'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = n * self.value['rates']['RUB']
                    h = round(c / self.value['rates']['TRY'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = n * self.value['rates']['HRK']
                    h = round(c / self.value['rates']['TRY'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = n * self.value['rates']['INR']
                    h = round(c / self.value['rates']['TRY'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = n * self.value['rates']['NOK']
                    h = round(c / self.value['rates']['TRY'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = n * self.value['rates']['PLN']
                    h = round(c / self.value['rates']['TRY'], 2)
                    b = format(h, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
        except:
            self.signals()

    def bitcoin(self):
        try:
            a = str(self.firstCINP_2.text())
            n = float(a.replace(',', '.'))
            if self.secondC_2.currentIndex() == 0:
                c = round(n * self.btcvalue['USD']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 1:
                c = round(n * self.btcvalue['EUR']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 2:
                c = n * self.btcvalue['USD']['last']
                g = c * self.value['rates']['BGN']
                h = round(g / self.value['rates']['USD'], 2)
                b = format(h, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 3:
                c = round(n * self.btcvalue['RUB']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 4:
                c = round(n * self.btcvalue['INR']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
        except:
            self.signals()


class AboutUi(about.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.setupUi(self)
        self.setModal(True)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Programa()
    sys.exit(app.exec_())
