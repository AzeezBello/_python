import ast
import connect

class User():

    def __init__(self, username = 'general'):
 
        self.username = username.lower()
        self.notes = Storage(self).read()

    def create_note(self):

        title = input('Please enter Title : ')
        body = input('Body of note : ')
        note = Note(title, body)
        formatted_sql = [self.username,note.title, note.body]
        connect.create_table()
        connect.add(formatted_sql)

        # Storage(self).save(note)
    
    def render_notes(self):
        notes_from_sql = (connect.select(self))
        print('Hello {}, below are your notes:\t\n'.format(self.username.upper()))
        
        for note in notes_from_sql:
            print('\t{} ==> {}\n'.format(note['title'], note['body']))


class Note():
    def __init__(self, title = 'empty', body = 'empty'):
        self.title = title
        self.body = body

class Storage():
    
    def __init__(self, user):
        self.user = user

    def save(self, incoming_note):
        data = self.__read_all()
        reg_users = list(data.keys())
        note = [incoming_note.title, incoming_note.body]
        print(note)

        if self.user.username in reg_users: #check if user exists
            data[self.user.username].append(note)

        else:

            data[self.user.username] = []
            data[self.user.username].append(note)

        with open('open.txt', 'w') as file:
            file.writelines(str(data)) 
            file.close()

    
    def __read_all(self):
        with open('open.txt', 'r') as file:
            data = file.read() 

            file.close()

            return {} if len(data)<1 else ast.literal_eval(data) 
    
    def read(self):
        with open('open.txt', 'r') as file:
            data = file.read() 

            file.close()
            try: 
                return {} if len(data)<1 else ast.literal_eval(data)[self.user.username]
            except: 
                return [['NONE','NO NOTES YET']]
        


user = User(username = 'osas')


_note = {'john': [['title', 'new note for me'], ['title', 'new note for me']]}
note = ['title', 'new note for me now today with a happy face']
# user.create_note()
user.render_notes()