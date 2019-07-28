import os
import tabula

# Windows automated builds are failing.. disabling the test
if 'windir' in os.environ:
  return 0

# Read remote pdf into DataFrame
df2 = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")
