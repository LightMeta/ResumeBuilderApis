
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

class CreatePdf:
    
    def __init__(self,data):

        self.name = data['name']
        self.address = data['address']
        self.number = data['number']
        self.email = data['email']
        self.location = data['location']
        self.experience = data['experience']
        self.techskills = data['TECH_SKILLS']

    def create_pdf(self):

        fileName = '{}.pdf'.format(self.name)
        documentTitle = '************* {} Resume ************* '.format(self.name)
        title = 'Technology'
        subTitle = '{} Resume'.format(self.name)
        textLines = [
            'NAME                   {} '.format(self.name),
            'ADDRESS                {} '.format(self.address),
            'NUMBER                 {} '.format(self.number),
            'EMAIL                  {} '.format(self.email),
            'LOCATION               {} '.format(self.location),
            'EXPERIENCE             {} '.format(self.experience),
            'TECHSKILLS             {} '.format(self.techskills),
        ]
        
        pdf = canvas.Canvas(fileName)
        

        pdf.setTitle(documentTitle)
        

 
        pdfmetrics.registerFont(
            TTFont('abc', 'FreeMono.ttf')
        )

        pdf.setFont('abc', 26)
        pdf.drawCentredString(300, 770, title)
        

        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 24)
        pdf.drawCentredString(290, 720, subTitle)

        pdf.line(30, 710, 550, 710)

        text = pdf.beginText(40, 680)
        text.setFont("Courier", 18)
        text.setFillColor(colors.blueviolet)
        for line in textLines:
            text.textLine(line)
        pdf.drawText(text)
        pdf.save()