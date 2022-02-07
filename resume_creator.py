# PDF Resume Creator
# Create a python program that will create your personal resume in PDF format
# All personal details are stored in a JSON file
# Your program should read the JSON file and write the details in the PDF

import email
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
sex = resumeDetails["sex"]

# Contact Information
number = resumeDetails["contactNumber"]
emailAd = resumeDetails["emailAddress"]
facebook = resumeDetails["Facebook"]

# Education
education = resumeDetails["education"]
university = resumeDetails["university"]

# Skills
skill1 = resumeDetails["computer"][0]
skill2 = resumeDetails["computer"][1]
skill3 = resumeDetails["computer"][2]
skillNt1 = resumeDetails["nonTechnical"][0]
skillNt2 = resumeDetails["nonTechnical"][1]

# creating pdf
resume = FPDF('P', 'cm', 'A4')
resume.add_page()

# customizing header
resume.set_font("Arial", "B", 25)
resume.set_text_color(48,51,49)
resume.set_fill_color(141,252,209)
resume.cell(20, 5,name, ln=1, align="C", fill=1)
resume.image('resumepic.jpg',0, 1, 5)

# inserting personal information details
resume.set_text_color(255,255,255)
resume.set_fill_color(48,51,49)
resume.set_font("Arial", "", 18)
resume.cell(20,2, "Personal Information", align="L", ln=1, fill=1)
# specific 
resume.set_font_size(14)
resume.set_text_color(48,51,49)
resume.cell(0,0.75, "Age: " + age, align="L", ln=1, fill=0)
resume.cell(0,0.75, "Address: " + address, align="L", ln=1, fill=0)
resume.cell(0,0.75, "Sex: " + sex, align="L", ln=1, fill=0)

# inserting contact information details
resume.set_text_color(255,255,255)
resume.set_font("Arial", "", 18)
resume.cell(20,1, "Contact Information", align="L", ln=1, fill=1)
# specific
resume.set_font_size(14)
resume.set_text_color(48,51,49)
resume.cell(0,0.75, "Contact Number: " + number, align="L", ln=1, fill=0)
resume.cell(0,0.75, "Email Address: " + emailAd, align="L", ln=1, fill=0)
resume.cell(0,0.75, "Facebook Account: " + facebook, align="L", ln=1, fill=0)

# inserting education details
resume.set_text_color(255,255,255)
resume.set_font("Arial", "", 18)
resume.cell(20,1, "Education", align="L", ln=1, fill=1)
# specific
resume.set_font_size(14)
resume.set_text_color(48,51,49)
resume.cell(0,0.75, "Degree Course: " + education, align="L", ln=1, fill=0)
resume.cell(0,0.75, "School: " + university, align="L", ln=1, fill=0)

# inserting skill details
resume.set_text_color(255,255,255)
resume.set_font("Arial", "", 18)
resume.cell(20,1, "Job Skills", align="L", ln=1, fill=1)
# specific
resume.set_font_size(14)
resume.set_text_color(48,51,49)
resume.cell(0,0.75, skill1, align="L", ln=1, fill=0)
resume.cell(0,0.75, skill2, align="L", ln=1, fill=0)
resume.cell(0,0.75, skill3, align="L", ln=1, fill=0)

resume.set_text_color(255,255,255)
resume.set_font("Arial", "", 18)
resume.cell(20,1, "Non-technical Skills", align="L", ln=1, fill=1)
# specific
resume.set_font_size(14)
resume.set_text_color(48,51,49)
resume.cell(0,0.75, skillNt1, align="L", ln=1, fill=0)
resume.cell(0,0.75, skillNt2, align="L", ln=1, fill=0)

# output pdf
resume.output("MERQUE_JOHNRIC.pdf")