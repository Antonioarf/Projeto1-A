from utils import load_data, load_template, build_response
from database import Database, Note
from urllib.parse import *

def index(request, db):
    if request.startswith('POST'):
        request = request.replace('\r', '')
        # request = request.encode(encoding='UTF-8')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus

        for chave_valor in corpo.split('&'):
            chave_valor = unquote_plus(chave_valor)
            div = chave_valor.split('=')
            
            params[div[0]]= div[1]
            print(chave_valor)

        note = Note()
        note.title = params["titulo"]
        note.content = params["detalhes"]

        if "atualizar" in params.keys():
            note.id = params["atualizar"]
            db.update(note)
        elif "apagar" in params.keys():
            db.delete(params["apagar"])
        else:
            db.add(note)

        return build_response(code=303, reason='See Other', headers='Location: /')

    elif request.startswith('GET'): 

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
        note_template = load_template('components/note.html')
        notes_li = [note_template.format(title=note.title, details=note.content, id = note.id) for note in db.get_all()]
        notes = '\n'.join(notes_li)
        # print(notes)
        return build_response(load_template('index.html').format(notes=notes)) # .format(notes=notes)
    
# return load_template('index.html').format(notes=notes).encode()