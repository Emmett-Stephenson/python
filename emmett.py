database = {'user1': 'emmettStephenson', 'binary_of_user1': '01011010 01010111 00110001 01110100 01011010 01011000 01010010 00110000 01100011 00110000 01100100 01110000 01100100 01000111 01101000 00110001 01011001 01100111 00111101 00111101'}
var1 = database['user1']
var2 = database['binary_of_user1']
print(var1 + var2)
login = input("Login by typing yes.")
if login == "yes":
  print("We only have 1 person in our database, emmettStephenson. You will have to find his password to login.")
  loginattempt = input("Type password for emmettStephenson")
if loginattempt == "emmettsGithub":
  print("You have cracked the password! Login succsessful.")
else:
  print("You lose! GET OUTTA HERE!")
  exit()
