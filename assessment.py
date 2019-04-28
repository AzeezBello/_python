import ast

class Info():
 
    def __init__(self, username):
    
            self.username = username.lower()
            # self.information = Storage(self).read()

    def bio(self):
        firstname = input('Please enter your Firstname : ')
        lastname = input('Please enter your Lastname : ')
        parental_background  = input('Wheere you raised by single parents  [yes/no] : ')
        employment_record = input('Please enter your Employment Record  [yes/no] : ')
        criminal_record = input('Please enter your Criminal Record  [yes/no] : ')

        

    def academic(self):
        education_level = input('Are you a graduate [yes/no] : ')
        result = input('what class of result do you have [1st class/ 2nd class/ 3rd class] : ')
        post_school = input('years after graduation [1-5] : ')
        educational_awards = input('Are you a graduate [yes/no] : ')
        
        

    def skills(self):
        writing_skill = input('Writing skills [Excellent/Average/poor]: ')
        reading_skill = input('Reading skills [Excellent/Average/poor]: ')
        communication_skill = input('Communication skills [Excellent/Average/poor]: ')
        computer_skill = input('Computer skills [Excellent/Average/poor]: ')
        leadership_skill = input('Leadership skills [Excellent/Average/poor]: ')

       



class Assessment():
    score = 0'
a

    pass



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
        
     
     
     
     