#CRUD OPERATIONS ON A LIST

a_list = [
    {
        'name': 'Meezan',
        'age': 24
    },
    {
        'name': 'Some one',
        'age': 30
    },
    {
        'name': 'Sme two',
        'age': 52
    }
]

def add(name, age):
    a_list.append({name, age})

def edit(name, updated_name):
    for i in a_list:
        if(a_list[i]['name']==name):
            i.update({updated_name, a_list[i]['age']})

def delete():
    return

edit()