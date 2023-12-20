import sys
from PySide6.QtWidgets import QApplication, QLabel

# Create the application
app = QApplication(sys.argv)

# Create a label widget
label = QLabel("Hello, PySide6!")

# Show the label
label.show()

# Run the application event loop
sys.exit(app.exec())
