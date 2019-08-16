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
        else:
            self.frame_8.close()
            self.line.close()
            self.setFixedSize(290, 216)

    def about(self):
        if self.themes.isChecked():
            self.a = AboutUi()
            self.a.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.a.setFixedSize(398, 280)
            self.a.line.setGeometry(90, 58, 90, 8)
            self.a.line_2.setGeometry(90, 109, 90, 8)
            self.a.show()
        else:
            self.a = AboutUi()
            self.a.setFixedSize(398, 280)
            self.a.show()

    def currencies(self):
        try:
            a = str(self.firstCINP.text())
            n = float(a.replace(',', '.'))
            if self.firstC.currentIndex() == 0:
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
                    'base': 'EUR'
                }

                zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                q = zdr.json()
                if self.secondC.currentIndex() == 0:
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = round(n * q['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = round(n * q['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = round(n * q['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = round(n * q['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = round(n * q['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = round(n * q['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = round(n * q['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 1:
                params = {
                    'symbols': {
                        "EUR",
                        "BGN",
                        "RUB",
                        "HRK",
                        "INR",
                        "NOK",
                        "PLN",
                        "TRY"
                    },
                    'base': 'USD'
                }

                zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                q = zdr.json()
                if self.secondC.currentIndex() == 0:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = round(n * q['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = round(n * q['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = round(n * q['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = round(n * q['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = round(n * q['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = round(n * q['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = round(n * q['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 2:
                params = {
                    'symbols': {
                        "EUR",
                        "USD",
                        "RUB",
                        "HRK",
                        "INR",
                        "NOK",
                        "PLN",
                        "TRY"
                    },
                    'base': 'BGN'
                }

                zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                q = zdr.json()
                if self.secondC.currentIndex() == 0:
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = round(n * q['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = round(n * q['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = round(n * q['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = round(n * q['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = round(n * q['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = round(n * q['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 3:
                params = {
                    'symbols': {
                        "EUR",
                        "USD",
                        "BGN",
                        "HRK",
                        "INR",
                        "NOK",
                        "PLN",
                        "TRY"
                    },
                    'base': 'RUB'
                }

                zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                q = zdr.json()
                if self.secondC.currentIndex() == 0:
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = round(n * q['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = round(n * q['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = round(n * q['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = round(n * q['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = round(n * q['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = round(n * q['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 4:
                params = {
                    'symbols': {
                        "EUR",
                        "USD",
                        "BGN",
                        "RUB",
                        "INR",
                        "NOK",
                        "PLN",
                        "TRY"
                    },
                    'base': 'HRK'
                }

                zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                q = zdr.json()
                if self.secondC.currentIndex() == 0:
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = round(n * q['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = round(n * q['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = round(n * q['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = round(n * q['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = round(n * q['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = round(n * q['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 5:
                params = {
                    'symbols': {
                        "EUR",
                        "USD",
                        "BGN",
                        "RUB",
                        "HRK",
                        "NOK",
                        "PLN",
                        "TRY"
                    },
                    'base': 'INR'
                }

                zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                q = zdr.json()
                if self.secondC.currentIndex() == 0:
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = round(n * q['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = round(n * q['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = round(n * q['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = round(n * q['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = round(n * q['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = round(n * q['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 6:
                params = {
                    'symbols': {
                        "EUR",
                        "USD",
                        "BGN",
                        "RUB",
                        "HRK",
                        "INR",
                        "PLN",
                        "TRY"
                    },
                    'base': 'NOK'
                }

                zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                q = zdr.json()
                if self.secondC.currentIndex() == 0:
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = round(n * q['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = round(n * q['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = round(n * q['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = round(n * q['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = round(n * q['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = round(n * q['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 7:
                params = {
                    'symbols': {
                        "EUR",
                        "USD",
                        "BGN",
                        "RUB",
                        "HRK",
                        "INR",
                        "NOK",
                        "TRY"
                    },
                    'base': 'PLN'
                }

                zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                q = zdr.json()
                if self.secondC.currentIndex() == 0:
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = round(n * q['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = round(n * q['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = round(n * q['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = round(n * q['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = round(n * q['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    c = round(n * q['rates']['TRY'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            elif self.firstC.currentIndex() == 8:
                params = {
                    'symbols': {
                        "EUR",
                        "USD",
                        "BGN",
                        "RUB",
                        "HRK",
                        "INR",
                        "NOK",
                        "PLN"
                    },
                    'base': 'TRY'
                }

                zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                q = zdr.json()
                if self.secondC.currentIndex() == 0:
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    c = round(n * q['rates']['BGM'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 3:
                    c = round(n * q['rates']['RUB'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 4:
                    c = round(n * q['rates']['HRK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 5:
                    c = round(n * q['rates']['INR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 6:
                    c = round(n * q['rates']['NOK'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 7:
                    c = round(n * q['rates']['PLN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 8:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, 'Connection Error',
                                           'There was an network error. Please check'
                                           '\nyour connection and try again. If the problem'
                                           '\nstill exists, try again later'
                                           )
            self.signals()
        except:
            self.signals()

    def bitcoin(self):
        try:
            a = str(self.firstCINP_2.text())
            n = float(a.replace(',', '.'))
            zdr = requests.get('https://blockchain.info/ticker')
            q = zdr.json()
            if self.secondC_2.currentIndex() == 0:
                c = round(n * q['USD']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 1:
                c = round(n * q['EUR']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 2:
                hui = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
                w = hui.json()
                c = n * q['USD']['last']
                h = round(c * w['rates']['BGN'], 2)
                b = format(h, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 3:
                c = round(n * q['RUB']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 4:
                c = round(n * q['INR']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, 'Connection Error',
                                           'There was a network error. Please check'
                                           '\nyour connection and try again. If the problem'
                                           '\nstill exists, try again later'
                                           )
            self.signals()
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
