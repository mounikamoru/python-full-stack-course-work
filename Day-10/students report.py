data = {
    'anju':{'status':True,'python':99,'mysql':90,'django':97},
    'manideep':{'status':True,'python':35,'mysql':22,'django':33},
    'bhuvan':{'status':True,'python':80,'mysql':75,'django':77},
    'himaja':{'status':True,'python':66,'mysql':55,'django':44},
    'manoj':{'status':True,'python':44,'mysql':39,'django':42},
    'deepak':{'status':False}
    }

name = input("enter your name:")
if name in data:
    if data[name]['status']:
        sum = data[name]['python'] + data[name]['mysql'] + data[name]['django']
        avg = sum/3
        if avg >= 90:
            print(f'congrats {name}, you got first class')
        elif avg >= 75:
            print(f'Good {name}, wish you all the best better luck next time')
        elif avg >= 50:
            print(f'{name}, need improvement')
        elif avg >= 35:
            print(f'Bad {name}, work hard next time')
        else:
            print(f'{name}, you failed in the exam, bring your parents')
    else:
        print(f'{name}, you have not written the exams. please bring your parents')
else:
    print(f'{name} data is not found')
