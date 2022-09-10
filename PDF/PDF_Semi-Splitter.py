from PyPDF2 import PdfMerger

merger = PdfMerger()

## odd pages only
merger.append("Sample.pdf", pages=(0,194,2))

merger.write("Output.pdf")
merger.close()