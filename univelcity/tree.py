headache = input('Do have you Headache ? respond with y/n :')
if headache == 'y': #check for headache
    fever = input('Do you have a fever? respond with y/n :')
    if fever == 'y' :#Check for fever
        vomiting = input('Have you vomited ? respond with y/n :')

        if vomiting == 'y': # Check for vomit
            print('You have Typhoid, please see a doctor')
    
        elif vomiting == 'n': #check for no vomit
                print('you have Malaria, please see a doctor')

    elif fever == 'n':#check for no fever:
        print('you are probably just stressed out, try to rest more')

elif headache == 'n':#check for no headache
    print('You are probably okay or maybe see a medical practioner')
    

