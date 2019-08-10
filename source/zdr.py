from PyQt5 import QtWidgets, QtGui, QtCore
import ccmain
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
        QtWidgets.QMessageBox.information(self, 'About qExchanger',
                                          'qExchanger is an open sourced project, built with PyQt 5.12.1'
                                          '<br> and licensed under '
                                          "<a href='https://www.gnu.org/licenses/gpl-3.0.txt'>GNU GPLv3</a>"
                                          '<br>'
                                          '<br> The program updates itself using APIs from'
                                          "<br> <a href='https://api.exchangeratesapi.io/latest'>exchangerates</a>"
                                          ' and '
                                          "<a href='https://blockchain.info/ticker'>blockchain</a>"
                                          '<br>'
                                          '<br>You can find this project on '
                                          "<a href='https://github.com/Qiceto/qExchanger'>GitHub</a>"
                                          )

    def currencies(self):
        try:
            a = str(self.firstCINP.text())
            n = float(a.replace(',', '.'))
            if self.firstC.currentIndex() == 0:
                if self.secondC.currentIndex() == 0:
                    params = {
                        'symbols': {
                            "USD",
                            "BGN"
                        },
                        'base': 'EUR'
                    }

                    zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                    q = zdr.json()
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    params = {
                        'symbols': {
                            "USD",
                            "BGN"
                        },
                        'base': 'EUR'
                    }

                    zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                    q = zdr.json()
                    c = round(n * q['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            if self.firstC.currentIndex() == 1:
                if self.secondC.currentIndex() == 0:
                    b = format(n, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    params = {
                        'symbols': {
                            "EUR",
                            "BGN"
                        },
                        'base': 'USD'
                    }

                    zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                    q = zdr.json()
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
                    params = {
                        'symbols': {
                            "EUR",
                            "BGN"
                        },
                        'base': 'USD'
                    }

                    zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                    q = zdr.json()
                    c = round(n * q['rates']['BGN'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
            if self.firstC.currentIndex() == 2:
                if self.secondC.currentIndex() == 0:
                    params = {
                        'symbols': {
                            "EUR",
                            "USD"
                        },
                        'base': 'BGN'
                    }

                    zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                    q = zdr.json()
                    c = round(n * q['rates']['USD'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 1:
                    params = {
                        'symbols': {
                            "EUR",
                            "USD"
                        },
                        'base': 'BGN'
                    }

                    zdr = requests.get('https://api.exchangeratesapi.io/latest', params)
                    q = zdr.json()
                    c = round(n * q['rates']['EUR'], 2)
                    b = format(c, ',')
                    self.secondCOUT.setText(str(b))
                elif self.secondC.currentIndex() == 2:
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
            if self.secondC_2.currentIndex() == 0:
                zdr = requests.get('https://blockchain.info/ticker')
                q = zdr.json()
                c = round(n * q['USD']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 1:
                zdr = requests.get('https://blockchain.info/ticker')
                q = zdr.json()
                c = round(n * q['EUR']['last'], 2)
                b = format(c, ',')
                self.secondCOUT_2.setText(str(b))
            elif self.secondC_2.currentIndex() == 2:
                zdr = requests.get('https://blockchain.info/ticker')
                q = zdr.json()
                c = n * q['USD']['last']
                hui = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
                w = hui.json()
                h = round(c * w['rates']['BGN'], 2)
                b = format(h, ',')
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Programa()
    sys.exit(app.exec_())
