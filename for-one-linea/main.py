# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # exclusive = 'exclusive-value'
    exclusive = None
    durable = 'durable-value'
    auto_delete = None
    options = {k: v for k, v in
               {'name': name, 'exclusive': exclusive, 'durable': durable, 'auto_delete': auto_delete}.items()
               if v is not None}
    print(options)


    required_fields = ['name', 'lname', 'phone', 'email']
    data = {
        "name": 'oscar',
        "phone": '55221458'
    }

    missing_fields = [f for f in required_fields if f not in data.keys()]
    print(missing_fields)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
