
import json
import os

myFile= "students.json"
# students = []


def display_menu():
    print("a - add") 
    print("d - delete")
    print("u - update")
    print("p - print all") 
    print("x - exit") 

def add_student(students):
    temp_student = input('student name?')
    students.append(temp_student)
    print('a contact added')

def printAll():
    students = loadFromFile()
    for student in students:
        print(student)

def loadFromFile():
    isExist = os.path.exists(myFile)
    if isExist:
        with open(myFile, 'r') as openFile:
            students = json.load(openFile)
        return students
    return []

def save2File(students):
    jsonString = json.dumps(students, indent=4)
    with open(myFile, "w") as outfile:
	    outfile.write(jsonString)

def handleAdd():
    name = input("Please enter name: ")
    age = input("Please enter age: ")
    city = input("Please enter city: ")

    students = loadFromFile() 
    maxId = 0
    for stu in students:
        if stu['id'] > maxId : 
            maxId = stu['id']
    newStudent = {"id":maxId + 1, "name": name, "age": age, "city": city}
    students.append(newStudent)
    save2File(students)
    print("New student added")


def handleUpdate():
    idUpd = input('Please enter id to update: ')
    students = loadFromFile() 
    studentFound = False
    for stu in students:
        if stu['id'] == int(idUpd):
            studentFound = True
            newName = input ('please enter the updated name: ')
            newAge = input ('please enter the updated age: ')
            newCity = input ('please enter the updated city: ')
            stu['city'] = newCity
            stu['age'] = newAge
            stu['name']= newName
            print("student is updated ")
            save2File(students)
    if (studentFound == False):
        print('id not found, try again')

def handleDelete(): 
    id = input ('please enter id to delete: ')
    students = loadFromFile() 
    studentFound = False
    for stu in students:
        if stu['id'] == int(id):
            studentFound = True
            students.remove(stu)
            print('id deleted')
            save2File(students) 
    
    if (studentFound == False):
        print('id not found, try again')



def main():

    while(True):
        display_menu()
        selection = input()

        if selection == 'a':
            handleAdd()
        elif selection == 'd':
            handleDelete()
        elif selection == 'p':
            printAll()
        elif selection == 'u':
            handleUpdate()
        elif selection == 'x':
            break
        else:
            print(f"{selection} is not a valid selection")
            continue
    
    
if __name__ == '__main__':
    main()
 
