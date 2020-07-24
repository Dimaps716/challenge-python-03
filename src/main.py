# Resolve the problem!!
import re, os 


def run():
    # Start coding here
    # pongo toda la ruta del archivo porque estoy trabajando en windows si estubiera en mac solo colocaria "encode.txt"
    #Es neserio que la ruta del archivo tenga boble barra invertida "\\" de lo comtrario dara erro "(unicode error) 'unicodeescape' "
    with open ("C:\\Users\\MARIA ANGELICA\\Cursos_DIMA\\git_clone\\challenge-python-03\\src\\encoded.txt", 'r', encoding='utf-8') as file:
        regex = re.compile('[a-z]')
        mensaje = re.findall(regex, file.read())
        print(''.join(mensaje))
  


if __name__ == '__main__':
    run()
