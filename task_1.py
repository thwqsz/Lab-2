import csv

dataset_path = 'books-en.csv'


# пункт 1
def get_obj(data):
    data.seek(0)
    c = 0
    reader = csv.DictReader(data, delimiter=';')
    for i in reader:
        if len(i["Book-Title"]) > 30:
            c += 1
    return c


# пункт 2
def find_book_with_author(data, author):
    data.seek(0)
    reader = csv.DictReader(data, delimiter=';')
    ans2 = []
    for i in reader:
        if i["Book-Author"] == author and (2018 >= int(i["Year-Of-Publication"]) >= 2015):
            ans2.append(i["Book-Title"])
    return ans2


# пункт 3
def task_3(data):
    data.seek(0)
    c = 0
    reader = csv.DictReader(data, delimiter=';')
    with open('task_1.3.txt', 'w') as file:
        for i in reader:
            c += 1
            file.write(f"{i["Book-Author"]}. {i["Book-Title"]} - {i["Year-Of-Publication"]}\n")
            if c == 20:
                break


if __name__ == '__main__':
    with open(dataset_path, encoding='windows-1251') as dataset:
        print(get_obj(dataset))
        print(find_book_with_author(dataset, "Suzanne Brockmann"))
        task_3(dataset)


