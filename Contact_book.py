import pyperclip 
contacts = {'BASI': '001122335', 'JOY': '299889427'}
w = True

while w:
    print('Enter a contact name: (blank to quit)')
    name = input().upper()
    if name == '':
        break

    if name in contacts:
        print(name, contacts[name])

    else:
        print('I do not have contact information for ' + name )
        print('What is their digit?')
        phone = int(input('>'))
        contacts[name] = phone
        print('Contact database updated.')
        # print('Enter "x" to stop else continue.')
        # end = input(">")
        # if end == "x":
        #     break
        # else:
        #     continue
    w = False
order = []
for k, v in contacts.items():
    
    setter = f'{k}--{v}'
    # pyperclip.copy(setter)
    order.append(setter)
pyperclip.copy('\n'.join(order))
# print()
with open('contact_list.txt', 'w', encoding='UTF-8') as file_obj:
    file_obj.write(pyperclip.paste())

with open('contact_list.txt', encoding='UTF-8') as file_obj:
    content = file_obj.read()
    

# i had a pretty hazy one with this one lol
# this program lets you enter names and phone numbers and it automatically stores it in a text file,
#  "contact_list.py" in a very organized format.
# here i used a lot of lines of code for what i assumed should only take less
# im sha glad that im building my confidence and critical thinking gradually this took me less than 2 hrs to complete without the help of any AI. 

