import sys
import img2pdf
import os

print("\n JPEG to PDF Conversion\n")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 19 April 2022 \n\n")

filepath = input(" Enter the file path: ")

#print(filepath)

#filepath = sys.argv[1]
if os.path.isdir(filepath):
    with open(filepath + "\output.pdf", "wb") as f:       # Create the output file name
        imgs = []
       
        for fname in os.listdir(filepath):
            #print(fname)
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(filepath, fname) # path name & jpeg file name 
            #print(path)
            """
            if os.path.isdir(path):              
                continue
            print(os.path.isdir)
            """
            imgs.append(path)
            
            #print(imgs.append)
            
        f.write(img2pdf.convert(imgs))
        
elif os.path.isfile(filepath):
    if filepath.endswith(".jpg"):
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(filepath))
else:
    print("please provide input file path")

