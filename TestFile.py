from barcode import ISBN13
from barcode.writer import ImageWriter



num = '978456752421'

book_barcode = ISBN13(num, writer=ImageWriter())

outputFileFolder = 'barcode/'
outputFile = outputFileFolder + 'isbn13_barcode'

book_barcode.save(outputFile)