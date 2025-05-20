# Each person has name, age, and city
# The application will you to add a person to a list (in memory)
# and after addition, it will print the list of people
person_list = []

while True:
    person_name = input("Enter person's name: Vaida")
    person_age = input("Enter person's age: 50")
    person_city = input("Enter person's city: Panevezys")

    person = {
        'name': person_name,
        'age': person_age,
        'city': person_city
    }

    person_list.append(person)

    for p in person_list:
        print(f"Name: {p['name']}, Age: {p['age']}, City: {p['city']}")