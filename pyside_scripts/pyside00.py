import sys

from PySide2.QtWidgets import QApplication, QMessageBox

# CREATE THE QApplication OBJECT

app=QApplication(sys.argv)
# 865349237
msg_box=QMessageBox()
msg_box.setText("Hello world")
msg_box.show()

sys.exit(msg_box.exec_())
