
user_inp='random'
data=[]

def show_menu():
    print('1.Add to list')
    print('2.Mark as done')
    print('3. View list')
    print('4.Exit')


while user_inp!='4':
    show_menu()
    user_inp=input('Select an option: ')

    if  user_inp=='1':
        item=input('What do you want to add? ')
        data.append(item)
    elif user_inp=='2':
        item=input('What do you want to mark as done? ')
        if item in data:
            data.remove(item)
            print('Removed item:', item)
    elif user_inp=='3':
        print('Viewing List: ')
        for item in data:
            print(item)
        print()
    elif user_inp=='4':
        print('GoodBye')
    else:
        print('Enter valid option')


