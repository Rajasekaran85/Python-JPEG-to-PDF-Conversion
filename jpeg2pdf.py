import sys
import img2pdf
import os

print("\n JPG to PDF Conversion \n")

# img2pdf library used
# Enter the JPG file location
# After tool execution converted the PDF files will created in the "PDF" folder of the same tif file path

filepath = input(" Enter the file path: ")

directory = "PDF"

output = filepath + "\\" + directory

if os.path.exists(output):
    pass
else:
    os.mkdir(output)

for fname in os.listdir(filepath):
	if not fname.endswith(".jpg"):
		continue
	sp = os.path.splitext(fname)[0] 
	path = os.path.join(filepath, fname) 
	jpegname =  filepath + "\\" + fname
	pdfname = output + "\\" + sp + ".pdf"
	print(pdfname)

	# creating pdf file
	file = open(pdfname, "wb")

	# converting image into pdf
	convpdf = img2pdf.convert(jpegname)

	# writing the pdf output file
	file.write(convpdf)

	# closing the pdf file
	file.close

print("\n\nPDF Conversion Completed")
