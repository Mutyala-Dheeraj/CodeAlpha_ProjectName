# TASK 3: Extract Email Addresses from a Text File

import re

# Open and read the text file
file = open("sample.txt", "r")
content = file.read()

# Find all email addresses using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Save extracted emails into another file
output = open("emails.txt", "w")

for email in emails:
    output.write(email + "\n")

# Close files
file.close()
output.close()

print("Email addresses extracted successfully!")
print("Saved in emails.txt")