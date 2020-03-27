from PyQt5 import QtWidgets, QtGui, QtCore
import ccmain, about
import requests, sys


class Main(ccmain.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.norm_rates()
        self.init_ui()
        self.signals()
        self.separator_dot()
        self.cc_show()

    def init_ui(self):
        self.setupUi(self)
        self.setFixedSize(290, 200)
        self.menuSeparator.setToolTipsVisible(True)
        self.actiontext.setToolTip('By default it\'s Dot')
        self.show()

    def signals(self):
        self.btc.triggered.connect(self.cc_show)
        self.exchange.clicked.connect(self.change_rates)
        self.btc_rates_btn.clicked.connect(self.btc_rates)
        self.firstC.currentIndexChanged.connect(self.norm_operations)
        self.secondC.currentIndexChanged.connect(self.norm_operations)
        self.secondC_2.currentIndexChanged.connect(self.btc_operations)
        self.firstCINP.textChanged.connect(self.norm_operations)
        self.firstCINP_2.textChanged.connect(self.btc_operations)
        self.actionRates.triggered.connect(self.norm_rates)
        self.actionDot.triggered.connect(self.separator_dot)
        self.actionComma.triggered.connect(self.separator_comma)
        self.actionAbout.triggered.connect(self.about)

    def indexes_first_c(self):
        return self.firstC.currentIndex()

    def indexes_second_c(self):
        return self.secondC.currentIndex()

    def indexes_second_c_btc(self):
        return self.secondC_2.currentIndex()

    def change_rates(self):
        index_one = self.indexes_first_c()
        index_two = self.indexes_second_c()
        self.secondC.setCurrentIndex(index_one)
        self.firstC.setCurrentIndex(index_two)

    def norm_rates(self):
        try:
            params_for_var = 'USD,BGN,RUB,HRK,INR,NOK,PLN,TRY'
            request_api = requests.get(f'https://api.exchangeratesapi.io/latest?symbols={params_for_var}', timeout=2)
            request_api_json = request_api.json()
            self.norm_value = request_api_json
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, 'Connection Error',
                                           'There was a network error.'
                                           '\nTry to download the rates manually'
                                           '\nby pressing <Rates> button in <Help> menu'
                                           )
            return None
        except:
            return None

        global norm_table

        norm_table = {
            0: 1,
            1: self.norm_value['rates']['USD'],
            2: self.norm_value['rates']['BGN'],
            3: self.norm_value['rates']['RUB'],
            4: self.norm_value['rates']['HRK'],
            5: self.norm_value['rates']['INR'],
            6: self.norm_value['rates']['NOK'],
            7: self.norm_value['rates']['PLN'],
            8: self.norm_value['rates']['TRY'],
        }

    def btc_rates(self):
        try:
            request_api = requests.get('https://blockchain.info/ticker')
            request_api_json = request_api.json()
            self.btc_value = request_api_json
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, 'Connection Error',
                                           'There was a network error.'
                                           '\nTry to download the rates manually'
                                           '\nby pressing <Rates> button in <Help> menu'
                                           )
            return None
        except:
            return None

        global btc_table

        btc_table = {
            0: self.btc_value['EUR']['last'],
            1: self.btc_value['USD']['last'],
            2: self.btc_value['USD']['last'],
            3: self.btc_value['RUB']['last'],
            4: self.btc_value['INR']['last'],
        }

    def norm_operations(self):
        if len(self.firstCINP.text()) == 0:
            self.secondCOUT.clear()
            return None

        try:
            global num_from_c

            str_inp = str(self.firstCINP.text())
            num_from_c = float(str_inp.replace(',', '.'))

            out = self.rates_return()

            format_and_round = format(round(out, 3), ',')
            self.secondCOUT.setText(str(format_and_round))
        except:
            return None

    def btc_operations(self):
        if len(self.firstCINP_2.text()) == 0:
            self.secondCOUT_2.clear()
            return None

        try:
            global num_from_c

            str_inp = str(self.firstCINP_2.text())
            num_from_c = float(str_inp.replace(',', '.'))

            out = self.btc_return()

            format_and_round = format(round(out, 3), ',')
            self.secondCOUT_2.setText(str(format_and_round))
        except:
            return None

    def rates_return(self):
        return (num_from_c * norm_table[self.indexes_second_c()]) / norm_table[self.indexes_first_c()]

    def btc_return(self):
        if self.secondC_2.currentIndex() == 2:
            return (num_from_c * btc_table[0]) * norm_table[2]
        else:
            return num_from_c * btc_table[self.indexes_second_c_btc()]

    def separator_dot(self):
        var = QtGui.QDoubleValidator(QtCore.QLocale.setDefault(QtCore.QLocale(1)))
        self.firstCINP.clear()
        self.secondCOUT.clear()
        self.firstCINP_2.clear()
        self.secondCOUT_2.clear()
        self.firstCINP.setValidator(var)
        self.firstCINP_2.setValidator(var)

    def separator_comma(self):
        var = QtGui.QDoubleValidator(QtCore.QLocale.setDefault(QtCore.QLocale(22)))
        self.firstCINP.clear()
        self.secondCOUT.clear()
        self.firstCINP_2.clear()
        self.secondCOUT_2.clear()
        self.firstCINP.setValidator(var)
        self.firstCINP_2.setValidator(var)

    def cc_show(self):
        if self.btc.isChecked():
            self.frame_8.show()
            self.line.show()
            self.setFixedSize(290, 370)
            self.btc_rates()
        else:
            self.frame_8.close()
            self.line.close()
            self.firstCINP_2.clear()
            self.secondCOUT_2.clear()
            self.setFixedSize(290, 200)

    def about(self):
        self.abt = About()
        self.abt.setFixedSize(398, 280)
        self.abt.show()


class About(about.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.setModal(True)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Main()
    sys.exit(app.exec_())
