from firebase import firebase
firebase = firebase.FirebaseApplication('https://pythontest-ac619.firebaseio.com/', None)

data =  {
          'Name': 'Hawlette Packard',
          'RollNo': '4su15cs023',
          'Percentage': 85.02,
          'Phone': 7451231412
          }
result = firebase.post('/pythontest-ac619/Student', data)
print(result)
