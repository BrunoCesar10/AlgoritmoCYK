import os
dirname = os.path.dirname(__file__)
text_file = os.path.join(dirname, '../file/gramatica.txt')

def file_reader():
    with open(text_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        print(line)

def main():
    file_reader()

if __name__ == '__main__':
    main()