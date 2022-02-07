# PDF Resume Creator
# Create a python program that will create your personal resume in PDF format
# All personal details are stored in a JSON file
# Your program should read the JSON file and write the details in the PDF

import json
from fpdf import FPDF

# reading json file
with open('details.json') as dataFile:
    resumeDetails = json.load(dataFile)

# retrieving data from json file
# Personal Information
name = resumeDetails["name"]
address = resumeDetails["address"]
# Contact Information
number = resumeDetails["contactNumber"]

# creating pdf
resume = FPDF("P", "cm",)
resume.add_page()
resume.set_font("Arial", "B", 18)
resume.set_fill_color(181,252,201)

resume.cell(0, 5, "              " + name, ln=1, align="L", fill=1)
#pdf.image('idpic.jpg', 15, 1, 5)

# output pdf
resume.output("MERQUE_JOHNRIC.pdf")