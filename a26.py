# indent your Python code to put into an email
from pathlib import Path

python_files = Path().glob('*.py')
for file_name in sorted(python_files):
    print (f'    ------{file_name}')

    with open(file_name) as f:
        for line in f:
            print ('    ' + line.rstrip())

    print()
