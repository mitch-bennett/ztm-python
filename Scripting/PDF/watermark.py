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


# # grab all pdfs in argument inputs into a list of inputs
# inputs = sys.argv[1:]


# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         # pdb.set_trace()
#         print(pdf)
#         merger.append(pdf)
#     merger.write("super.pdf")

# pdf_combiner(inputs)

# solution mainly from https://pypdf2.readthedocs.io/en/latest/user/add-watermark.html


def watermark(content, stamp):
    reader_content = PyPDF2.PdfFileReader((content))
    pages = list(range(0, len(reader_content.pages)))

    writer = PyPDF2.PdfFileWriter()

    reader_stamp = PyPDF2.PdfFileReader((stamp))
    image_page = reader_stamp.pages[0]

    for page in pages:
        content_page = reader_content.pages[page]
        mediabox = content_page.mediabox

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open("watermarked.pdf", "wb") as fp:
        writer.write(fp)


watermark("super.pdf", "wtr.pdf")


# solution code below....-------------

# import PyPDF2

# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
#   page = template.getPage(i)
#   page.mergePage(watermark.getPage(0))
#   output.addPage(page)

#   with open('watermarked_output.pdf', 'wb') as file:
#     output.write(file)
