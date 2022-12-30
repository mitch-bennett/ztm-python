import PyPDF2
import sys
import pdb

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)


# grab all pdfs in argument inputs into a list of inputs
inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        # pdb.set_trace()
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")


pdf_combiner(inputs)
