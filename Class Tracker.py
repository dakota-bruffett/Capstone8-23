classes = []
while True:
    class_name = input('Enter name of class or enter to quit')
    if class_name == '':
        break
        classes.append(class_name)

    for class_name in classes:
        print(class_name)
