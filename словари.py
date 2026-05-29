class_data = {
    "Аня": {
        "Математика": [5, 4],
        "История": [3, 5]
    },
    "Максим": {
        "Математика": [4, 4],
        "История": [5]
    }
}

class_data["Аня"]["История"].append(4)
class_data["Максим"]["Математика"].append(5)

grades_1 = class_data["Аня"]["Математика"]
grades_2 = class_data["Максим"]["История"]

avarage_1 = sum(grades_1)/len(grades_1)
avarage_2 = sum(grades_2)/len(grades_2)

print("Средний балл Ани:", avarage_1)
print("Средний балл Максима", avarage_2)

print(class_data)