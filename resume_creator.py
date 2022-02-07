# PDF Resume Creator
# Create a python program that will create your personal resume in PDF format
# All personal details are stored in a JSON file
# Your program should read the JSON file and write the details in the PDF
    
import json
with open('details.json', 'r') as dataFile:
    resumeDetails = json.load(dataFile)

print(resumeDetails)
