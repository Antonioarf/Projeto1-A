import sqlite3
class Database:

    def __init__(self,nome):
        import sqlite3
        self.conn = sqlite3.connect(nome+".db")
        print(nome+".db")
        self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT , content TEXT NOT NULL);")
    
    def add(self, teste):
        
        self.conn.execute("INSERT INTO note (title, content) VALUES  ('{0}' , '{1}');".format(teste.title, teste.content))
        self.conn.commit()
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    def get_all(self):
        return [Note(linha[0],linha[1],linha[2]) for linha in self.conn.execute("SELECT id, title, content FROM note")]

    def update(self, entry):
        # self.conn.execute("UPDATE note SET title = '{}', content = '{}' WHERE id = {} );".format(entry.title, entry.content,entry.id))
        self.conn.execute("UPDATE note SET title = '{}' WHERE id = {} ;".format(entry.title, entry.id))
        self.conn.execute("UPDATE note SET content = '{}' WHERE id = {} ;".format(entry.content,entry.id))
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute("DELETE FROM note WHERE id = {} ;".format(note_id))
        self.conn.commit()


from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''