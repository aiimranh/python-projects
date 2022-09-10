from PyPDF2 import PdfMerger

pdfs = ["test1.pdf", "test2.pdf", "test3.pdf"]

merger = PdfMerger()
for pdf in pdfs:
	merger.append(pdf)

merger.write("test.pdf")
merger.close()