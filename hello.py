from firebase import firebase
firebase = firebase.FirebaseApplication('https://<example-app-id>firebaseio.com/', None)

data =  {
          'Name': 'Hawlette Packard',
          'RollNo': '4su15cs023',
          'Percentage': 85.02,
          'Phone': 7451231412
          }
result = firebase.post('/<example-app-id>-<app-number>/Student', data)
print(result)
