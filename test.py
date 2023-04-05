import csv

# Define the JSON data
json_data = {
   "promoter_features": "Executive (C-Suite or Cabinet",
   "question2": [
      "Item 1"
   ],
   "question5": "IT and Media",
   "question6": "Item 1",
   "question1": True,
   "question7": True,
   "question8": [
      "Item 1",
      "Item 2",
      "Item 3"
   ],
   "question9": True,
   "question10": True,
   "question11": True,
   "question12": True,
   "question13": "awesome!",
   "question14": True,
   "question15": "awesome!",
   "question16": True,
   "question17": {
      "Row 1": {
         "Column 1": 1
      },
      "Row 2": {
         "Column 1": 2
      },
      "Row 3 ": {
         "Column 1": 1
      },
      "Row 4 ": {
         "Column 1": 1
      },
      "Row 5 ": {
         "Column 1": 1
      },
      "Row 6 ": {
         "Column 1": 2
      },
      "Row 7 ": {
         "Column 1": 1
      }
   }
}

# Define the fields for the CSV file
csv_fields = ['promoter_features', 'question2', 'question5', 'question6', 'question1', 'question7', 'question8', 'question9', 'question10', 'question11', 'question12', 'question13', 'question14', 'question15', 'question16', 'question17']

# Create a list of dictionaries representing each response
response_list = []
response = {}
for key in csv_fields:
    if key in json_data:
        response[key] = json_data[key]
    else:
        response[key] = ''
response_list.append(response)

# Write the list of dictionaries to a CSV file
with open('responses.csv', mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
    writer.writeheader()
    for response in response_list:
        writer.writerow(response)
