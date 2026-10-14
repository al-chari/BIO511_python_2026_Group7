# Possible Hospital Class:
class Patient():
    def __init__(self, name, date_of_reception, disease):
        self.name = name
        self.date_of_reception = date_of_reception
        self.disease = disease

patient1 = Patient("Markus", 20261009, "pneumotorax")

print(patient1)
# OUTPUT: <__main__.Patient object at 0x00000227629B86E0>

print(patient1.disease)
# OUTPUT: pneumotorax

# Possible Videogame Class:
class User():
    def __init__(self, username, password, account_level, gold):
        self.username = username
        self.password = password
        self.account_level = account_level
        self.gold = gold

user1 = User("xXmarkusXx", "pojHIOK2H#", 45, 550)

print(user1)
# OUTPUT: <__main__.User object at 0x0000022273E48830>

print(user1.account_level)
# OUTPUT: 45

# Possible University Class:
class Alumni():
    def __init__(self, username, email, password, faculty, degree):
        self.username = username
        self.email = email
        self.password = password
        self.faculty = faculty
        self.degree = degree

alumni1 = Alumni("marpor4","marpor4@student.gu.se" ,"pojHIOK2H#", "Science and Technology", "Masters in Bioinformatics")

print(alumni1)
# OUTPUT: <__main__.Alumni object at 0x00000259931A8980>

print(alumni1.email)
# OUTPUT: marpor4@student.gu.se

# Possible book class (also works as an example of a library class too):
class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book1 = Book("Anna Karenina", "Leo Tolstoy", 1877)

print(book1)
# OUTPUT: <__main__.Book object at 0x0000029F46F98AD0>

print(book1.author)
# OUTPUT: Leo Tolstoy
