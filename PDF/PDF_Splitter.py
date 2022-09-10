from PyPDF2 import PdfMerger

## first odd pages , then even pages.
for i in [0,1]:
	merger = PdfMerger()
	merger.append("Sample.pdf",pages=(0,194,2))

	merger.write("Output"+str(i)+".pdf")
	merger.close()