from PyQt5 import QtWidgets, QtGui, QtCore
from generated.ccmain_temp import Ui_MainWindow
from about import About
from typing import Dict
import requests, sys


class Main(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.about: About = None
        self.norm_table: Dict[int: float] = None
        self.btc_table: Dict[int: float] = None

        self.num_from_c = None

        self.norm_rates()
        self.init_ui()
        self.signals()
        self.separator(1)
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
        self.actionDot.triggered.connect(lambda: self.separator(1))
        self.actionComma.triggered.connect(lambda: self.separator(22))
        self.actionAbout.triggered.connect(self.initiate_about)

    @property
    def index_first_c(self) -> int:
        return self.firstC.currentIndex()

    @property
    def index_second_c(self) -> int:
        return self.secondC.currentIndex()

    @property
    def index_second_c_btc(self) -> int:
        return self.secondC_2.currentIndex()

    def change_rates(self):
        index_one, index_two = self.index_first_c, self.index_second_c
        self.secondC.setCurrentIndex(index_one)
        self.firstC.setCurrentIndex(index_two)

    def norm_rates(self):
        try:
            params_for_var = 'USD,BGN,RUB,HRK,INR,NOK,PLN,TRY'
            request_api = requests.get(f'https://api.exchangeratesapi.io/latest?symbols={params_for_var}', timeout=2)
            norm_value = request_api.json()
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, 'Connection Error',
                                           'There was a network error.'
                                           '\nTry to download the rates manually'
                                           '\nby pressing <Rates> button in <Help> menu'
                                           )
            return None
        except:
            return None

        self.norm_table = {
            0: 1,
            1: norm_value['rates']['USD'],
            2: norm_value['rates']['BGN'],
            3: norm_value['rates']['RUB'],
            4: norm_value['rates']['HRK'],
            5: norm_value['rates']['INR'],
            6: norm_value['rates']['NOK'],
            7: norm_value['rates']['PLN'],
            8: norm_value['rates']['TRY'],
        }

    def btc_rates(self):
        try:
            request_api = requests.get('https://blockchain.info/ticker')
            btc_value = request_api.json()
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, 'Connection Error',
                                           'There was a network error.'
                                           '\nTry to download the rates manually'
                                           '\nby pressing <Rates> button in <Help> menu'
                                           )
            return None
        except:
            return None

        self.btc_table = {
            0: btc_value['EUR']['last'],
            1: btc_value['USD']['last'],
            2: btc_value['USD']['last'],
            3: btc_value['RUB']['last'],
            4: btc_value['INR']['last'],
        }

    def norm_operations(self):
        if len(self.firstCINP.text()) == 0:
            self.secondCOUT.clear()
            return None

        try:
            str_inp = self.firstCINP.text()
            self.num_from_c = float(str_inp.replace(',', '.'))

            out = self.rates_return()

            format_and_round = format(round(out, 3), ',')
            self.secondCOUT.setText(format_and_round)
        except:
            return None

    def btc_operations(self):
        if len(self.firstCINP_2.text()) == 0:
            self.secondCOUT_2.clear()
            return None

        try:
            str_inp = self.firstCINP_2.text()
            self.num_from_c = float(str_inp.replace(',', '.'))

            out = self.btc_return()

            format_and_round = format(round(out, 3), ',')
            self.secondCOUT_2.setText(format_and_round)
        except:
            return None

    def rates_return(self) -> float:
        return (self.num_from_c * self.norm_table[self.index_second_c]) / self.norm_table[self.index_first_c]

    def btc_return(self) -> float:
        if self.secondC_2.currentIndex() == 2:
            return (self.num_from_c * self.btc_table[0]) * self.norm_table[2]
        return self.num_from_c * self.btc_table[self.index_second_c_btc]

    def separator(self, sep: int):
        var = QtGui.QDoubleValidator(QtCore.QLocale.setDefault(QtCore.QLocale(sep)))
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

    def initiate_about(self):
        self.about = About()
        self.about.setFixedSize(398, 280)
        self.about.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Main()
    sys.exit(app.exec_())