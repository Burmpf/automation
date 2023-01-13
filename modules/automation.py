import re


email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_regex = r'\b(?:\+?1[-. ]?)?\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})|([0-9]{7})\b$'


with open('./assets/potential_contacts.txt', 'r') as f:
    text = f.read()

emails = set(re.findall(email_regex, text))
phones = set(re.findall(phone_regex, text))



emails = sorted(emails)
phones = sorted(phones)

phone_list = ['{}-{}-{}'.format(number[0], number[1], number[2]) for number in phones]


with open('outputs/emails.txt', 'w') as f:
    for email in emails:
        f.write(email + '\n')

with open('outputs/phone_numbers.txt', 'w') as f:
    for phone in phone_list:
        f.write(phone + '\n')