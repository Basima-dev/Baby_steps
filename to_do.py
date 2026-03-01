
import re, pyperclip
toDo = ['bath', 'cook', 'clean']
done = ['eat', 'brush']

F = True
while F:
    pyperclip.copy('\n'.join(toDo))
    

    print('To Do list:\n','\n'.join(toDo))
    with open('ToDo_list.txt', 'w', encoding='UTF-8') as file_obj:
        file_obj.write('To Do list:\n')
        file_obj.write(pyperclip.paste())
    print(f'Completed:\n','\n'.join(done))
    pyperclip.copy('\n'.join(done))
    with open('ToDo_list.txt', 'a', encoding='UTF-8') as file_obj:
        file_obj.write('\nCompleted Tasks:\n')
        file_obj.write(pyperclip.paste())
    what = input('Enter: a-add task, r-remove task and c + "the task"- to complete (leave blank to close)>>')
    if what == 'a':
        add = input('Add something >>')
        toDo.append(add)

    elif what == 'r':
        sub = input("Enter the item or it's index>>")
        toDo.remove(sub)
    elif what == 'c':
        change = input('Enter the completed task>>')
        toDo.remove(change)
        done.append(change)
    else:
        
        F = False
    



        

        



