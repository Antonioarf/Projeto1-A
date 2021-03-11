
def extract_route(string):
    i = string.find('/') +1
    f = string[i:].find(' ') 
    route = string[i:f+i]
    return route
    
def read_file(path):

    path = str(path)

    if path.endswith('.txt') or path.endswith('.html') or path.endswith('.css'):
        file = open(path, "rb")
        return file.read()

    else:
        file = open(path, "rb")
        return file.read()


def load_data(file):
    import json
    with open('data/{0}'.format(file)) as json_file: 
        data = json.load(json_file) 
    return data


def load_template(file):
    import codecs
    f=codecs.open("templates/{0}".format((file)), 'r',encoding='utf8')
    return f.read()


# def add_json(dict):
#     import json
#     with open('data/notes.json', "r", encoding='utf8') as json_file: 
#         data = json.load(json_file) 

    # data.append(dict)

    # with open('data/notes.json', 'w') as json_file:
    #     json.dump(data, json_file)



def build_response(body='', code=200, reason='OK', headers=''):
    if body == "" and headers == "":
        return (bytes(str("HTTP/1.1" +" "  + str(code) +" "+ reason +  headers+ body+"\n\n"),'UTF-8'))
    elif headers == "":
        return (bytes(str("HTTP/1.1" +" "  + str(code) +" "+ reason +"\n\n"+ body ),'UTF-8'))
    else:
        return(bytes(str("HTTP/1.1" +" "  + str(code) +" "+reason +"\n"+ headers+ "\n\n" ),'UTF-8'))

# b'HTTP/1.1 302 See Other\nLocation /\n\n'
# b'HTTP/1.1 302 See OtherLocation /\n\n'