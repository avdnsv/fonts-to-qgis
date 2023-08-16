import os
from qgis.PyQt.QtGui import QFontDatabase

# An absolute path to your local fonts
path_folder = '/path/to/the/folder'

# Get all fonts in the folder
fonts = os.listdir(path_folder)

# Get QFontDatabase object
qfdb = QFontDatabase()

# Iterate over each font with its own absolute path and add to QGIS
for font in fonts:
    qfdb.addApplicationFont(os.path.join(path_folder, font))
