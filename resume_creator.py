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
age = resumeDetails["age"]
address = resumeDetails["address"]

# Contact Information
number = resumeDetails["contactNumber"]

# creating pdf
resume = FPDF('P', 'cm', 'A4')
resume.add_page()

# customizing header
resume.set_font("Arial", "B", 25)
resume.set_text_color(48,51,49)
resume.set_fill_color(181,252,201)
resume.cell(20, 5,name, ln=1, align="C", fill=1)
resume.image('resumepic.jpg',0, 1, 5)

# inserting personal information details
resume.set_text_color(255,255,255)
resume.set_fill_color(48,51,49)
resume.set_font("Arial", "", 18)
resume.cell(20,1, "Personal Information", align="L", ln=1, fill=1)
# specific details
resume.set_font_size(14)
resume.cell(0,0.75, "age: " + age, align="L", ln=1, fill=0)
resume.cell(0,0.75, "address: " + address, align="L", ln=1, fill=0)

# output pdf
resume.output("MERQUE_JOHNRIC.pdf")