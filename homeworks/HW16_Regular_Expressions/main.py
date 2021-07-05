import re


with open('django_success.log') as log_file:
    changes = ''.join(log_file.readlines())
    changes = re.sub(r'\[\d*\/\w*\/\d*\s(\d{2}:?){3}\]', '[XX/XXX/XXXX XX:XX:XX]', changes)

    changes = re.sub(r'\/admin\/', '/####/', changes)
    with open('new_django_success.log', 'a') as file:
        file.write(changes)
