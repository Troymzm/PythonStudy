data = "[{'name': '1', 'gender': '1', 'id': '23331866', 'classes': [{'number': '12345678', 'name': '1', 'teacher': '1', 'position': '5301', 'time': '9:00-10:30', 'engagestudents': []}], 'password': 'aaron33120', 'grades': [], 'email': '123', 'tel': '15609885921'}]"

new_list = eval(data)
for i in new_list:
    for j in i:
        print(i[j])