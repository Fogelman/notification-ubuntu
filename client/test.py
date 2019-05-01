import sys
from PyQt5 import QtWidgets, uic


ClasseGraficaBase, ClasseWidgetsBase = uic.loadUiType('main.ui')


class Window(ClasseWidgetsBase, ClasseGraficaBase):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.bt_enviar.clicked.connect(self.paginaHtml)

    def paginaHtml(self):
        texto = self.ln_texto.text()
        html = """
		<!DOCTYPE html>
		<html>
		<head>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script>
		$(document).ready(function(){
		    $("div").animate({fontSize: '50'}, "slow");
		});
		</script>
		</head>
		<body>
		<div style="background:#98bf21;height:fill;width:fill;">%s</div>
		</body>
		</html>
		""" % ('Olá ' + texto + '!!!')
        self.webView.setHtml(html)

        # self.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
sys.exit(app.exec_())
