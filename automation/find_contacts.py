import re

with open("assets/potential-contacts.txt") as f:
    all_data = f.read()

emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', all_data)
emails.sort()
emails =list(dict.fromkeys(emails))

phone_numbers = re.findall(r"\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}", all_data)
phone_numbers.sort()
phone_numbers = list(dict.fromkeys(phone_numbers))
list_of_numbers = []

for i in phone_numbers:
    i=i.replace(".","-")  
    i=i.replace(")","-")  
    i=i.replace("(","")  
    if len(i) == 10:
        i = i[:3] + "-" + i[3:6] + "-" + i[6:]
    list_of_numbers.append(i)


with open("assets/phone_numbers.txt" , "w") as f:
    f.write(f"{list_of_numbers}")

with open("assets/emails.txt" , "w") as f:
    f.write(f"{list_of_numbers}")




